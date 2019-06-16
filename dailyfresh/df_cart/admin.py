from django.contrib import admin
from .models import *

class CartInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','goods','count']
    # 设置哪些字段可以进入编辑页面
    list_display_links = ('id', 'goods')
    class Meta:
        verbose_name = '购物车商品信息'
        verbose_name_plural = '购物车商品信息'

admin.site.register(CartInfo,CartInfoAdmin)