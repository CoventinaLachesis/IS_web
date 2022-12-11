from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),
    path('forget',views.forget,name="forget"),
    path('activate/<uidb64>/<token>',views.activate,name="activate"),
    path('setnewpassword/<uidb64>/<token>',views.setnewpassword,name="setnewpassword"),
    
    
]
