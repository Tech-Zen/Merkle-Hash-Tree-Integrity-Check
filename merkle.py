#Merkle Root Algorithim with n file input
#Coded by Isaac Beasley
#For CIS 555

#importing necessary libraries
#hashlib  library for hashing functions
#os allows access to os system dependent functionality
import hashlib
import os 

#This Loop opens all files in the listed directory, and appends them to leaves list
#Change this path to your desired directory to use of this program.
folderpath = r"C:/Users/isaac/Desktop/merkle files/"
filepaths = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]

#Creates empty list to store hashed SHA-1 files
leaves = []

#Open all files in folderpath, hash the files using Hashlib sha1, and append them to the leaves list
for path in filepaths:
    with open(path, 'r') as f:
        data = f.read()
        hash = hashlib.sha1(data.encode('utf-8')).hexdigest()
        leaves.append(hash)
#Prints first row and base layer of Merkle Tree
print("Blocks hashes:")
print(leaves)

#This function prints combined leaf pairs
def print_leaves():
    print(','.join(leaves))

#This function determines if input is odd
def is_odd(n):
    return n % 2 == 1

#First it checks if the number of leaves is odd. As we want a binary tree, we will append the last item in the list to make it even.
while len(leaves) > 1:
    if is_odd(len(leaves)):
        leaves.append(leaves[-1])
        print_leaves()
    i = 0
    j = 0
    #These loops act to step, and jump through the base Merkle leaves
    #Once equal pairs are created, they're concatinated and hashed into a parent leaf using SHA-1.
    while j < len(leaves):
        leaves[i] = leaves[j] + leaves[j + 1]
        leaves[i] = hashlib.sha1(leaves[i].encode('utf-8')).hexdigest()
        i += 1
        j += 2
    leaves = leaves[:len(leaves) // 2]
    print_leaves()

#Assigns leaves list to MerkleRoot, just for easier understanding of code
MerkleRoot = leaves
#This prints the Merkle Root
print('')
print("Merkle Root Hash:", MerkleRoot)
