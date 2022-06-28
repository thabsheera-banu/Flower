from . import views
from django.urls import path

app_name='booking'
urlpatterns = [
    path('',views.booking,name='booking'),
    path('conformed/',views.conform,name='conform')


]
