from django import forms

class UploadImageForm(forms.Form):
    title = forms.CharField(max_length=50)
    #file = forms.FileField()
    image = forms.ImageField()