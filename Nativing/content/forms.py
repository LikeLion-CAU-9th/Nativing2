from django import forms
from django.forms import ModelForm, TextInput, Select, FileInput, RadioSelect
from . models import ContentUpload 

class ContentUploadForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ContentUploadForm, self).__init__(*args, **kwargs)
        self.fields['agree'].required = True
        self.fields['image'].required = True

    class Meta:
        model = ContentUpload
        fields = ['title','expression', 'expression_descript', 'image', 'tag', 'expression_descript_select', 'relation_select','agree']
        widgets = {
            'title' : TextInput(attrs={
                'placeholder' : "제목을 입력하세요.",
                'class' : "title_input"
            }),
             'expression' : TextInput(attrs={
                'placeholder' : "핵심표현을 입력하세요.",
                'class' : "expression_tag_input"
            }),
             'expression_descript' : TextInput(attrs={
                'placeholder' : "핵심표현에 대한 설명을 입력하세요.",
                 'class' : "expression_tag_input"
            }),
             'tag' : TextInput(attrs={
                'placeholder' : "해시태그를 입력하세요.(최대 5개)",
                'class' : "expression_tag_input"
            }),
            'expression_descript_select' : Select(attrs={
                'class' : "drop_down",
            }),
            'relation_select' : Select(attrs={
                'class' : "drop_down_relation",
            }),
             'image' : FileInput(attrs={
                'class' : "image_button",
                'style' : "display: block",
                'id' : "input-image",
            }),
            
        }