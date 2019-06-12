from django.shortcuts import render,HttpResponse
from df_user import user_decorator
from df_cart.models import CartInfo
from df_user.models import UserInfo
from django.db import transaction
from .models import *
from datetime import datetime
from decimal import Decimal
from django.http import JsonResponse

# 结算
@user_decorator.login
def order(request):
    uid = request.session['user_id']
    user = UserInfo.objects.get(id=uid)
    # 获取所有结算的购物车id，列表
    cart_ids = request.GET.getlist('cart_id')
    carts = []
    total_price = 0
    for cart_id in cart_ids:
        cart = CartInfo.objects.get(id=cart_id)
        carts.append(cart)
        total_price = total_price + float(cart.count)*float(cart.goods.gprice)
    total_price = float('%0.2f' %total_price)
    # 运费
    trans_cost = 10
    total_trans_price = trans_cost + total_price
    context = {
        'title': '提交订单',
        'page_name': 1,
        'carts':carts,
        'user':user,
        'total_price':float('%0.2f' %total_price),# 总金额不含运费
        'trans_cost':trans_cost,
        'total_trans_price':total_trans_price,# 总金额含运费
    }
    return render(request, 'df_order/order.html', context)
'''
事务提交：
这些步骤中，任何一环节一旦出错则全部退回1
1. 创建订单对象
2. 判断商品库存是否充足
3. 创建 订单 详情 ，多个
4，修改商品库存
5. 删除购物车
'''
@user_decorator.login
@transaction.atomic() # 事务装饰器
def order_handle(request):
    # 保存事务发生点
    tran_id = transaction.savepoint()
    # 用户提交的订单购物车，此时cart_ids为字符串，例如'1,2,3'
    cart_ids = request.POST.get('cart_ids')
    # 获取当前用户的id,int类型
    user_id = request.session['user_id']
    data = {}
    try:
        # 创建一个订单对象
        order_info = OrderInfo()
        now = datetime.now()
        # 订单编号为订单提交时间和用户id组合
        order_info.oid = '%s%d'%(now.strftime('%Y%m%d%H%M%S'),int(user_id))
        # 订单时间
        order_info.odate = now
        # 订单的用户id
        order_info.user_id = int(user_id)
        # 从前端获取订单总价,total是前端页面总金额的id
        order_info.ototal = Decimal(request.POST.get('total'))
        order_info.save()
        # 对用户提交订单中的每类商品即每一个小购物车进行遍历
        for cart_id in cart_ids.split(","):
            # 从CartInfo表中获取小购物车对象
            cart = CartInfo.objects.get(pk=cart_id)
            # 大订单中的每一个小商品订单
            order_detail = OrderDetailInfo()
            # 外键关联，小订单和大订单进行关联
            order_detail.order = order_info
            # 具体商品
            goods = cart.goods
            # 判断库存
            if cart.count <= goods.gkucun:
                goods.gkucun = goods.gkucun - cart.count
                goods.save()
                order_detail.goods = goods
                order_detail.price = goods.gprice
                order_detail.count = cart.count
                order_detail.save()
                # 提交成功并删除当前的购物车
                cart.delete()
            else:
                # 事务回滚，取消订单
                transaction.savepoint_rollback(tran_id)
                return HttpResponse("库存不足，提交订单失败")
        data['ok'] = 1
        transaction.savepoint_commit(tran_id)
    except Exception as e:
        # 任何一个环节出错，事务全部取消
        transaction.savepoint_rollback(tran_id)
        return HttpResponse("未完成订单提交，原因为：",e)
    return JsonResponse(data)

# 支付不能做
@user_decorator.login
def pay(request):
    return HttpResponse("支付成功啦！")

