import bcrypt

good_hash = bcrypt.hashpw(b'goodpassword',bcrypt.gensalt())
bad_hash = bcrypt.hashpw(b'badpassword',bcrypt.gensalt())


print("Good:",good_hash)
print("Bad:",bad_hash)


if (good_hash == bcrypt.hashpw(b'goodpassword',good_hash)):
    print("Password is correct")
else:
    print("Wrong password")

