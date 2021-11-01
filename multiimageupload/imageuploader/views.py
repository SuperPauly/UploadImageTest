from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .forms import UploadForm, PostTitle
from .models import Post, Images
from uuid import uuid4
import PIL
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
        image = UploadForm(request.POST, request.FILES)
        post = PostTitle(request.POST)
        if image.is_valid() and post.is_valid():
            post.save()
            image.save()
            return JsonResponse({"Saved": request.FILES['file'].name}, status=200)
        return JsonResponse({"method is POST": "serial"}, status=200)
    return JsonResponse({"last JSON": "Upload"}, status=200)
