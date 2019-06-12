
from django.urls import path,re_path
from df_user import views

urlpatterns = [
    path('register/', views.register),
    path('register_handle/', views.register_handle),
    path('login/', views.login),
    path('login_handle/', views.login_handle),# 登录判断
    path('register_exist/', views.register_exist), # js判断用户名是否存在
    path('user_center_info/', views.user_center_info),
    path('user_center_order/<int:index>/', views.user_center_order,name='user_center_order'),# 用户中心的全部订单，需要传个页数
    path('user_center_site/', views.user_center_site),
    path('logout/', views.logout),

]
