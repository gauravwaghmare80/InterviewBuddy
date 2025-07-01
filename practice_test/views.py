from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Test, Question, Submission
from django import forms

class AnswerForm(forms.Form):
    answer = forms.ChoiceField(choices=[(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3'), (4, 'Option 4')], widget=forms.RadioSelect)

@login_required
def practice_home(request):
    tests = Test.objects.all()
    completed_tests = Submission.objects.filter(user=request.user).values_list('test_id', flat=True)
    return render(request, 'practice_test/practice_home.html', {
        'tests': tests,
        'completed_tests': completed_tests,
    })

@login_required
def take_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    questions = Question.objects.filter(test=test)

    if request.method == 'POST':
        score = 0
        for question in questions:
            form = AnswerForm(request.POST, prefix=str(question.id))
            if form.is_valid():
                user_answer = int(form.cleaned_data['answer'])
                if user_answer == question.correct_option:
                    score += 1
        
        submission = Submission(user=request.user, test=test, score=score)
        submission.save()
        # Add namespace to the URL name
        return redirect('practice_test:test_result', test_id=test.id, submission_id=submission.id)
    
    forms = {question.id: AnswerForm(prefix=str(question.id)) for question in questions}
    return render(request, 'practice_test/take_test.html', {
        'test': test,
        'questions': questions,
        'forms': forms,
    })

@login_required
def test_result(request, test_id, submission_id):
    test = get_object_or_404(Test, id=test_id)
    submission = get_object_or_404(Submission, id=submission_id, user=request.user)
    return render(request, 'practice_test/test_result.html', {  # Fixed template name from 'take_result.html' to 'test_result.html'
        'test': test,
        'submission': submission,
    })