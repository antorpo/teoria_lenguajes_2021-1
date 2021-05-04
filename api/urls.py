from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadenaList, name="cadena-list"),
    path('cadena-create/', views.cadenaCreate, name="cadena-create"),
    path('cadena-delete/<str:pk>/', views.cadenaDelete, name="cadena-delete"),
    path('cadena-delete-first/', views.cadenaDeleteFirst, name="cadena-delete-first"),
    path('cadena-delete-all/', views.cadenaDeleteAll, name="cadena-delete-all"),
    path('cadena-last/', views.cadenaLast, name="cadena-last"),
    path('token-array/', views.tokenArray, name="token-array")
]