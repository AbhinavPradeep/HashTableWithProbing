from Node import Node
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

class HashTable:
    def __init__(self,A,B) -> None:
        self.Table = np.empty(10, dtype=Node)
        self.A = A
        self.B = B

    def Hash(self,Key):
        Hash = 0
        for Char in Key:
            Hash += ord(Char)
        return Hash
    
    def Insert(self,Node:Node):
        Index = self.Hash(Node.Key)%10
        if None not in self.Table:
            return
        if self.Table[Index] == None:
            self.Table[Index] = Node
        else:
            i = 1
            while self.Table[Index] != None:
                Index = (Index + self.A*i + self.B*(i**2))%10
            self.Table[Index] = Node

    def Delete(self,Key):
        Index = self.Hash(Key)%10
        self.Table[Index] = None

    def Find(self,Key):
        Index = self.Hash(Key)%10
        if self.Table[Index].Key == Key:
            return self.Table[Index]
        else:
            i = 1
            while self.Table[Index].Key != Key:
                Index = (Index + self.A*i + self.B*(i**2))%10
            return self.Table[Index]