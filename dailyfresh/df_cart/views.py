from django.shortcuts import render,redirect
from df_user import user_decorator
from .models import CartInfo
from django.http import JsonResponse
from df_goods.models import GoodsInfo

# 购物车，装饰器
@user_decorator.login
def cart(request):
    try:
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
    except Exception as e:
        print("////",e)
        redirect('/')

# 添加
@user_decorator.login
def add(request,gid,count):
    # if request.is_ajax(): # 这个还得研究不然会影响详情页直接购买跳转
    # 直接输入http://127.0.0.1:8000/cart/add1_2则会给购物车id为1的产品数量增加2,
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
    # 和库存进行对比，如果数量大于库存，则购物车数量等于库存
    goods = GoodsInfo.objects.get(id=gid)
    kucun = goods.gkucun
    if len(carts)>=1:
        cart = carts[0]
        cart.count = cart.count + count
    else:
        cart = CartInfo()
        cart.user_id = uid
        cart.goods_id = gid
        cart.count = count
    if cart.count > kucun:
        cart.count = kucun
    cart.save()
    # 如果是ajax请求则返回json,否则转向购物车  测试  正常都不转
    if request.is_ajax():
        count=CartInfo.objects.filter(user_id=uid).count()
        return JsonResponse({'count':count})
    else:
        return redirect('/cart/') # 转到购物车

# @user_decorator.login
def edit(request,gid,count):
    data = {}
    try:
        if request.is_ajax():
            goods = CartInfo.objects.get(id=int(gid))
            goods.count = int(count)
            goods.save()
            data = {'ok':1}
    except Exception as e:
        data = {'ok':int(count)}
    if data=={}:
        return redirect('/')
    else:
        return JsonResponse(data)
def delete(request,gid):
    data = {}
    try:
        if request.is_ajax():
            goods = CartInfo.objects.get(id=int(gid))
            goods.delete()
            data={'ok':1}
    except Exception as e:
        data = {'ok':0,'e':e}
    if data == {}:
        return redirect('/')
    else:
        return JsonResponse(data)
