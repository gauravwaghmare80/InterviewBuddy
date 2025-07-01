from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home(request):
    return redirect('dashboard')  # Redirects to /dashboard/

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('user_dashboard.urls')),
    path('accounts/', include('accounts.urls')),
    path('practice_test/', include('practice_test.urls')),
    path('', home, name='home'),  # Root URL
    path('assessment/', include('technical_assessment.urls')),
    path('gd/', include('group_discussion.urls')),

]