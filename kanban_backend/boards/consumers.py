import json
from channels.generic.websocket import AsyncWebsocketConsumer

class BoardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.board_id = self.scope['url_route']['kwargs']['board_id']
        self.group_name = f'board_{self.board_id}'

        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    # Receive message from websocket client
    async def receive(self, text_data):
        data = json.loads(text_data)
        # Broadcast message to group
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'board_message',
                'message': data,
            }
        )

    # Receive message from group
    async def board_message(self, event):
        message = event['message']
        # Send message to WebSocket
        await self.send(text_data=json.dumps(message))
