from . import views
from django.urls import path

app_name='shop'
urlpatterns = [
    path('',views.demo,name='demo'),




]
