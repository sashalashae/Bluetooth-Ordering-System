# Group 7: Sanaya Sangvhi, Sasha Morgan, and Shashank Shinde
from bluetooth import *

server_sock = BluetoothSocket(RFCOMM)
server_sock.bind(("", PORT_ANY))
server_sock.listen(1)
# [Checkpoint] Connected to vhost 'ece4564val' on RMQ server at 'localhost' as user 'user'
# [Checkpoint] Setting up exchanges and queues...
# [Checkpoint] Bluetooth ready!
server_sock = BluetoothSocket(RFCOMM)
server_sock.bind(("", PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

advertise_service(
    server_sock,
    "SampleServer",
    service_id=uuid,
    service_classes=[uuid, SERIAL_PORT_CLASS],
    profiles=[SERIAL_PORT_PROFILE])
# [Checkpoint] Waiting for connection on RFCOMM channel 1
# [Checkpoint] Accepted connection from ('B8:27:EB:80:14:26', 1)
# [Checkpoint] Sent menu:
# [Checkpoint] Received order:['item3', 'item3', 'item4', 'item5', 'item1']
# [Checkpoint] Sent receipt: Order ID: 564, Items: ['item3', 'item3', 'item4', 'item1'] Total Price: 12.0, Total Time: 26
# [Checkpoint] Closed Bluetooth Connection.
# [Checkpoint] Waiting for connection on RFCOMM channel 1