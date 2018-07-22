from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

class DroneConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = "drone_group"

        # Join drone group
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        # Send message to drone group
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'drone_message',
                'message': text_data_json
            }
        )

    # Receive message from drone group
    def drone_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
