from django.urls import path
from AppTienda import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('agregar/', views.agregar_producto, name="agregar_producto"),
    path('modificar/<id>', views.modificar_producto, name="modificar_producto"),
]
