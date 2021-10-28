from django import forms
from .models import Images


class UploadForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = '__all__'
    # title = forms.CharField(max_length=64, required=False)
    # file = forms.ImageField()
