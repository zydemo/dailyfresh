from django.db import models

class UserInfo(models.Model):
    uname = models.CharField(max_length=20) # 用户名
    upwd = models.CharField(max_length=40) # 密码
    uemail = models.EmailField(max_length=30) # 邮箱地址
    ushou = models.CharField(max_length=20) # 收货人姓名
    uaddress = models.CharField(max_length=200) # 详细地址
    uyoubian = models.CharField(max_length=6) # 邮编
    uphone = models.CharField(max_length=11) # 用户手机
    isDelete = models.BooleanField(default=False) # 是否删除
