from django.shortcuts import render,HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("hello!")
def hello3(request):
    return HttpResponse("hello3")