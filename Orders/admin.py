from django.contrib import admin

from Orders.models import OrderLine
from .models import OrderLine, Order
# Register your models here.

admin.site.register([Order, OrderLine])