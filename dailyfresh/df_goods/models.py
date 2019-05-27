from django.db import models
from DjangoUeditor.models import UEditorField
from .storage import ImageStorage

# index首页商品分类信息
class TypeInfo(models.Model):
    ttitle = models.CharField('分类名称',max_length=20)
    isDelete = models.BooleanField('是否删除', default=False)
    def __str__(self):
        return self.ttitle
    class Meta:
        verbose_name = '分类信息'
        verbose_name_plural = '分类信息'

# 商品信息
class GoodsInfo(models.Model):
    gtitle = models.CharField('商品名称',max_length=35)
    gtype = models.ForeignKey(TypeInfo,verbose_name='所属分类',on_delete=models.CASCADE)
    gprice = models.DecimalField('商品价格',max_digits=7,decimal_places=2)
    gunit = models.CharField('规格',max_length=20, default='500g')     #商品的单位
    gclick = models.IntegerField('点击量')
    isDelete = models.BooleanField('是否删除',default=False)
    gjianjie = models.CharField('简介',max_length=200)     #商品简介
    gkucun = models.IntegerField('库存')
    # gpic = models.ImageField(upload_to='article_img/',verbose_name='商品图片',null=True,blank=True)
    # ImageStorage()图片上传后重命名
    gpic = models.ImageField(upload_to='article_img/%Y%m',storage=ImageStorage(),verbose_name='商品图片',null=True,blank=True)
    gcontent = UEditorField('详细介绍', height=300, width=1000,toolbars='full',imagePath='upimg/',
                               filePath='upfile/',upload_settings={'imageMaxSize':1024000},
                               settings={},command=None,blank=True)
    # gadv = models.BooleanField(default=False)   #商品推荐
    def __str__(self):
        return self.gtitle
    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = '商品信息'
