from django.contrib import admin
from django.urls import path,re_path,include
from df_user import views
# 导入静态文件模块
from django.views.static import serve
# 导入配置文件里上传文件配置
from django.conf import settings

# https://github.com/sweetdoctor/dailyfresh
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('df_goods.urls')),
    path('',include('df_user.urls')),
    path('',include('df_cart.urls')),
    path('',include('df_order.urls')),
    path('ueditor/',include('DjangoUeditor.urls')),
    re_path('^static/media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]
