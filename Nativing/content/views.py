from django.shortcuts import render, redirect


# Create your views here.
def content(request):
    return render(request, 'content.html')


def contentDetail(request):
    return render(request, 'contentDetail.html')


def explore(request):
    return render(request, 'explore.html')


def learningCenter(request):
    return render(request, 'learningCenter')

