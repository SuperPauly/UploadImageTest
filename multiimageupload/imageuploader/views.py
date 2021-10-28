from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .forms import UploadForm, PostTitle
from uuid import uuid4
from django.core import serializers
from django.core.files.storage import FileSystemStorage

# Create your views here.


def upload(request):
    form = UploadForm()
    formm = PostTitle()
    return render(request, 'test.html', context={"form": form, "formm": formm})


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
        uf = UploadForm(request.POST, request.FILES)
        pf = PostTitle(request.POST)
        if uf.is_valid() and pf.is_valid():
            uf.save()
            pf.save()
            return JsonResponse({"FUCK": "serial"}, status=200)
        return JsonResponse({"img_url": "serial"}, status=200)
    return JsonResponse({"No": "Upload"}, status=200)
