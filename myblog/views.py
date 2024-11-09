from django.http import HttpResponse
from django.shortcuts import render
from myblog.models import Post
# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'myblog/post_list.html',{'posts':posts})