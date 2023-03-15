from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import team


def demo(request):
     obj1=place.objects.all()
     obj2=team.objects.all()
     return render(request,'index.html',{'result':obj1,'result1':obj2})
