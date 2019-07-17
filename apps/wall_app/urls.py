from django.conf.urls import url
from . import views, models

urlpatterns = [
    url(r'^$', views.index),
    url(r'^wall$', views.wall),
]