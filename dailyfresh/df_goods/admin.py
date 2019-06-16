from django.contrib import admin
from .models import *

class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','ttitle']
    # 设置哪些字段可以进入编辑页面
    list_display_links = ('id', 'ttitle')
    search_fields = ['ttitle']

class GoodsInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id','gtitle','gprice','gunit','gclick','gkucun','gtype']
    list_display_links = ('id', 'gtitle','gtype')
    search_fields = ['gtitle', 'gcontent', 'gjianjie']

admin.site.register(TypeInfo,TypeInfoAdmin)
admin.site.register(GoodsInfo,GoodsInfoAdmin)