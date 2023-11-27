from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DetailView
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect, HttpResponse
from django.db import transaction
from django.shortcuts import redirect, render, get_object_or_404

from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from .tables import AgreementTable
from .models import Agreement
from .forms import AgreementForm, AgreementStatusUpdateForm
from .filters import AgreementFilter

from agreement.utils.agreement_to_pdf import insert_values_to_pdf_template


class AgreementCreateView(LoginRequiredMixin, CreateView):
    model = Agreement
    template_name = "agreement_form.html"
    success_url = "/agreement/htmx"
    form_class = AgreementForm
    login_url = "/login"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class AgreementUpdateView(LoginRequiredMixin, UpdateView):
    model = Agreement
    success_url = "/agreement/htmx"
    template_name = "agreement_form.html"
    form_class = AgreementForm
    login_url = "/login"


class AgreementDetailView(LoginRequiredMixin, DetailView):
    model = Agreement
    context_object_name = "agreement"
    template_name = "agreement_details.html"
    login_url = "/login"


class AgreementDeleteView(LoginRequiredMixin, DeleteView):
    model = Agreement
    success_url = "/agreement/htmx"
    template_name = "agreement_delete.html"
    login_url = "/login"


class AgreementTableHTMXView(LoginRequiredMixin, SingleTableMixin, FilterView):
    table_class = AgreementTable
    queryset = Agreement.objects.all()
    filterset_class = AgreementFilter
    paginate_by = 10
    login_url = "/login"

    def get_template_names(self):
        if self.request.htmx:
            template_name = "agreement_table_partial.html"
        else:
            template_name = "agreement_table_htmx.html"
        return template_name


class HttpResponseHXRedirect(HttpResponseRedirect):
    status_code = 200

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self["HX-Redirect"] = self["Location"]


@login_required(login_url="/login")
def response_action(request):
    if request.method == "POST" and request.htmx:
        selected_ids = request.POST.getlist("selection")
        actions = {
            "new": {
                "path": "/agreement/new"
            },
            "edit": {
                "path": "/agreement/{}/edit",
                "message": "Edit operation can only be performed on 1 agreement."
            },
            "details": {
                "path": "/agreement/{}",
                "message": "Details operation can only be performed on 1 agreement."
            },
            "delete": {
                "path": "/agreement/{}/delete",
                "message": "Delete operation can only be performed on 1 agreement."
            },
            "status": {
                "path": "/agreement/status_update",
                "message": "Status update has to be performed on at least 1 agreement.",
                "set_session": True
            },
            "to_pdf": {
                "path": "/agreement/{}/generate_pdf",
                "message": "Generate PDF can only be performed on 1 agreement."
            }

        }
        trigger_name = request.htmx.trigger_name
        action = actions.get(trigger_name)
        if action:
            if action.get("set_session"):
                request.session["selected_ids"] = selected_ids
            if trigger_name == "new" or "{}" not in action["path"] and len(selected_ids) >= 1:
                return HttpResponseHXRedirect(action["path"])
            elif len(selected_ids) == 1:
                return HttpResponseHXRedirect(action["path"].format(selected_ids[0]))
        return HttpResponse(action["message"] if action else "Invalid action")


@login_required(login_url="/login")
def update_agreement_status(request):
    selected_ids = request.session["selected_ids"]
    agreements = Agreement.objects.filter(id__in=selected_ids)
    if request.method == "POST":
        form = AgreementStatusUpdateForm(request.POST)
        if form.is_valid():
            new_status = form.cleaned_data["status"]
            with transaction.atomic():
                agreements.update(status=new_status)
            return redirect("agreement.htmx")
    else:
        form = AgreementStatusUpdateForm()
    return render(request, "agreement_status.html", {"form": form, "agreements": agreements})


@login_required(login_url="/login")
def generate_pdf(_, pk):
    agreement = get_object_or_404(Agreement, pk=pk)
    buffer = insert_values_to_pdf_template(agreement)
    buffer.seek(0)
    response = HttpResponse(buffer, content_type="application/pdf")
    response["Content-Disposition"] = f"filename=agreement_id_{pk}.pdf"
    return response
