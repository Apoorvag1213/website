from turtle import title
from django.http import HttpResponse
from django.shortcuts import render           #it renders html page and does requesting task
 

def  homepage(request):
    return render(request,"index.html",)

def register(request):
    return render(request,"templates/register.html")



