from django.urls import path
from . import views

app_name = 'technical_assessment'

urlpatterns = [
    path('', views.assessment_home, name='assessment_home'),
    path('problems/<int:problem_id>/', views.problem_detail, name='problem_detail'),
    # Add more URLs
]