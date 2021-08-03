from django.shortcuts import render
from django.views.generic import CreateView
from . models import ContentUpload
from .forms import ContentUploadForm

class CreateContentUploadView(CreateView):
    model = ContentUpload
    form_class = ContentUploadForm
    template_name = 'content_upload.html'
    success_url = '/'

def expresstionENG(request):
    expression = ContentUpload.expression_descript_select
    if expression == "ABBREVIATION":
        temp = "abbreviation"
    if expression == "NEOLOGISM":
        temp = "neologism"
    return temp

def relationENG(request):
    relation = ContentUpload.relation_select
    if relation == "FAMILY":
        temp = "family"
    if relation == "FRIEND":
        temp = "friend"
    return temp






 