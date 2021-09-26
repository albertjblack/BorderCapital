from django.contrib import auth
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'customers'
urlpatterns=[
    path('login/', auth_views.LoginView.as_view(template_name='customers/login.html'), name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', views.CustomerCreate.as_view(), name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('update/<pk>', views.CustomerUpdate.as_view(), name='update'),
] 