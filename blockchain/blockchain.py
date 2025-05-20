import hashlib

class NeuralCoinBlock:
    def __init__(self, prevBlockHash, transList):
        self.prevBlockHash = prevBlockHash
        self.transList = transList

        self.blockData = "-".join(transList) + "-" + prevBlockHash