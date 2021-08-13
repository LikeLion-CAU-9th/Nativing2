from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render

from accounts.models import User, Follow
from content.models import ContentUpload, SocialSaves, SocialLikes

import json

# Create your views here.

def social_save(request):
    if request.method == 'POST':
        post_data = json.loads(request.body.decode("utf-8"))
        content_id = post_data['content_id']
        content = get_object_or_404(ContentUpload, pk = content_id)

        if content.saves.filter(id = request.user.id).exists():
            content.saves.remove(request.user)
            content.save()
        else: 
            content_save = SocialSaves(save_user = request.user, save_content = content)
            content_save.save() 

        content_user_both = SocialSaves.objects.filter(save_content_id = content_id, save_user_id = request.user.id).values()
        content_saved = SocialSaves.objects.filter(save_content_id = content_id).values()
        is_saved = content_user_both.exists()
        
        result = { "is_saved" : is_saved }

    return JsonResponse(result, safe=False)


def social_likes(request):
    if request.method == "POST":
        like_data = json.loads(request.body.decode('utf-8'))
        content_id = like_data['content_like_id']
        content = get_object_or_404(ContentUpload, pk = content_id)
        
        if content.likes.filter(id = request.user.id).exists():
            content.likes.remove(request.user)
            content.save()
        else:
            content_like = SocialLikes(like_user = request.user, like_content = content)
            content_like.save()
        
        is_liked = SocialLikes.objects.filter(like_content_id = content_id, like_user_id = request.user.id).exists()
        likes_count = SocialLikes.objects.filter(like_content_id = content_id).count()

        result = {
            "is_liked" : is_liked,
            "likes_count" : likes_count,
        }
        
    return JsonResponse(result, safe= False)


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
        
        uploader_followers = Follow.objects.filter(followee_id = uploader_id).count()
        is_follower_plural = (uploader_followers > 1)
        follow_bool = Follow.objects.filter(followee_id = uploader_id, follower_id = request.user.id).exists()
        result = {
            "is_following" : follow_bool,
            "follower_num" : uploader_followers,
            "is_plural" : is_follower_plural,
        }
        print(is_follower_plural)
    
    return JsonResponse(result, safe = False)
    

    

