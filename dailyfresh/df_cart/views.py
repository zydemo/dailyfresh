from django.shortcuts import render,redirect
from df_user import user_decorator
from .models import CartInfo
from django.http import JsonResponse

# 购物车，装饰器
@user_decorator.login
def cart(request):
    uid = request.session['user_id']
    carts = CartInfo.objects.filter(user_id = uid)
    context = {
        'title':'购物车',
        'page_name': 1,
        'carts':carts,
        # 加个判断值，这个值使cart页面中继承base时不用base里面的刷新购物车功能
        'refresh':1,

    }
    return render(request,'df_cart/cart.html',context)

# 添加
@user_decorator.login
def add(request,gid,count):
    # 获取用户id
    uid = request.session['user_id']
    # 将商品id和数量转换为int
    gid = int(gid)
    count = int(count)
    if gid==0 and request.is_ajax() and count==0:
        # 查询当前登录用户购物车的商品类型数量
        count = CartInfo.objects.filter(user_id=uid).count()
        return JsonResponse({'count':count})
    # 查询购物车中是已有该商品,如果有则数量增加,如果没有则新增一个商品
    carts = CartInfo.objects.filter(user_id=uid,goods_id=gid)
    if len(carts)>=1:
        cart = carts[0]
        cart.count = cart.count + count
    else:
        cart = CartInfo()
        cart.user_id = uid
        cart.goods_id = gid
        cart.count = count
    cart.save()
    # 如果是ajax请求则返回json,否则转向购物车  测试  正常都不转
    if request.is_ajax():
        count=CartInfo.objects.filter(user_id=uid).count()
        return JsonResponse({'count':count})
    else:
        return redirect('/cart/') # 转到购物车

def edit(request,gid,count):
    try:
        if request.is_ajax():
            goods = CartInfo.objects.get(id=int(gid))
            goods.count = int(count)
            goods.save()
            data = {'ok':1}
    except Exception as e:
        data = {'ok':int(count)}
    return JsonResponse(data)
def delete(request,gid):
    try:
        if request.is_ajax():
            goods = CartInfo.objects.get(id=int(gid))
            goods.delete()
            data={'ok':1}
    except Exception as e:
        data = {'ok':0,'e':e}
    return JsonResponse(data)

# 结算
def place_order(request):
    context = {
        'title': '提交订单',
        'page_name': 1,

    }
    return render(request, 'df_cart/place_order.html', context)
