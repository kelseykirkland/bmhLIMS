from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
#from .forms import UploadFileForm

# Imaginary function to handle an uploaded file.
# in verify_samplesheet.py
#from somewhere import handle_uploaded_file

from django.views import View
from django.views.generic import TemplateView


#class UploadSampleFileView(View):
#    template_name = "uploader/sample_uploader.html"
#    success_url = ''

def my_pretty_view(request):
    print(request.POST)
    raise Exception("Poop")
    return render(request, "sample_uploader.html")
  # if request.method == 'POST':
  #      if 'pieFact' in request.POST:
  #          pieFact = request.POST['pieFact']
  #          # doSomething with pieFact here...
  #          return HttpResponse('success')  # if everything is OK
  #      # nothing went well
  #      return HttpResponse('FAIL!!!!!')


#uploader_sample_sheet_view = UploadSampleFileView.as_view()








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

