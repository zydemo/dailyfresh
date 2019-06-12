from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.order,name='order'),
    path('order_handle/',views.order_handle,name='order_handle'),
]
