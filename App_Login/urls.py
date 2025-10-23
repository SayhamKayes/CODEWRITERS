from django.urls import path
from App_Login import views


app_name = 'App_Login'

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change-profile/', views.user_change, name='user_change'),
    path('password/', views.pass_change, name='pass_change'),
    path('add-picture/', views.add_profile_pic, name='add_profile_pic'),
    path('change-picture', views.change_profile_pic, name='change_profile_pic'),
]

