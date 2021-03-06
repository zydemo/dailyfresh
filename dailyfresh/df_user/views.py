from django.shortcuts import render,redirect
from .models import *
from hashlib import sha1
from django.http import JsonResponse,HttpResponseRedirect
from . import user_decorator
from df_order.models import OrderInfo
from df_goods.models import GoodsInfo
# 导入自带的分页插件
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from datetime import timedelta

# https://github.com/shihao1010/tiantianshengxian
# 注册
def register(request):
    context = {
        'title':'注册',
    }
    return render(request,'df_user/register.html',context)

# 注册验证并存入数据库
def register_handle(request):
    if request.method == 'POST':
        # 接收用户输入
        post = request.POST
        uname = post.get('user_name')
        upwd = post.get('pwd')
        upwd2 = post.get('cpwd')
        uemail = post.get('email')
        # 判断两次密码是否一致
        if upwd != upwd2:
            return redirect('/register/')
        # 密码加密
        s1 = sha1()
        # 对s1更新
        s1.update(upwd.encode())
        # 加密处理
        result_upwd = s1.hexdigest()

        # 创建对象
        user = UserInfo()
        user.uname = uname
        user.upwd = result_upwd
        user.uemail = uemail
        user.save()
        # 注册成功后转到登录界面
        return redirect('/login/')
    else:
        return HttpResponseRedirect('/')

# 判断用户是否存在
def register_exist(request):
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})

# 登录
def login(request):
    uname = request.COOKIES.get('uname','') # 获取cookie
    context = {
        'title': '登录',
        'error_name':0,
        'error_pwd':0,
        'uname':uname,
    }
    return render(request,'df_user/login.html',context)

# 登录验证
def login_handle(request):
    if request.method == 'POST':
        post = request.POST
        uname = post.get('username')
        upwd = post.get('pwd')
        jizhu = post.get('jizhu',0) #当jizhu有值时,即jizhu被勾选等于1时,返回的数据为1,否则get返回后面的0
        # 根据用户输入的用户名查询,结果是一个列表
        users = UserInfo.objects.filter(uname=uname)
        # 判断，如果未查到则说明用户名错误，如果查到则去判断密码是否正确，如果正确跳转到登录之前进入的页面，如果没有进入首页
        if len(users) == 1:
            s1=sha1()
            s1.update(upwd.encode())
            if s1.hexdigest() == users[0].upwd:
                url = request.COOKIES.get('url','/') # 获取登录之前的页面，如果没有跳转首页
                red = HttpResponseRedirect(url)
                # 记住用户名，只有登录成功才可以记住
                if jizhu != 0:
                    red.set_cookie('uname',uname)
                else:
                    red.set_cookie('uname','',max_age=-1) # max_age指的是过期时间,当为-1时为立刻过期
                request.session['user_id'] = users[0].id #把用户id和名字放入session中
                request.session['user_name'] = uname
                # 浏览器关闭时过期
                # request.session.set_expiry(0)
                request.session.set_expiry(timedelta(days=2))
                return red
            else:
                context = {
                    'title':'登录',
                    'error_name':0, # 用户名正确
                    'error_pwd':1, # 密码错误
                    'uname':uname,
                    'upwd':upwd
                }
                return render(request,'df_user/login.html',context)
        else:
            context = {
                'title': '登录',
                'error_name': 1,
                'error_pwd': 0,
                'uname': uname,
                'upwd': upwd
            }
            return render(request,'df_user/login.html',context)
    else:
        return HttpResponseRedirect('/')
# 注销
def logout(request):
    # flush()：删除当前的会话数据并删除会话的Cookie
    # request.session.flush()
    # 另一种方法
    del request.session['user_name']
    del request.session['user_id']
    return redirect('/')


# 用户中心，装饰器
@user_decorator.login
def user_center_info(request):
    username = request.session.get('user_name')
    user=UserInfo.objects.filter(uname=username).first()
    goods_list = []

    # 里面存储了最近浏览的五个产品id，session方法,str类型
    # key = str(request.session.get('user_id'))
    # goods_ids2 = request.session.get(key,'')
    # if len(goods_ids2) > 0:
    #     for goods_id in goods_ids2.split(","):
    #         goods_list.append(GoodsInfo.objects.get(id=int(goods_id)))

    # 里面存储了最近浏览的五个产品id，cookie方法
    goods_ids = request.COOKIES.get('goods_ids','')
    if len(goods_ids)>0:
        for goods_id in goods_ids.split(","):
            goods_list.append(GoodsInfo.objects.get(id=int(goods_id)))
    context = {
        'title':'用户中心',
        'page_name':1,
        'user_phone':user.uphone,
        'user_address':user.uaddress,
        'user_name':username,
        'user_email':user.uemail,
        'goods_list':goods_list,
    }
    return render(request,'df_user/user_center_info.html',context)

# 用户订单，装饰器
@user_decorator.login
def user_center_order(request,index): # 需要传入页数
    try:
        user_id = request.session['user_id']
        # 下单时间倒序排序
        order_list = OrderInfo.objects.filter(user_id=int(user_id)).order_by('-odate')
        paginator = Paginator(order_list,2) # 每页两条数据
        try:
            page = paginator.page(int(index))  # 获取当前页码的记录:<Page 1 of 2>
        except PageNotAnInteger:
            page = paginator.page(1)  # 如果用户输入的页码不是整数，显示第一页内容
        except EmptyPage:
            # paginator.num_pages 总页数
            page = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时，显示最后一页
        context = {
            'title': '用户中心',
            'page_name': 1,
            'page':page,
            'paginator':paginator,
            'order_list':order_list
        }
        return render(request,'df_user/user_center_order.html',context)
    except:
        return redirect('/user_center_order/1/')

# 收货地址，装饰器
@user_decorator.login
def user_center_site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        post = request.POST
        user.ushou = post.get('ushou')
        user.uyoubian = post.get('uyoubian')
        user.uphone = post.get('uphone')
        user.uaddress = post.get('uaddress')
        user.save()
    context = {
        'title': '用户中心',
        'page_name': 1,
        'user':user,
    }
    return render(request,'df_user/user_center_site.html',context)