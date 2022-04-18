from django.urls import path
from . import views 
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('process_order/', views.process_order, name="process_order"),
    path('list/', login_required(OrderList.as_view()), name="order_list"),
    path('<int:pk>', login_required(OrderDetail.as_view()), name="order_detail"),
]
