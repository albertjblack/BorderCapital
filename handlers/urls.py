from django.urls import path
from bc import views as bc_views
app_name='handlers'
urlpatterns=[
    path('',bc_views.IndexView.as_view(),name='home')
]