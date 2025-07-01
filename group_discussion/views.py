# gd/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import DiscussionRoom, Participant
import uuid

@login_required
def create_room(request):
    if request.method == 'POST':
        room = DiscussionRoom.objects.create(
            code=str(uuid.uuid4())[:8],
            assessor=request.user
        )
        Participant.objects.create(room=room, user=request.user)
        return redirect('group_discussion:room_detail', room_code=room.code)
    return render(request, 'gd/create_room.html')

@login_required
def join_room(request, room_code):
    try:
        room = DiscussionRoom.objects.get(code=room_code, is_active=True)
        if request.user != room.assessor:
            Participant.objects.get_or_create(room=room, user=request.user)
        is_assessor = request.user == room.assessor
        return render(request, 'gd/room.html', {
            'room': room,
            'is_assessor': is_assessor
        })
    except DiscussionRoom.DoesNotExist:
        return render(request, 'gd/error.html', {'message': 'Room not found or inactive'})

@login_required
def room_detail(request, room_code):
    room = DiscussionRoom.objects.get(code=room_code, assessor=request.user)
    participants = room.participant_set.all()
    return render(request, 'gd/room_detail.html', {'room': room, 'participants': participants})

def gd_lobby(request):
    return render(request, 'group_discussion/gd_lobby.html')
