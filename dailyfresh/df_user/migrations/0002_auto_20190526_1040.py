# Generated by Django 2.1.1 on 2019-05-26 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='uaddress',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uphone',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='ushou',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uyoubian',
            field=models.CharField(default='', max_length=6),
        ),
    ]
