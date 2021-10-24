from django import forms


class UploadForm(forms.Form):
    title = forms.CharField(max_length=64, required=False)
    file = forms.ImageField()
