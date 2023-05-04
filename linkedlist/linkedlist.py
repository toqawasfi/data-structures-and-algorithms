class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList :
 def __init__(self):
    self.head =None

 
 def __str__(self):
    output = ""
    current = self.head
    while current:
        output += f"{current.value} -> "
        current = current.next
    output += "Null"
    return output
 
 
 def __repr__(self):
    if self.head is None:
        return "Empty LinkedList"
    current = self.head
    nodes = []
    while current:
        nodes.append(str(current.value))
        current = current.next
    return " -> ".join(nodes)

 
      
 def insert(self,value):
     node = Node(value)
     current = self.head
     self.head=node
     node.next=current

 def includes(self,value):
       current =self.head
       while current  is not None:
        if value == current.value :
           return True
           break
        current=current.next
        if current == None:
         return False
        