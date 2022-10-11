from django.shortcuts import render,HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("hello!")

def hello2(request):
    return HttpResponse("hello2!")