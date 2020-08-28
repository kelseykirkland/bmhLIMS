from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
# from .forms import UploadFileForm

from django.views import View
from django.views.generic import TemplateView
from bmhlims.bmhlims.uploader import verify_samplesheet
from bmhlims.bmhlims.uploader.verify_samplesheet import *


class UploadSampleFileView(View):
    template_name = "uploader/sample_uploader.html"
    success_url = 'result/'

    def home_view(self, request):
        print(request.POST)
        return render(request, self.template_name)

    def post(self, request):
        return redirect(self.success_url)


uploader_sample_sheet_view = UploadSampleFileView.as_view()


class UploadFileResult(View):
    template_name = "uploader/sample_uploader_result.html"

    def post(self, request, *args, **kwargs):
        fname = request.POST('filename')

        # readfile sends to verify_samplesheet.py
        # opens parses file row by row
        # returns a tuple (result, errorMessages)
        # result is a string SUCCESS or FAIL
        # errorMessages is a list of strings of the error messages or an empty list
        result = readfile(fname)
        context = {'success': True,
                   'url': self.success_url,
                   'result': result[0],
                   'messages': result[1]}
        return JsonResponse(context)


uploader_result_view = UploadFileResult.as_view()



