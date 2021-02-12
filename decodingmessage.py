## decription of encoded file

import base64

base64_message = 'VGhlIHdhZ2VzIG9mIHNpbiBpcyBkZWF0aA=='
base64_byte = base64_message.encode('ascii')
message_byte=base64.b64decode(base64_byte)
message = message_byte.decode('ascii')


print(message)
