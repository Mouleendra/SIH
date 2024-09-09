from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.RegisterPage,name="registerpage"),
    path("register/",views.UserRegister,name="register"),
    path("login/",views.login,name="login"),
    path("logins/",views.loginuser,name="logins"),
    path("home/", views.home, name="home"),
    path("map/",views.map,name="map"),
]