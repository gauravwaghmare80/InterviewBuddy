from django.shortcuts import render

# Create your views here.
def aptitude_test(request):
    return render(request, 'aptitude_test.html')