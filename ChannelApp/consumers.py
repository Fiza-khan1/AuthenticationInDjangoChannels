from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json

class TokenAuthConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        # Accept the WebSocket connection
        await self.accept()
        
        # Print the username and email of the authenticated user
        user = self.scope.get("user")
        if user.is_authenticated:
            print(f"Username: {user.username}")
            print(f"Email: {user.email}")
        else:
            print("User is not authenticated")

    async def disconnect(self, close_code):
        # Handle the WebSocket disconnection
        print(f"WebSocket disconnected with close code: {close_code}")
        # You can perform additional cleanup if necessary

    async def receive_json(self, content):
        # Handle incoming JSON messages
        command = content.get("command")
        if command == "Say hello !":
            data_string = content.get("data_string", None)
            print(f"Received data_string: {data_string}")
            
            # Send a JSON response back to the client
            await self.send_json({
                "command_response": "The command to say hello was received",
                "data_string_bacK": data_string
            })
        else:
            await self.send_json({
                "error": "Unknown command"
            })
