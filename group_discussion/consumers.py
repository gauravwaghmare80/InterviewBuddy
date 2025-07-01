# gd_app/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from .models import DiscussionRoom, Participant

class VideoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_code = self.scope['url_route']['kwargs']['room_code']
        self.room_group_name = f'video_{self.room_code}'
        self.user = self.scope['user']

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

        # Notify others of new participant
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_joined',
                'username': self.user.username
            }
        )

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_left',
                'username': self.user.username
            }
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_type = data['type']
        user = self.user.username
        is_assessor = data.get('is_assessor', False)

        if is_assessor:
            if message_type == 'end_session':
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'end_session',
                        'message': 'Session ended by assessor'
                    }
                )
                room = DiscussionRoom.objects.get(code=self.room_code)
                room.is_active = False
                room.save()
            elif message_type == 'mute':
                username = data['username']
                participant = Participant.objects.get(room__code=self.room_code, user__username=username)
                participant.is_muted = True
                participant.save()
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'mute_user',
                        'username': username
                    }
                )
        else:
            participant = Participant.objects.get(room__code=self.room_code, user__username=user)
            if not participant.is_muted:
                if message_type == 'offer':
                    await self.channel_layer.group_send(
                        self.room_group_name,
                        {
                            'type': 'offer',
                            'offer': data['offer'],
                            'from': user
                        }
                    )
                elif message_type == 'answer':
                    await self.channel_layer.group_send(
                        self.room_group_name,
                        {
                            'type': 'answer',
                            'answer': data['answer'],
                            'from': user,
                            'to': data['to']
                        }
                    )
                elif message_type == 'ice-candidate':
                    await self.channel_layer.group_send(
                        self.room_group_name,
                        {
                            'type': 'ice_candidate',
                            'candidate': data['candidate'],
                            'from': user,
                            'to': data['to']
                        }
                    )

    async def user_joined(self, event):
        await self.send(text_data=json.dumps({
            'type': 'user_joined',
            'username': event['username']
        }))

    async def user_left(self, event):
        await self.send(text_data=json.dumps({
            'type': 'user_left',
            'username': event['username']
        }))

    async def offer(self, event):
        await self.send(text_data=json.dumps({
            'type': 'offer',
            'offer': event['offer'],
            'from': event['from']
        }))

    async def answer(self, event):
        if event['to'] == self.user.username:
            await self.send(text_data=json.dumps({
                'type': 'answer',
                'answer': event['answer'],
                'from': event['from']
            }))

    async def ice_candidate(self, event):
        if event['to'] == self.user.username:
            await self.send(text_data=json.dumps({
                'type': 'ice-candidate',
                'candidate': event['candidate'],
                'from': event['from']
            }))

    async def mute_user(self, event):
        await self.send(text_data=json.dumps({
            'type': 'mute',
            'username': event['username']
        }))

    async def end_session(self, event):
        await self.send(text_data=json.dumps({
            'type': 'end',
            'message': event['message']
        }))