from django.contrib import admin
from .models import *

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['uname','uemail','ushou','uaddress','uyoubian','uphone','isDelete']
    list_display_links = ('uname','uemail','uaddress','uphone')
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'
admin.site.register(UserInfo,UserInfoAdmin)