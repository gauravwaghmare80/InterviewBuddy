from django.urls import path
from .views import *
urlpatterns = [
    path('aptitude_test/', aptitude_test, name='aptitude_test'),
    
]
