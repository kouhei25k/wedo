import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from chat.models import *
import datetime


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        if 'message' in text_data_json:
            message = text_data_json['message']
            username = text_data_json['username']
            is_todo = text_data_json['is_todo']
            # Send message to room group

            await self.save_message(text_data_json)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'username': username,
                    'is_todo': is_todo
                }
            )
        if 'what' in text_data_json:
            create_user = text_data_json['create_user']
            what = text_data_json['what']
            how_much = text_data_json['how_much']
            by_when = text_data_json['by_when']
            punishment = text_data_json['punishment']
            await self.save_todo(text_data_json)
    # Receive message from room group

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        is_todo = event['is_todo']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'is_todo': is_todo
        }))

    @database_sync_to_async
    def save_message(self, event,):
        message = event['message']
        room_id = self.room_group_name[5:]
        user = self.scope["user"]
        room = Room.objects.get(id=room_id)
        is_todo = event['is_todo']
        Message.objects.create(
            room=room, content=event['message'], user=user, is_todo=is_todo)

    async def chat_todo(self, event):
        create_user = event['create_user']
        what = event['what']
        how_much = event['how_much']
        by_when = event['how_much']
        punishment = event['how_much']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'create_user': create_user,
            'what': what,
            ' how_much':  how_much,
            'by_when': by_when,
            'punishment': punishment,
            'is_todo': is_todo

        }))

    @database_sync_to_async
    def save_todo(self, event,):

        todo = Todo()
        todo.create_user = self.scope["user"]
        todo.what = event['what']
        todo.how_much = event['how_much']
        # todo.by_when = event['how_much']
        todo.by_when = datetime.datetime.now()
        todo.punishment = event['how_much']
        room_id = self.room_group_name[5:]
        todo.room = Room.objects.get(id=room_id)
        todo.save()


class TodoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        create_user = text_data_json['create_user']
        what = text_data_json['what']
        how_much = text_data_json['how_much']
        by_when = text_data_json['how_much']
        punishment = text_data_json['how_much']

        # Send message to room group

        await self.save_todo(text_data_json)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_todo',
                'create_user': create_user,
                'what': what,
                'how_much':  how_much,
                'by_when': by_when,
                'punishment': punishment,
            }
        )

    # Receive message from room group
    async def chat_todo(self, event):
        create_user = event['create_user']
        what = event['what']
        how_much = event['how_much']
        by_when = event['how_much']
        punishment = event['how_much']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'create_user': create_user,
            'what': what,
            ' how_much':  how_much,
            'by_when': by_when,
            'punishment': punishment,

        }))

    @database_sync_to_async
    def save_todo(self, event,):

        todo = Todo()
        todo.create_user = self.scope["user"]
        todo.what = event['what']
        todo.how_much = event['how_much']
        todo.by_when = event['how_much']
        todo.punishment = event['how_much']
        todo.room_id = self.room_group_name[5:]
        todo.room = Room.objects.get(id=room_id)
        todo.save()
    #
