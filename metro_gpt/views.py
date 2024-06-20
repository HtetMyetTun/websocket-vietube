from django.shortcuts import render
import openai
# Create your views here.
def index(request):
    return render(request,"metro_chat/index.html")
