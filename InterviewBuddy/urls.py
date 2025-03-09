from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_dashboard.urls')),
    path('accounts/', include('accounts.urls')),
    path('practice_test/', include('practice_test.urls')),
]
