from django.db import models

class CartInfo(models.Model):
    # 用户
    user = models.ForeignKey('df_user.UserInfo',on_delete=models.CASCADE)
    # 商品
    goods = models.ForeignKey('df_goods.GoodsInfo',on_delete=models.CASCADE)
    # 购买数量
    count = models.IntegerField(default=0)
    class Meta:
        verbose_name = '购物车商品信息'
        verbose_name_plural = '购物车商品信息'
