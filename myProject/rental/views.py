from django.shortcuts import render
from django.http import HttpResponse

def member(request):
    return render(request,"hi.html")

def staff(request):
    return render(request,"staff.html")