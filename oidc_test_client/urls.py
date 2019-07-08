from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from .views import HomePageView
from .views import logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^oidc/', include('mozilla_django_oidc.urls')),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^logout/$', logout),
]
