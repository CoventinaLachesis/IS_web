from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('order/<table>',views.order,name="home"),# customer order menu
    path('alltable',views.alltable,name="table"), # chef see what menu customer order
    path('addmenu',views.addmenu,name="add"), # admin add menu to store
]
