from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request,'project/post/list.html',{'posts':posts})

def post_detail(request,post):
    post = get_object_or_404(Post)
    return render(request,'project/post/detail.html',{'posts':post})