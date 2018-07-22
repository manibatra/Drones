from channels.generic.websocket import AsyncWebsocketConsumer
import json

class DroneConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "drone_group"

        # Join drone group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave drone group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        # Send message to dashboard group
        await self.channel_layer.group_send(
            "dashboard_group",
            {
                'type': 'drone_message',
                'message': text_data_json
            }
        )


class DashboardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "dashboard_group"

        # Join dashboard group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave dashboard group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    # Receive message from drone group
    async def drone_message(self, event):
        message = event['message']
        identity = message['id']
        latitude = message['lat']
        longitude = message['long']
        speed = message['speed']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'id': identity,
            'latitude': latitude,
            'longitude': longitude,
            'speed': speed
        }))
