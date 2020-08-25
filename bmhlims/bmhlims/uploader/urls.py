from django.urls import path
from django.conf.urls import url

from . import views
from .views import my_pretty_view

app_name = "uploader"
urlpatterns = [
    # Index
    path("",  my_pretty_view)



]
