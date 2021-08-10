
from os import write
from django.db.models.expressions import Exists, F
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.views.generic import CreateView
from django.db.models import Q
from pandas.core.reshape.merge import merge
from accounts.models import User
from . models import ContentUpload, RELATION_CHOICES, Tag, TaggedContent
from .forms import ContentUploadForm
from django.http import JsonResponse

import numpy as np
import pandas as pd

def CreateContentUploadView(request):
    if not request.user.is_authenticated:
        return redirect('accounts_login')

    if request.method == "POST":
        form = ContentUploadForm(request.POST, request.FILES)       
        if form.is_valid():   
            new_content = form.save(commit=False)      
            new_content.writer = request.user
            new_content.save()
            form.save_m2m()
            return redirect('explore')
    else:
        form = ContentUploadForm()
        return render(request, 'content_upload.html', {'form': form})


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


def explore_test(request):
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

def explore(request):
    content_all = ContentUpload.objects.all()
    keyword_query = request.GET.get('keyword')
    
    if keyword_query:
        content_all = content_all.filter(
            Q(title__icontains = keyword_query) | 
            Q(expression__icontains = keyword_query) |
            Q(expression_descript__icontains = keyword_query)).order_by('-datetime')
    
    relationships  = np.array(RELATION_CHOICES)[:, 0]

    tag_db = Tag.objects.all().values() 
    tag_list = list()
    for tag_db_iter in tag_db:
        if tag_db_iter['name'] not in tag_list:
            tag_list.append(tag_db_iter['name'])
               
    return render(request, 'explore.html', {'content_all' : content_all,
                                             "keyword": keyword_query,
                                             "relationships" : relationships,
                                             "tags" : tag_list},)

                                             
def explore_filter(request):
    content_all = ContentUpload.objects.all()
    writer_all = ContentUpload.objects.select_related("writer").all()
    tag_all = ContentUpload.objects.prefetch_related("tag").all()
    
    user_values = list()
    for writer_iter in writer_all:
        temp_iter = {"content_id" : writer_iter.id,
                     "user_name" : writer_iter.writer.name, 
                     "user_gender" : writer_iter.writer.user_gender, 
                     "user_age" : writer_iter.writer.user_age,
                     "user_image_url" : writer_iter.writer.user_image.url
                     }
        user_values.append(temp_iter)

    tag_values = list()
    for tag_iter in tag_all:
        temp_list = []
        only_tags = tag_iter.tag.all().values_list("name")
        
        for j in only_tags:
            temp_list.append(j[0])

        temp_iter = {
            "content_id" : tag_iter.id,
            "tag" : temp_list
        }
        tag_values.append(temp_iter)

    contentDF = pd.DataFrame(content_all.values())
    userDF = pd.DataFrame(user_values)
    tagDF = pd.DataFrame(tag_values)
    
    mergedDF = pd.merge(contentDF, userDF, how="left", left_on ="id", right_on="content_id")
    mergedDF.drop(["image", "agree", "content_id",], axis=1, inplace= True)
    
    mergedDF = pd.merge(mergedDF, tagDF, how = "left", left_on="id", right_on="content_id") 
    mergedDF.sort_values(by=['id'], inplace=True, ascending=False)

    mergedDict = mergedDF.transpose().to_dict()
    
    a = writer_all
    for i in a: 
        print(i.writer.user_image.url)

    return JsonResponse(list(mergedDict.values()), safe = False, json_dumps_params={'ensure_ascii': False})


def content_detail(request, content_id):
    content_detail = get_object_or_404(ContentUpload, pk = content_id)
    return render(request, 'content_detail.html', {"detail" : content_detail})