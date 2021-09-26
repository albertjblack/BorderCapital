"""bc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views as bc_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',bc_views.IndexView.as_view(),name='index'),
    path('soon/',bc_views.UnderDevView.as_view(),name='under_dev'),
    path('customers/',include('customers.urls',namespace='customers')),
    path('atms/',include('atms.urls',namespace='atms')),
    path('investing/',include('investing.urls',namespace='investing')),
    path('transact/',include('transact.urls',namespace='transact')),
    path('change-password',auth_views.PasswordChangeView.as_view(
        template_name='customers/changepassword.html',
        success_url = 'customers/logout/'
        ),
        name='changepassword'
    ),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='customers/password-reset/password_reset.html',
             subject_template_name='customers/password-reset/password_reset_subject.txt',
             email_template_name='customers/password-reset/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='customers/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='customers/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='customers/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]

handler500 = 'handlers.views.handler500'
handler404 = 'handlers.views.handler404' 
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)