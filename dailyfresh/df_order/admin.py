from django.contrib import admin
from .models import *


class OrderInfoAdmin(admin.ModelAdmin):
    list_display = ['oid', 'user','odate','oIsPay','ototal','oaddress']
    # 设置哪些字段可以进入编辑页面
    list_display_links = ('oid', 'user','ototal','oaddress','odate')
    class Meta:
        verbose_name = '订单信息'
        verbose_name_plural = '订单信息'

class OrderDetailInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'goods','order','price','count']
    # 设置哪些字段可以进入编辑页面
    list_display_links = ('id','goods', 'order','price','count')
    class Meta:
        verbose_name = '订单详情'
        verbose_name_plural = '订单详情'


admin.site.register(OrderInfo,OrderInfoAdmin)
admin.site.register(OrderDetailInfo,OrderDetailInfoAdmin)
