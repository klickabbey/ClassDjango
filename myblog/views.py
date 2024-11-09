from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.
def post_list(request):
    from blog.models import Post
def post_list(request):
    posts = Post.objects.all()
    return HttpResponse(f"List of posts: {'posts':posts} ")