from django.urls import path
from . import views


app_name = "App_Login"

urlpatterns = [
    path("create_profile/", views.create_profile, name="create_profile"),
    path('login/', views.login_profile, name="login_profile"),
    path('logout/', views.logout_profile, name="logout_profile"),
    path('profile/', views.profile, name="profile"),
    path('change_profile/', views.change_profile, name="change_profile"),
    path('password/', views.change_pass, name="change_pass"),
    path('profile_pic/', views.add_pro_pic, name="add_pro_pic"),
    path('change_pro_pic/', views.change_pro_pic, name='change_pro_pic')
]
