from django.urls import path

from myblog import views

urlpatterns =[
    path('', views.post_list, name='post_list')
]