from django.urls import path
from bc import views as bc_views
app_name='atms'
urlpatterns=[
    path('',bc_views.IndexView.as_view(),name='home'),
    path('locate/',bc_views.IndexView.as_view(),name='locate'),
]