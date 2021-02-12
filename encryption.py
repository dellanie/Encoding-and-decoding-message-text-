import base64

message =  ("The wages of sin is death")
message_bytes = message.encode('ascii')
base64_bytes=base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

print("Encoded message is" + base64_message)


