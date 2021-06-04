import json

from channels.generic.websocket import AsyncWebsocketConsumer


class OrdersConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        stream_id = self.scope['url_route']['kwargs']['pk']

        self.user = self.scope["user"]

        if not self.user.is_authenticated:
            await self.close()

        self.room_name = f"stream{stream_id}"
        self.room_group_name = f"updates_{self.room_name}"

        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )

        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        pass

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    async def send_notification(self, event):
        data = json.loads(event.get('value'))
        await self.send(text_data=json.dumps({'payload': data}))
