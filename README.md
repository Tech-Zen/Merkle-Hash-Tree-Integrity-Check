# Merkle-Hash-Tree-Integrity-Check
![Merkle Tree Example](https://raw.githubusercontent.com/Tech-Zen/Merkle-Hash-Tree-Integrity-Check/main/Hash_Tree.svg.png)

# What is a Merkle Tree?
"A Merkle Tree allows computers on a network to verify individual records without having to review and compare versions of the entire database. They do so by using cryptography that reveals an individual record while also guaranteeing that all the other records in the database haven’t been changed. First patented in 1979 by Ralph Merkle, Merkle trees have been an important key to database verification throughout the history of computers (Bennett Garner 2018)."

# My code
Using Python, I attempted to implement the Merkle Tree algorithim. This program inputs files from my Desktop directory, and then computes the respective SHA1 hashes. Once the base data blocks have been hashed, the program combines the leaves into equal pairs hashes them into a parent leaf. This process then continues untill the Merkle Root has been reached. 
