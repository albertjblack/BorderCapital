from django.shortcuts import render
from django.views import generic

# Create your views here.
def handler500(request, *args, **kwargs):
    return render(request,'handlers/500.html')

def handler404(request, *args, **kwargs):
    return render(request,'handlers/404.html')