from node3 import Node

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
 def kth_from_end(self, k):
        if self.head is None:
            return None

        current_node = self.head
        count = 0
        while current_node is not None:
            count += 1
            current_node = current_node.next

        if k > count:
            return None

        current_node = self.head
        for i in range(count - k):
            current_node = current_node.next

        return current_node.value