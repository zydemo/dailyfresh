from django.db import models
from df_goods.models import GoodsInfo
from df_user.models import UserInfo

# 大订单
class OrderInfo(models.Model):
    oid = models.CharField(max_length=20,verbose_name='订单编号')
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE,verbose_name='订单用户')
    odate = models.DateTimeField(auto_now=True,verbose_name='下单时间')
    oIsPay = models.BooleanField(default=False,verbose_name='是否支付')
    # 订单总价单独计算减少数据库频繁交互 不含运费
    ototal = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='总价格')
    oaddress = models.CharField(max_length=300,verbose_name='订单地址')

    class Meta:
        verbose_name='订单信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "用户{0}在{1}的订单".format(self.user.uname,self.odate.strftime("%Y-%m-%d %H:%M:%S"))

# 大订单中的具体某一商品订单，关于支付、物流信息
class OrderDetailInfo(models.Model):
    goods = models.ForeignKey(GoodsInfo,on_delete=models.CASCADE,verbose_name='商品')
    order = models.ForeignKey(OrderInfo,on_delete=models.CASCADE,verbose_name='订单信息')
    price = models.DecimalField(max_digits=7,decimal_places=2,verbose_name='商品价格')
    count = models.IntegerField(verbose_name='购买商品数量')

    class Meta:
        verbose_name = '订单详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}(数量为{1})".format(self.goods.gtitle,self.count)
