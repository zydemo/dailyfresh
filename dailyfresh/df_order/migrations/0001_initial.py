# Generated by Django 2.1.1 on 2019-06-11 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('df_goods', '0002_auto_20190605_1322'),
        ('df_user', '0002_auto_20190526_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetailInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='商品价格')),
                ('count', models.IntegerField(verbose_name='商品数量')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_goods.GoodsInfo', verbose_name='商品')),
            ],
            options={
                'verbose_name': '订单详情',
                'verbose_name_plural': '订单详情',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oid', models.CharField(max_length=20, verbose_name='订单编号')),
                ('odate', models.DateTimeField(auto_now=True, verbose_name='下单时间')),
                ('oIsPay', models.BooleanField(default=False, verbose_name='是否支付')),
                ('ototal', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='总价格')),
                ('oaddress', models.CharField(max_length=300, verbose_name='订单地址')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_user.UserInfo', verbose_name='订单用户')),
            ],
            options={
                'verbose_name': '订单信息',
                'verbose_name_plural': '订单信息',
            },
        ),
        migrations.AddField(
            model_name='orderdetailinfo',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_order.OrderInfo', verbose_name='订单信息'),
        ),
    ]
