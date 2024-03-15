import redis
from time import sleep

def message_handler(message):
  print(f"Received on {message['channel'].decode()}: {message['data'].decode()}")

def subscribe_to_channels(pubsub, channels):
  pubsub.subscribe(**{channel: message_handler for channel in channels})
  print(f"Subscribed to {channels}. Waiting for messages...")
  pubsub.run_in_thread(sleep_time=0.001)

channels = ['general', 'random', 'engineering']

try:
  r = redis.Redis()
  pubsub = r.pubsub()
  subscribe_to_channels(pubsub, channels)
except redis.ConnectionError:
  print("Connection failed, retrying in 5 seconds...")
  sleep(5)
