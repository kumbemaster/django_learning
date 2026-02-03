from django.urls import path
from . import views

app_name = 'contact'

# Create your views here.
urlpatterns = [
    path('', views.contact, name='contact'),
]