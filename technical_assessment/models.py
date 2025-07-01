
# Create your models here.
from django.db import models
from accounts.models import CustomUser  # Your custom user model

class AssessmentTopic(models.Model):
    name = models.CharField(max_length=100)  # "Algorithms", "System Design"
    icon = models.CharField(max_length=50)  # For dashboard display

class CodingProblem(models.Model):
    topic = models.ForeignKey(AssessmentTopic, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=20, choices=[
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard')
    ])
    problem_statement = models.TextField()
    solution = models.TextField()

class UserSubmission(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    problem = models.ForeignKey(CodingProblem, on_delete=models.CASCADE)
    code = models.TextField()
    passed = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)