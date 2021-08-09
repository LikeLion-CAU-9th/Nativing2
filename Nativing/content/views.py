
from django.db.models.expressions import Exists, F
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.views.generic import CreateView
from django.db.models import Q
from accounts.models import User
from . models import ContentUpload, RELATION_CHOICES, Tag, TaggedContent
from .forms import ContentUploadForm
from django.http import JsonResponse
from datetime import date, datetime, timedelta

import numpy as np

def CreateContentUploadView(request):
    if not request.user.is_authenticated:
        return redirect('accounts_login')
    name_temp = request.user.name
    print(name_temp)
    if request.method == "POST":
        form = ContentUploadForm(request.POST, request.FILES)       
        if form.is_valid():   
            new_content = form.save(commit=False)      
            new_content.writer = request.user
            new_content.save()
            form.save_m2m()
            return redirect('/')
    else:
        form = ContentUploadForm()
    return render(request, 'content_upload.html', {'name': name_temp, 'form': form})


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

    tag_db = Tag.objects.all().values() 
    tag_list = list()
    for tag_db_iter in tag_db:
        if tag_db_iter['name'] not in tag_list:
            tag_list.append(tag_db_iter['name'])
        
    print("relation tag들: ", relationships,type(relationships))

               
    return render(request, 'test_explore.html', {'content_all' : content_all,
                                             "keyword": keyword_query,
                                             "relationships" : relationships,
                                             "tags" : tag_list},)

def explore2(request):
    return render(request, "explore.html")

                                             
def explore_filter(request):
    content_all = ContentUpload.objects.all()
    data = np.array(content_all.values())
    
    np_tag = np.array(Tag.objects.all().values())
    np_tag_list = np.array(TaggedContent.objects.all().values())

    for tag_list_iter in np_tag_list:
        tag_id_temp = tag_list_iter['tag_id'] - 1
        tag_list_iter['tag'] = np_tag[tag_id_temp]['name'].strip()

    for tag_list_iter in np_tag_list:
        content_id_temp = tag_list_iter['content_object_id'] - 1
        if 'tag' in data[content_id_temp]:
            data[content_id_temp]['tag'].append(tag_list_iter['tag'])
        else:
            data[content_id_temp]['tag'] = [tag_list_iter['tag']]
    print(np_tag, "태그들")

    writer_all = ContentUpload.objects.select_related("writer__user_age", "writer__user_name")
    print(writer_all.values()[0])
    


    return JsonResponse(list(data), safe = False)

def tags_to_json(request):
    tag_db = Tag.objects.all().values()
    tag_list = list()
    for tag_db_iter in tag_db:
        if tag_db_iter['name'] not in tag_list:
            tag_list.append(tag_db_iter['name'])
    print("상황 tag들: ", tag_list)
    tag_dict = dict({
        "tags" : tag_list,
    })
    print(tag_dict, "태그딕트")
    return JsonResponse(list(tag_list), safe= False)

def content_detail(request, content_id):
    content_detail = get_object_or_404(ContentUpload, pk = content_id)
    return render(request, 'content_detail.html', {"detail" : content_detail})