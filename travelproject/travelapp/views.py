from django.http import HttpResponse
from django.shortcuts import render
from . models import place,person


# Create your views here.
def app(request):
    obj=place.objects.all()
    obj1=person.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obj1})