import json
from channels.generic.websocket import WebsocketConsumer
from gpt4all import GPT4All
model = GPT4All('orca-mini-3b-gguf2-q4_0.gguf')

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print("socket is connected")
        self.accept()
    
    def disconnect(self, close_code):
        pass
    
    def receive(self, text_data=None, bytes_data=None):
        text_data_json=json.loads(text_data)
        self.send(text_data=json.dumps({"message":model.generate(text_data_json["message"],max_tokens=100)}))
        