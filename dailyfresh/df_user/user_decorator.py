#!/usr/bin/env python
# coding=utf-8
# 登录验证的实现，装饰器

from django.http import HttpResponseRedirect

# 如果未登录转到登录界面
def login(func):
    def login_inner(request,*args,**kwargs):
        # 假如点的是用户中心，request的值：<WSGIRequest: GET '/user_center_info/'>
        if request.session.has_key('user_id'):
            return func(request,*args,**kwargs)
        else:
            red = HttpResponseRedirect('/login/')
            red.set_cookie('url',request.get_full_path())
            return red
    return login_inner
'''
127.0.0.1:8000/10/?type=12
request.path():表示当前路径，为/10/
request.get_full_path()：表示全路径，为：/10/?type=12
'''
