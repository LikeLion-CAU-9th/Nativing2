from django import forms
from . models import ContentUpload

class ContentUploadForm(forms.ModelForm):
    class Meta:
        model = ContentUpload
        fields = '__all__'