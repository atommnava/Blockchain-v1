import hashlib

class NeuralCoinBlock:
    def __init__(self, prevBlockHash, transList):
        self.prevBlockHash = prevBlockHash
        self.transList = transList

        self.blockData = "-".join(transList) + "-" + prevBlockHash
        # To calculate the hash
        self.blockHash = hashlib.sha256(self.blockData.encode()).hexdigest()

t1 = "Tom sends 2 NC to Mike"
t2 = "Bob sends 4.2 NC to Mike"
t3 = "Mike sends 3.2 NC to Bob"
t4 = "Daniel sends 0.3 NC to Tom"
t5 = "Mike sends 1 NC to Charlie"
t6 = "Mike sends 5.2 NC to Daniel"

initialBlock = NeuralCoinBlock("Initial String", [t1,t2])

print(initialBlock.blockData)
print(initialBlock.blockHash)

secondBlock = NeuralCoinBlock(initialBlock.blockHash, [t3,t4])

print(secondBlock.blockData)
print(secondBlock.blockHash)

thirdBlock = NeuralCoinBlock(secondBlock.blockHash, [t5,t6])

print(thirdBlock.blockData)
print(thirdBlock.blockHash)