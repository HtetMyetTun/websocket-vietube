from django.urls import path,include
from . import views
urlpatterns = [
    path("home/",views.home,name="home"),
    path("menu/",views.menu,name="menu"),
    path("watch/",views.watch,name="watch")
]
