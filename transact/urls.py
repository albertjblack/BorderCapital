from django.urls import path
from bc import views as bc_views
from customers import views as customers_views

app_name = 'transact'

urlpatterns=[
    path('info/',bc_views.IndexView.as_view(),name='info')
]