from django.shortcuts import render
from django.views.generic import CreateView
from django.db.models import Q
from . models import ContentUpload, RELATION_CHOICES
from .forms import ContentUploadForm

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
    return temp


def explore(request):
    content_all = ContentUpload.objects.all()
    keyword_query = request.GET.get('keyword')
    print(request.body)
    print(type(request.body))
    # print("키워드는: ", keyword)
    if keyword_query:
        print("키워드는: ", keyword_query)
        content_all = content_all.filter(
            Q(title__icontains = keyword_query) | 
            Q(expression__icontains = keyword_query) |
            Q(expression_descript__icontains = keyword_query)).order_by('-datetime')
        # return render(request, 'explore.html', {'content_all' : content_all, "keyword" : keyword_query})
    else:
        print("키워드 없")
    
    # a = Content.objects.values()
    relationships  = np.array(RELATION_CHOICES)[:, 0]
    print("프린트 결과: ", relationships,type(relationships))
    # for i in relationships:
    #     print(i[0])

    # jsonObject = json.loads(request.body)
    # print(jsonObject.get)

    # return JsonResponse(jsonObject)

    return render(request, 'test_explore.html', {'content_all' : content_all,
                                             "keyword": keyword_query,
                                             "relationships" : relationships})
                                             







 