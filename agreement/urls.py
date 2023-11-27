from django.urls import path

from . import views

urlpatterns = [
    path("agreement/htmx", views.AgreementTableHTMXView.as_view(), name="agreement.htmx"),
    path("agreement/new", views.AgreementCreateView.as_view(), name="agreement.new"),
    path("agreement/<int:pk>/edit", views.AgreementUpdateView.as_view(), name="agreement.update"),
    path("agreement/<int:pk>/delete", views.AgreementDeleteView.as_view(), name="agreement.delete"),
    path("agreement/<int:pk>", views.AgreementDetailView.as_view(), name="agreement.details"),
    path("agreement/htmx/action", views.response_action, name="agreement.htmx.action"),
    path("agreement/status_update", views.update_agreement_status, name="agreement.status.update"),
    path("agreement/<int:pk>/generate_pdf", views.generate_pdf, name="agreement.generate.pdf"),
]
