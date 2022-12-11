from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('order/<table>',views.order,name="order"),# customer order menu
    path('alltable',views.alltable,name="table"), # chef see what menu customer order
    path('addmenu',views.addmenu,name="add"), # admin add menu to store
]
