from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

# 主页
def index(request):
    # 首先获得外键指向的表中对象，然后通过‘_set’这样的方法获得目标表中的数据
    typelist = TypeInfo.objects.all()
    # 按照id降序排序，取出前四个
    type0 = typelist[0].goodsinfo_set.order_by('-id')[0:4]
    type01 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]
    type1 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    type11 = typelist[1].goodsinfo_set.order_by('-gclick')[0:4]
    type2 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    type21 = typelist[2].goodsinfo_set.order_by('-gclick')[0:4]
    type3 = typelist[3].goodsinfo_set.order_by('-id')[0:4]
    type31 = typelist[3].goodsinfo_set.order_by('-gclick')[0:4]
    type4 = typelist[4].goodsinfo_set.order_by('-id')[0:4]
    type41 = typelist[4].goodsinfo_set.order_by('-gclick')[0:4]
    type5 = typelist[5].goodsinfo_set.order_by('-id')[0:4]
    type51 = typelist[5].goodsinfo_set.order_by('-gclick')[0:4]

    context = {
        'title':'首页','guest_cart':1,
        'type0': type0, 'type01': type01,
        'type1': type1, 'type11': type11,
        'type2': type2, 'type21': type21,
        'type3': type3, 'type31': type31,
        'type4': type4, 'type41': type41,
        'type5': type5, 'type51': type51,
    }
    return render(request,'index.html',context)
# 详情页
def detail(request,sid):
    # 通过id查询指定的产品
    goods = GoodsInfo.objects.get(id=int(sid))
    # 点击量
    goods.gclick = goods.gclick + 1
    goods.save()
    # 获取当前分类下的新品推荐
    news = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
    # 如果产品标题太长，截取20位
    if len(goods.gtitle) >= 20:
        title = goods.gtitle[0:20]+"..."
    else:
        title = goods.gtitle
    context = {
        # title呈现为：分类名-产品标题
        'title': goods.gtype.ttitle + "-" + title,
        'goods':goods,
        'news':news,
        'sid':sid,
        'guest_cart': 1
    }
    response =  render(request,'df_goods/detail.html',context)
    # 记录最近浏览,在用户中心使用
    if request.session.has_key('user_id'): # 判断是否登录
        key = str(request.session.get('user_id'))
        goods_ids = request.session.get(key,'')
        print("***",goods_ids,key)
        goods_id = str(goods.id)
        # 判断是否有浏览记录，也就是看过产品
        if goods_ids != '':
            # 如果已经存在则删除掉
            if goods_ids.count(goods_id) >= 1:
                goods_ids.remove(goods_id)
            # 添加到第一个
            goods_ids.insert(0, goods_id)
            # 如果超过6个则删除最后一个
            if len(goods_ids) >= 6:
                del goods_ids[5]
        else:
            goods_ids = []
            goods_ids.append(goods_id)
        request.session[key] = goods_ids
    return response

# 列表页
def list(request,tid,pindex,sort): # 类型id,页码,排序规则（人气、价格、默认）
    typeinfo = TypeInfo.objects.get(id=int(tid))
    # 获取当前分类下的新品推荐
    news = typeinfo.goodsinfo_set.order_by('-id')[0:2]
    if sort == '1':#默认，最新
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')
    elif sort == '2': # 价格排序
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gprice')
    elif sort == '3': # 点击量
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gclick')
    paginator = Paginator(goods_list,10)
    page = paginator.page(int(pindex))
    context = {
        'title':typeinfo.ttitle + '商品列表',
        'page':page,
        'news':news,
        'sort':sort,
        'typeinfo':typeinfo,
        'paginator':paginator,
        'goods_list':goods_list,
        'guest_cart':1
    }
    return render(request,'df_goods/list.html',context)

