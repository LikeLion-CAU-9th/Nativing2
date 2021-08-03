from django import forms
from . models import ContentUpload

class ContentUploadForm(forms.ModelForm):
    class Meta:
        model = ContentUpload
        fields = ['title', 'expression', 'expression_descript', 'image', 'tag', 'expression_descript_select', 'relation_select']