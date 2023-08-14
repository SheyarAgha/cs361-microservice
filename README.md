**Communication Contract:**

*Requesting Data*

To request data from the image_path microservice:

1. Set up a ZeroMQ client instance
2. Send "get_image" formatted as bytes

```
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
socket.send(b"get_image")
```

*Receiving Data*

To receive data requested from the microservice:

1. Set up the ZeroMQ client as shown above
2. Decode the the data received

```
.
.
.
socket.send(b"get_image")
image_path = socket.recv()
image_path = image_path.decode('utf-8')
```

*UML Sequence Diagram*
<img width="306" alt="UML diagram" src="https://github.com/SheyarAgha/cs361-microservice/blob/main/UML.vpd.jpg">
