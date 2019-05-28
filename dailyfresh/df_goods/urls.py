from django.urls import path,re_path
from . import views
# from .views import *

urlpatterns = [
    path('', views.index,name='index'),
    path('itemId=<int:sid>', views.detail),
    re_path('list(\d+)_(\d+)_(\d+)/',views.list,name='list'),# 列表页
]
