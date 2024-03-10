from django.shortcuts import render

def home(request):
    return render(request,'home.html',{'title':'learn-django','cname':'django'})
