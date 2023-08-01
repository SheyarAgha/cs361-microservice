# Example microservice client implementation
# CS361 Summer 2023 Assignment 9
# Sheyar Abdullah

import zmq


# Initialize socket
context = zmq.Context()
print("Connecting to imagepath generator microservice...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
print("Connected successfully!")

# Request random imagepath
print("Sending request")
socket.send(b"get_image")

# Receive reply
image_path = socket.recv()
image_path = image_path.decode('utf-8')
print(f"Path received: {image_path}")
