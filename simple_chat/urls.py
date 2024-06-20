from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("group_chat",views.group_chat,name="group_chat"),
]
