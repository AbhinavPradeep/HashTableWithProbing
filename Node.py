class Node:
    def __init__(self,Key,Data) -> None:
        self.Key = Key
        self.Data = Data
    
    def __str__(self) -> str:
        return f"({self.Key}, {self.Data})"
    
    __repr__ = __str__