from node2 import Node

class LinkedList2 :
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
 def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
 def insert_before(self, value, new_value):
        new_node = Node(new_value)
        if self.head and self.head.value == value:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current and current.next:
                if current.next.value == value:
                    new_node.next = current.next
                    current.next = new_node
                    return
                current = current.next
 def insert_after(self, value, new_value):
        new_node = Node(new_value)
        current = self.head
        while current:
            if current.value == value:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next