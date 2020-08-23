from django.urls import path

from . import views

app_name = 'status' 

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:pk>', views.upd, name='update'), 
]