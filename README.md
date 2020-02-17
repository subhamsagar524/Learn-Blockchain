# Learn-Blockchain
Learning Blockchain with Python

- Hashing
Hashing is an one way process in which you can convert any word or sentence to a fixed number of words. Here SHA256 is used i.e. any word or sentence is converted to 256 digit hex number.
Code -> https://github.com/subhamsagar524/Learn-Blockchain/blob/master/hashing/hashing.py

- Public & Private Key
These are a pair of keys which can be circulated to each and every individual uniquely. For that, first I took the information from the user say name and age. So now I can append the name and age into a sentence and produce the hash but, suppose there are more than one person having same name and age. Hence, to avoid this conflict I appended the timestamp with the name and age. Like "john 25 1581956050.994884" i.e. "name age timestamp". Come on it is almost not possible that more than one person would produce their keys at the same time with 6 digit of precision in mili seconds. I got the timestamp from the time library.
After getting the whole sentence I hashed it once to got the public key. Then, hash the public key to get the privete key.
Code -> https://github.com/subhamsagar524/Learn-Blockchain/blob/master/hashing/public_private_key.py
