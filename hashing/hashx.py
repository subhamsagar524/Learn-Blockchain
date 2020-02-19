# Import the hashing Library
import hashlib

# Display all the available algorithm
print("There are several algorithm for hashing...")
print("Here you can use these algorithm choose yours:")
store_algo = hashlib.algorithms_guaranteed
store_algo
ch = input("Choose by entering 1, 2, ...etc: ")

# Get the string as input
word = input("Enter the word for Hashing: ")

# Get the hashing and Print the result
if (ch == 1):
    hashed_code = hashlib.sha256(word.encode())
    final = hashed_code.hexdigest()
elif (ch == 2):
    hashed_code = hashlib.sha512(word.encode())
    final = hashed_code.hexdigest()
elif (ch == 3):
    hashed_code = hashlib.sha384(word.encode())
    final = hashed_code.hexdigest()
elif (ch == 4):
    hashed_code = hashlib.sha1(word.encode())
    final = hashed_code.hexdigest()
elif (ch == 5):
    hashed_code = hashlib.md5(word.encode())
    final = hashed_code.hexdigest()
elif (ch == 6):
    hashed_code = hashlib.sha224(word.encode())
    final = hashed_code.hexdigest()
