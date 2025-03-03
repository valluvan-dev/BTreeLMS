from django.urls import path
from .views import *

urlpatterns = [
    path('',Home,name="home"),
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('admin_dashboard/',admin_dashboard,name='admin_dashboard'),
    path('student_dashboard/',student_dashboard,name='student_dashboard'),
    path('trainer_dashboard/',trainer_dashboard,name='trainer_dashboard'),
    path('staff_dashboard/',staff_dashboard,name='staff_dashboard'),
    path('no_permission/', no_permission, name='no_permission'),
    path('unauthorized_page/',unauthorized_page,name='unauthorized_page'),
    path('users/', user_list, name='user_list'),  
    path('users/<int:user_id>/', user_detail, name='user_detail'), 
]

