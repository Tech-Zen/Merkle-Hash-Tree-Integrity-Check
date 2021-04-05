#Isaac Beasley
#Merkle Root Algorithim with n file input

import hashlib
import os
#Loop to open all files and append them to list
folderpath = r"C:/Users/isaac/Desktop/merkle files/"
filepaths = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]

#creates empty list to store hashed SHA-1 files
leaves = []

#open all files in folderpath, hash the files, and append them to the leaves list
for path in filepaths:
    with open(path, 'r') as f:
        data = f.read()
        #hash the file's contents
        hash = hashlib.sha1(data.encode('utf-8')).hexdigest()
        leaves.append(hash)
print("Blocks hashes:")
print(leaves)
print('')

#Merkle tree is binary tree
#Checks if num of files is odd, if so duplicate last file's hash to list
if (len(leaves) % 2 != 0):
    leaves.append(leaves[-1])

#Concatinate every pair list items, and pair hashes, continue loop untill Merkle Root is reached
while (len(leaves)> 1) :
    j = 0
    for i in range(0, len(leaves) - 1):
        leaves[j] = hashlib.sha1(leaves[i].encode('utf-8') + leaves[i+1].encode('utf-8')).hexdigest()
        i += 2
        j += 1

    #deletes extra space in list
    lastDelete = i - j
    del leaves[-lastDelete:]
    print(leaves)

MerkleRoot = leaves
#This prints the Merkle Root
print("Merkle Root:", MerkleRoot)
