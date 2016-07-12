from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^question/(?P<id>\d+)/$', views.single, name='question_single'),
    url(r'^question/$', views.home, name='home'),
]
