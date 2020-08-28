from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
#from .forms import UploadFileForm

# Imaginary function to handle an uploaded file.
# in verify_samplesheet.py
#from somewhere import handle_uploaded_file

from django.views import View
from django.views.generic import TemplateView


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

    def get_file(request):
        if request.method == 'POST':
            fname = request.POST
            return HttpResponseRedirect('/thanks/')
        return render(request, 'sample_uploader.html')


uploader_result_view = UploadFileResult.as_view()


#class UploadSampleSheetView():
#    template_name = ""


#def upload_file(request):
#    if request.method == 'POST':
#        form = UploadFileForm(request.POST, request.FILES)
#        if form.is_valid():
#            # the function I make to handle file v
#            #handle_uploaded_file(request.FILES['file'])
#            return HttpResponseRedirect('/success/url/')
#    else:
#        form = UploadFileForm()
#    return render(request, 'upload.html', {'form': form})

