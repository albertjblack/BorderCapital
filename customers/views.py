from customers import models
from django.views.generic.base import TemplateView
from django.views import generic
from django.urls import reverse_lazy,reverse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms

# Create your views here.
class CustomerCreate(generic.CreateView):
    form_class = forms.CustomerCreateForm
    success_url = reverse_lazy("customers:login")
    template_name = "customers/signup.html"


class CustomerUpdate(generic.UpdateView, LoginRequiredMixin):
    template_name = 'customers/update.html'
    login_url = '/customers/login/'
    redirect_field_name = 'customers/dashboard'
    form_class = forms.CustomerUpdateForm
    model = models.Customer
    def get_success_url(self):
        return reverse('customers:dashboard')


def dashboard(request):
    current_user = request.user
    image_url = current_user.customer.profile_pic.name
    if current_user.is_authenticated:
        return render(request,'customers/dashboard/dashboard.html',{'profile_pic':image_url})
    else:
        return reverse('index') 