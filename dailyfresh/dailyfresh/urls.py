"""dailyfresh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from df_user import views
# 导入静态文件模块
from django.views.static import serve
# 导入配置文件里上传文件配置
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register),
    path('register_handle/', views.register_handle),
    path('login/', views.login),
    path('login_handle/', views.login_handle),# 登录判断
    path('register_exist/', views.register_exist), # js判断用户名是否存在
    path('', views.index,name='index'),
    path('user_center_info/', views.user_center_info),
    path('user_center_order/', views.user_center_order),
    path('user_center_site/', views.user_center_site),
    path('logout/', views.logout),
    path('cart/', views.cart),
    path('ueditor/',include('DjangoUeditor.urls')),
    re_path('^static/media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]
