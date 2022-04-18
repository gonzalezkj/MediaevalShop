from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name="Shop"),
    path('boats/', views.boats, name="Boats"),
    path('horses/', views.horses, name="Horses"),
    path('carriages/', views.carriages, name="Carriages"),
    path('swords/', views.swords, name="Swords"),
    path('shields/', views.shields, name="Shields"),
    path('helmets/', views.helmets, name="Helmets"),
]
