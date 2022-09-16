from django.urls import path, include
from . import views

app_name = 'newsletter'

urlpatterns = [
    path('', views.newsletter, name='newsletter')
]