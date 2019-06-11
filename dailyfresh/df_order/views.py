from django.shortcuts import render
from df_user import user_decorator
from df_cart.models import CartInfo
from df_user.models import UserInfo

# 结算
@user_decorator.login
def order(request):
    uid = request.session['user_id']
    user = UserInfo.objects.get(id=uid)
    # carts = CartInfo.objects.filter(user_id=uid)
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
