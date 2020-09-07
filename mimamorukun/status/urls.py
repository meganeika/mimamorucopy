from django.urls import path

from . import views

app_name = 'status' 

urlpatterns = [
    path('', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('update/<int:member_pk>', views.upd, name='update'),
]