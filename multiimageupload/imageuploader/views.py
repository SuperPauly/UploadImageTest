from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from .forms import UploadForm, PostTitle
from uuid import uuid4
from django.core.files.storage import FileSystemStorage

# Create your views here.


def upload(request):
    form = UploadForm()
    formm = PostTitle()
    return render(request, 'test.html', context={"form": form, "formm": formm})


def uploadImage(request):
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
