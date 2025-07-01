# Register your models here.
from django.contrib import admin
from .models import AssessmentTopic, CodingProblem

@admin.register(AssessmentTopic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')

@admin.register(CodingProblem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'difficulty')
    list_filter = ('topic', 'difficulty')