from django.urls import path
from . import views

app_name = 'election'

urlpatterns = [
    path('', views.home_view, name='home'),
]

