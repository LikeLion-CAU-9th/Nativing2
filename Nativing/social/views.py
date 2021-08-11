from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render

from accounts.models import User, Follow

import json

# Create your views here.

def social_follow(request):
    if request.method == "POST":
        follow_data = json.loads(request.body.decode('utf-8'))
        uploader_id = follow_data['uploaderId']
        followee = get_object_or_404(User, pk = uploader_id)
        following_or_not = Follow.objects.filter(followee_id = uploader_id, follower_id = request.user.id)
        
        if following_or_not.exists():
            following_or_not.delete()
            print("canceled")
        else: 
            follow_save = Follow(follower = request.user, followee = followee)
            follow_save.save()
            print("saved")
        
        follow_bool = Follow.objects.filter(followee_id = uploader_id, follower_id = request.user.id).exists()
        result = {"is_following" : follow_bool}
    
    return JsonResponse(result, safe = False)
    