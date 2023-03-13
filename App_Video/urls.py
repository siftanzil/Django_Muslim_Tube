from django.urls import path
from . import views

app_name = 'App_Blog'

urlpatterns = [
    path('', views.BlogList.as_view(), name='list_video'),

]
