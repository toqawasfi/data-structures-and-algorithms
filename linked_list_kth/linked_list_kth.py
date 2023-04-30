from linked_list_kth.node2 import Node
class LinkedList1 :
 def __init__(self):
    self.head =None

 
 def __str__(self):
        """ this method is intended for the user to see the linked list after any changes if he/she want"""
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
        '''
        This Method to return the index of an element from the tail
        Takes an int argument to search for its index
        returns an int which represnts the index
        '''
        if self.head is None:
            raise ValueError('List is empty')

        length = 0
        current_node = self.head
        
        while current_node is not None:
            length += 1
            current_node = current_node.next

        if k > length or k<0:
            raise ValueError('k is out of range')
        if k==length:
             raise Exception("Sorry, K is equal to the length of linked list")
         
        
        
        if k == length//2 and k>0:
                 return "Happy Path"

        current_node = self.head
        for i in range(length - k):
            current_node = current_node.next
            if current_node is None and k>0:
                raise ValueError('k not found in linked list')

        if length == 1 and k==0:
            return self.head.value
        else:
            return current_node.value
 
 def append(self, value):
        '''
        This Method is to appened element to the linked list
        '''
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

## ######################################### stretch Goal #############################################
 def find_middle_node(self):
        if self.head is None:
            raise ValueError('List is empty')

        first = self.head
        second = self.head

        while second is not None and second.next is not None:
           first =first.next
           second = second.next

        return first.value