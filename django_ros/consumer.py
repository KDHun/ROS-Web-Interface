import json
from .ros import subscribeToMap
from channels.generic.websocket import WebsocketConsumer

class DataConsumer(WebsocketConsumer):
    def __init__(self):
        print("Initializeing")
        
    def connect(self):
        self.accept()
        subscribeToMap(self)