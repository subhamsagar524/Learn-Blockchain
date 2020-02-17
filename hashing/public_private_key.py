# Import the hashing, time Library
import hashlib
import time

# Get the information from the user
name = input("Enter your name: ")   # Get the name
age = input("Enter your age: ")     # Get the age
user_timestamp = time.time()        # Get the timestamp

# Attach all to a string
final = name + age + str(user_timestamp)

# Creating the public key
temp = hashlib.sha256(final.encode())
public_key = temp.hexdigest()

# Creating the private key
temp = hashlib.sha256(public_key.encode())
private_key = temp.hexdigest()

# Display both the keys
print("Your Public Key: ")
print(public_key)
print("Your Private Key: ")
print(private_key)
