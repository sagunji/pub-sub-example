import redis

def choose_channel(channels):
  for idx, channel in enumerate(channels):
    print(f"{idx + 1}. {channel}")
  try:
    choice = int(input("Select channel number: "))
    if 1 <= choice <= len(channels):
      return channels[choice - 1]
    else:
      print("Inavalid choice. Please choose a valid channel number.")
  except ValueError:
    print("Please enter a number.")
  

def send_message(r, channel):
  while True:
    message = input(f"Enter a message to send on {channel} (or type 'exit' to quit): ")
    if message.lower() == 'exit':
      exit(0)
    r.publish(channel, message)
    continue_prompt = input("Continue in this channel? (y/n): ").lower()
    if continue_prompt == 'n':
      return

channels = ['general', 'random', 'engineering']

r = redis.Redis()

current_channel = choose_channel(channels)

while True:
  send_message(r, current_channel)
  switch = input("Switch channel? (y/n): ").lower()

  if switch == 'y':
    current_channel = choose_channel(channels)
  elif switch == 'n':
    continue
  elif switch.lower() == 'exit':
    break

print("Publisher exited..")
  