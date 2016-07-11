from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^question/', views.home, name='home'),
]
