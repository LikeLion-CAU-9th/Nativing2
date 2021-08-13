from django.shortcuts import render
from content.models import ContentUpload

def index(request):
    return render(request, 'index.html')

def main(request):
    content_list = ContentUpload.objects.select_related("writer")
    content_list_timeorder = content_list.order_by('-datetime').all()
    content_list_random = content_list.order_by('?')[:6]
    context = {
        'content_list': content_list_timeorder,
        'content_list_random': content_list_random
    }
    return render(request, 'main.html', context)