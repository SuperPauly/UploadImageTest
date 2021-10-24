from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .forms import UploadForm
from .models import Images
from uuid import uuid4
from django.core import serializers
from django.core.files.storage import FileSystemStorage

# Create your views here.


def upload(request):
    form = UploadForm()

    # instance = Images(file=file, name=str(uuid4()))
    # instance.save()
    # instance.save()
    return render(request, 'test.html', context={"form": form})


def uploadImage(request):
    print("in func")
    # serial = serializers.serialize(
    #     "json", [{"hi": "test", "boo": "fdfs"}, ])
    if request.method == 'POST':
        print("passed if")
        # fs = FileSystemStorage()
        # print(fs)
        for ff in request.FILES.items():
            # filename = fs.save(ff.name, ff)
            print(ff.name)
            # uploaded_file = fs.url(filename)
            # print("UPLOADED TO ----> " + uploaded_file)
        return JsonResponse({"img_url": "serial"}, status=200)
    return JsonResponse({"none": "serial"}, status=200)
