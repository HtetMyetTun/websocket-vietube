from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"simple_chat/index.html")

def group_chat(request):
    return render(request,"simple_chat/group_chat.html")