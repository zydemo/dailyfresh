from django.urls import path,re_path
from . import views
# from .views import *

urlpatterns = [
    path('order/', views.order,name='order'),
]
