from django.urls import path
from . import views 

app_name="carro"

urlpatterns = [
    path('add/<int:product_id>/', views.add, name="add"),
    path('remove/<int:product_id>/', views.remove, name="remove"),
    path('decrement/<int:product_id>/', views.decrement, name="decrement"),
    path('clear/', views.clear, name='clear'),
]
