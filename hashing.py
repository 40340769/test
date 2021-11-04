from Crypto.Hash import SHA256

value_1_1 = SHA256.new(b'Hello Napier').hexdigest()

hello_napier = b'Hello Napier'
value_1_2 = SHA256.new(hello_napier).hexdigest()

value_2 = SHA256.new(b'Hello Starbit').hexdigest()

print("Hello Napier (1st):",value_1_1)
print("Hello Napier (2nd):",value_1_2)
print("Hello Starbit:",value_2)

