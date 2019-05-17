from django.shortcuts import render,redirect
from .models import *
from hashlib import sha1
from django.http import JsonResponse,HttpResponseRedirect

# https://github.com/shihao1010/tiantianshengxian
# 注册
def register(request):
    context = {
        'title':'天天生鲜-注册',
    }
    return render(request,'df_user/register.html',context)

# 注册验证并存入数据库
def register_handle(request):
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

# 判断用户是否存在
def register_exist(request):
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})

# 登录
def login(request):
    uname = request.COOKIES.get('uname','') # 获取cookie
    context = {
        'title': '天天生鲜-登录',
        'error_name':0,
        'error_pwd':0,
        'uname':uname,
    }
    return render(request,'df_user/login.html',context)

# 登录验证
def login_handle(request):
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
            return red
        else:
            context = {
                'title':'天天生鲜-登录',
                'error_name':0, # 用户名正确
                'error_pwd':1, # 密码错误
                'uname':uname,
                'upwd':upwd
            }
            return render(request,'df_user/login.html',context)
    else:
        context = {
            'title': '天天生鲜-登录',
            'error_name': 1,
            'error_pwd': 0,
            'uname': uname,
            'upwd': upwd
        }
        return render(request,'df_user/login.html',context)

# 主页
def index(request):
    return render(request,'index.html')