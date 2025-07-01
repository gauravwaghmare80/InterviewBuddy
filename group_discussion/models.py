from django.db import models
# from django.contrib.auth.models import User
from accounts.models import CustomUser

class DiscussionRoom(models.Model):
    code = models.CharField(max_length=8, unique=True)
    assessor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='assessor_rooms')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

class Participant(models.Model):
    room = models.ForeignKey(DiscussionRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_muted = models.BooleanField(default=False)
