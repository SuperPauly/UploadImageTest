from django import forms
from django.db.models import fields
from .models import Images, Post


class UploadForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['name', 'file']


class PostTitle(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['tile']
    # title = forms.CharField(max_length=64, required=False)
    # file = forms.ImageField()
