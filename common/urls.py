from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^status/$', views.status),
    url(r'^clear/$', views.clear)
]