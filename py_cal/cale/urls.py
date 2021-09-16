from django.urls import path
from . import views

app_name = 'cale'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:cale_date>/', views.date, name='date'),
    path('<str:cale_day>/', views.day, name='day'),
]
