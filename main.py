from HashTable import HashTable
from Node import Node

Table = HashTable(1,1)

print(Table.Table)

print("\n")

Node1 = Node("jrptf",1314)
Node3 = Node("xqoao",3566)
Node4 = Node("psiwf",2453)
Node5 = Node("szccc",9203)
Node6 = Node("pwnjl",3892)
Node7 = Node("wiink",1234)
Node8 = Node("fzvxi",3032)
Node9 = Node("krffq",5685)
Node10 = Node("pxawo",7722)
Node11 = Node("wtdmi",7722)

Table.Insert(Node1)
Table.Insert(Node3)
Table.Insert(Node4)
Table.Insert(Node5)
Table.Insert(Node6)
Table.Insert(Node7)
Table.Insert(Node8)
Table.Insert(Node9)
Table.Insert(Node10)

print(Table.Table)

Table.Insert(Node11)

print("\n")

print(Table.Table)

print("\n")

print(Table.Find("wtdmi"))