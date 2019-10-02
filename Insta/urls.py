from django.contrib import admin
from django.urls import path, include

from Insta.views import PostView, PostDetail, PostCreateView, PostUpdateView,PostDeleteView


urlpatterns = [
    path('', PostView.as_view(), name ='home'),
    path('post/<int:pk>/', PostDetail.as_view(), name= 'post_detail'),
    path('make_post/', PostCreateView.as_view(), name='make_post'),
    path('update_post/<int:pk>/', PostUpdateView.as_view(), name='update_post'),
    path('delete_post/<int:pk>/', PostDeleteView.as_view(), name='delete_post'),
]