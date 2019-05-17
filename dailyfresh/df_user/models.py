from django.db import models

class UserInfo(models.Model):
    # default,blank是python层面的约束，不影响表结构，无需重新迁移
    uname = models.CharField(max_length=20) # 用户名
    upwd = models.CharField(max_length=40) # 密码
    uemail = models.EmailField(max_length=30) # 邮箱地址
    ushou = models.CharField(max_length=20,default='') # 收货人姓名
    uaddress = models.CharField(max_length=200,default='') # 详细地址
    uyoubian = models.CharField(max_length=6,default='') # 邮编
    uphone = models.CharField(max_length=11,default='') # 用户手机
    isDelete = models.BooleanField(default=False) # 是否删除
