from django.urls import path
from django.conf.urls import url

from . import views
from .views import uploader_sample_sheet_view, uploader_result_view

app_name = "uploader"
urlpatterns = [
    # Enter file page
    path("", view=uploader_sample_sheet_view,  name="upload_sample_sheet"),

    # Verification result page
    path("result/", view=uploader_result_view, name="upload_result")

]
