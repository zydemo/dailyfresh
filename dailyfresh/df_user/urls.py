
from django.urls import path
from df_user import views

urlpatterns = [
    path('register/', views.register),
    path('register_handle/', views.register_handle),
    path('login/', views.login),
    path('login_handle/', views.login_handle),# 登录判断
    path('register_exist/', views.register_exist), # js判断用户名是否存在
    path('user_center_info/', views.user_center_info),
    path('user_center_order/', views.user_center_order),
    path('user_center_site/', views.user_center_site),
    path('logout/', views.logout),

]
