from django.urls import path,re_path
from . import views
# from .views import *

urlpatterns = [
    path('cart/', views.cart,name='cart'),
    re_path(r'add(\d+)_(\d+)/',views.add),# 加入购物车 分别为商品的id和数量
    re_path(r'edit(\d+)_(\d+)/',views.edit),# 修改购物车中商品的数量 分别为商品的id和数量
    re_path(r'delete(\d+)/',views.delete),#删除购物车中的某个商品 为商品的id
    path('place_order/', views.place_order),
]
