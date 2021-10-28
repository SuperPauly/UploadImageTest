from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .forms import UploadForm
from uuid import uuid4
from django.core import serializers
from django.core.files.storage import FileSystemStorage

# Create your views here.


def upload(request):
    form = UploadForm()

    return render(request, 'test.html', context={"form": form})


def handle_uploaded_file(f):
    with open('some/file/name.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def uploadImage(request):
    print("iner")
    print(request.FILES)
    if request.method == 'POST':
        fss = FileSystemStorage()
        for filename, file in request.FILES.items():
            fss.save(filename, file)
        
        ff = UploadForm(name="dsad")
        if ff.is_valid():
        return JsonResponse({"img_url": "serial"}, status=200)
    return JsonResponse({"No": "Upload"}, status=200)
