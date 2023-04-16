from node import Node

class LinkedList :
 def __init__(self):
    self.head =None

 
 def __str__(self):

        output = ""
        
        if self.head is None:
            output = "Empty LinkeList"
        else:
            current = self.head
            while(current):
                output += f'{{{current.value} }}-> '
                current = current.next
            
            output += " Null"
        return output
 
 def __repr__(self):

        output = ""
        
        if self.head is None:
            output = "Empty LinkeList"
        else:
            current = self.head
            while(current):
                output += f'{{current.value}} -> '
                current = current.next
            
            output += " NULL"
        return output
    
 
      
 def insert(self,value):
     node = Node(value)
     current = self.head
     self.head=node
     node.next=current

 def includes(self,value):
       current =self.head
       while current  is not None:
        if value == current.value :
           print(True)
           break
        current=current.next
        if current == None:
         print(False)
        