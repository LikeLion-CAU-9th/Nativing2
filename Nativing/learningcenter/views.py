from django.shortcuts import render
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