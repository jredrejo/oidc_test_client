from django.views.generic.base import TemplateView
from mozilla_django_oidc.utils import is_authenticated
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect


class HomePageView(TemplateView):
    template_name = "home.html"

def logout(request):
    if  is_authenticated(request.user):
        auth_logout(request)
    return redirect('/')
