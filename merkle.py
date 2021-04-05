#Merkle Root Algorithim with n file input
import hashlib
import os

#Loop to open all files and append them to leaves list
folderpath = r"C:/Users/isaac/Desktop/merkle files/"
filepaths = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]

#creates empty list to store hashed SHA-1 files
leaves = []

#open all files in folderpath, hash the files, and append them to the leaves list
for path in filepaths:
    with open(path, 'r') as f:
        data = f.read()
        hash = hashlib.sha1(data.encode('utf-8')).hexdigest()
        leaves.append(hash)
print("Blocks hashes:")
print(leaves)

#This function prints combined leaf pairs
def print_leaves():
    print(','.join(leaves))

#This function determines if input is odd
def is_odd(n):
    return n % 2 == 1

while len(leaves) > 1:
    if is_odd(len(leaves)):
        leaves.append(leaves[-1])
        print_leaves()
    i = 0
    j = 0
    while j < len(leaves):
        leaves[i] = leaves[j] + leaves[j + 1]
        leaves[i] = hashlib.sha1(leaves[i].encode('utf-8')).hexdigest()
        i += 1
        j += 2
    leaves = leaves[:len(leaves) // 2]
    print_leaves()

MerkleRoot = leaves
#This prints the Merkle Root
print('')
print("Merkle Root Hash:", MerkleRoot)
