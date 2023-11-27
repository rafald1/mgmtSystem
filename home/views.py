from datetime import datetime

from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView


class HomeView(TemplateView):
    template_name = "welcome.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["today"] = datetime.now()
        return context


class LoginInterfaceView(LoginView):
    template_name = "login.html"


class LogoutInterfaceView(LogoutView):
    template_name = "logout.html"
