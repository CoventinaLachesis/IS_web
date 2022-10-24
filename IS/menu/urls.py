from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('order/<table>',views.order,name="home"),
    path('alltable',views.alltable,name="home"),
]
