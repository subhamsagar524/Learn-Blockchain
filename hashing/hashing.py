# Import the hashing Library
import hashlib

# Get the string as input
word = input("Enter the word for Hashing: ")

# Get the hashing
hashed_code = hashlib.sha256(word.encode())
final = hashed_code.hexdigest()

# Print the result
print("Hashed with 256 bit: ")
print(final)
