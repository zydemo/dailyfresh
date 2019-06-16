from django.db import models

class UserInfo(models.Model):
    # default,blank是python层面的约束，不影响表结构，无需重新迁移
    uname = models.CharField('用户名',max_length=20) # 用户名
    upwd = models.CharField(max_length=40) # 密码
    uemail = models.EmailField('邮箱地址',max_length=30) # 邮箱地址
    ushou = models.CharField('收货人姓名',max_length=20,default='') # 收货人姓名
    uaddress = models.CharField('详细地址',max_length=200,default='') # 详细地址
    uyoubian = models.CharField('邮编',max_length=6,default='') # 邮编
    uphone = models.CharField('手机号',max_length=11,default='') # 用户手机
    isDelete = models.BooleanField('是否删除',default=False) # 是否删除
    def __str__(self):
        return self.uname
    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = "用户信息"
