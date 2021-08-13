from content.models import SocialSaves, ViewHistory
from django.shortcuts import get_object_or_404, render
from content.models import ContentUpload
from accounts.models import User, Follow

# Create your views here.

def learning_center(request):
    contents = Follow.objects.filter(follower_id = request.user.id).select_related('follower')
    following_ids = []
    for followee_iter in contents:
        following_ids.append(followee_iter.followee.id)
    
    following_contents = []
    for followee_id in following_ids:
        content_temp = ContentUpload.objects.filter(writer_id = followee_id).select_related('writer')
        following_contents.append(content_temp)
    
    return render(request,'learning.html', {"contents" : following_contents})


def saved_contents(request):
    saved_contents = SocialSaves.objects.filter(save_user_id = request.user.id)
    return render(request, 'saved_contents.html', {"contents" : saved_contents})


def view_history(request):
    viewed_contents = ViewHistory.objects.filter(view_user_id = request.user.id).order_by("-view_time")
    return render(request, 'view_history.html', {"contents" : viewed_contents})