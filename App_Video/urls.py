from django.urls import path
from . import views

app_name = 'App_Video'

urlpatterns = [
    path('', views.VideoList.as_view(), name='video_list'),
    path('category/', views.CategoryList.as_view(), name='category_list'),
    path('upload/', views.UploadVideo.as_view(), name='upload_video'),
    path('play/<slug>', views.play_video, name='play_video'),
    path('liked/<pk>/', views.liked, name='liked_post'),
    path('unliked/<pk>/', views.unliked, name='unliked_post'),
    path('my-videos/', views.MyVideos.as_view(), name='my_videos'),
    path('edit/<pk>/', views.UpdateVideo.as_view(), name='update_video'),
]
