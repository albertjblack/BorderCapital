from django.shortcuts import render
from django.views import generic

# Create your views here.
def handler500(request):
    return render(request,'base/handler500.html')

def handler404(request,exception):
    return render(request,'base/handler404.html',context=exception)