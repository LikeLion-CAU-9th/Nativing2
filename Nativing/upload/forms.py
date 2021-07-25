from django import forms
from . models import Content_upload

class Content_upload_Form(forms.ModelForm):
    class Meta:
        model = Content_upload
        fields = '__all__'