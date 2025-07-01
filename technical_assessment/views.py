# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import AssessmentTopic, CodingProblem

@login_required
def assessment_home(request):
    topics = AssessmentTopic.objects.all()
    return render(request, 'technical_assessment/home.html', {'topics': topics})

@login_required
def problem_detail(request, problem_id):
    problem = get_object_or_404(CodingProblem, id=problem_id)
    return render(request, 'technical_assessment/problem.html', {'problem': problem})

# Add more views for code submission, evaluation, etc.