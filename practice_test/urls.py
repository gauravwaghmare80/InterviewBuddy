# practice_test/urls.py
from django.urls import path
from . import views

app_name = 'practice_test'  # This is the namespace

urlpatterns = [
    path('', views.practice_home, name='practice_home'),  # This is the name you reference
    path('take/<int:test_id>/', views.take_test, name='take_test'),
    path('result/<int:test_id>/<int:submission_id>/', views.test_result, name='test_result'),
]