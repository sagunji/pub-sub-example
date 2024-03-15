# Pub-Sub Messaging Example

## Overview

This Pub-Sub messaging example demonstrates a basic publish-subscribe system using Python and Redis. The purpose of this example is to provide a hands-on experience for learning the Pub-Sub architecture, which is a messaging pattern where senders (publishers) broadcast messages without knowing the recipients (subscribers), and recipients receive messages without knowing who the sender is.

## Prerequisites

Before running the example, you must have the following installed:

- Python 3
- Redis server
- Python Redis library (redis-py), which can be installed using pip:

```sh
pip install redis
```

## Running the Example

To run the Pub-Sub example, follow these steps:

1. Start the Redis server on your local machine.
2. Run the subscriber script in one terminal:

```sh
python3 subscriber.py
```

3. Run the publisher script in another terminal:

```sh
python3 publisher.py
```

4. Follow the on-screen prompts to publish and subscribe to messages.

## Theoretical Concepts of Pub-Sub Architecture

The Pub-Sub architecture is a widely used pattern in event-driven systems and services. The key concepts include:

- **Publisher**: Sends messages to a message broker without an awareness of the subscribers.
- **Subscriber**: Receives messages from a message broker based on topic subscriptions without an awareness of the publishers.
- **Topic/Channel**: A conduit where messages are published.
- **Message Broker**: An intermediary that manages the transmission of messages from publishers to subscribers.
- **Decoupling**: Publishers and subscribers are loosely coupled, promoting scalability and maintainability.

## Why Pub-Sub?

Pub-Sub is particularly useful for:

- Distributing messages to multiple consumers.
- Balancing loads between workers.
- Implementing event-driven architectures.
