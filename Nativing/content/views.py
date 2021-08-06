from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView
from django.db.models import Q
from . models import ContentUpload, RELATION_CHOICES
from .forms import ContentUploadForm
from django.http import JsonResponse
from taggit.models import Tag

import numpy as np


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
    if relation == "SENIOR":
        temp = "senior"
    if relation == "WORK":
        temp = "work"
    return temp


def explore(request):
    content_all = ContentUpload.objects.all()
    print("type of request : ", type(request))
    print("type of object_all : ", type(content_all))
    keyword_query = request.GET.get('keyword')
    
    if keyword_query:
        print("키워드는: ", keyword_query)
        content_all = content_all.filter(
            Q(title__icontains = keyword_query) | 
            Q(expression__icontains = keyword_query) |
            Q(expression_descript__icontains = keyword_query)).order_by('-datetime')
    else:
        print("키워드 없")
    
    relationships  = np.array(RELATION_CHOICES)[:, 0]
        
    print("relation tag들: ", relationships,type(relationships))
            
    return render(request, 'test_explore.html', {'content_all' : content_all,
                                             "keyword": keyword_query,
                                             "relationships" : relationships},)

def explore2(request):
    return render(request, "explore.html")

                                             
def explore_filter(request):
    content_all = ContentUpload.objects.all().prefetch_related('tag')
    # content_all = ContentUpload.objects.raw("SELECT * FROM content_ContentUpload")
    data = content_all.values()
    for content in data:
        new_content = content
        new_content['tag'] = []
        for tag in ContentUpload.objects.get(id=1).tag.all():
             new_content['tag'].append(str(tag))
    return JsonResponse(list(data), safe = False)

def content_detail(request, content_id):
    content_detail = get_object_or_404(ContentUpload, pk = content_id)
    return render(request, 'content_detail.html', {"detail" : content_detail})