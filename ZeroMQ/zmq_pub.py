import zmq

from time import sleep

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://127.0.0.1:2000')

messages = [100,200,300]
i = 0

while True:
    sleep(1)
    socket.send_pyobj({i:messages[i]})
    i = 0 if i == 2 else i + 1
