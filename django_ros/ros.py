import rclpy
from rclpy.node import Node
from nav_msgs.msg import OccupancyGrid
import json

class MapConsumer(Node):
    observer_list = []

    def __init__(self):
        rclpy.init()
        super().__init__('map_consumer')
        self.subscription = self.create_subscription(OccupancyGrid, '/map', self.publish, 10)
    def publish(self, data):
        for observer in self.observer_list:
            observer.send(text_data=json.dumps({ 'message': data }))
    
    def addObservable(self, observer):
        self.observer_list.append(observer)
    
    def removeObserver(self, observer):
        self.observer_list.remove(observer)

mapConsumer = MapConsumer()
rclpy.spin(mapConsumer)
def subscribeToMap(observer):
    mapConsumer.addObserver(observer)

def unsubscribe(observer):
    mapConsumer.removeObserver(observer)