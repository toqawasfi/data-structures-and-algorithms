class Node():
   def __init__(self,value):
      self.value=value
      self.next=None

   def __repr__(self):
        return str(self.value)

class my_stack():
   '''
    Initilizer constructor
    '''
   def __init__(self):
      self.top=None
      self.size=0

   '''
    Method to reformat the output from the user side

   '''
   def __str__(self):
    output = ""
    current = self.top
    while current:
        output += f"{current.value} -> "
        current = current.next
   
    return output
   '''
    Method to reformat the output from the terminal side
    '''
   def __repr__(self):
    if self.top is None:
        return "Empty LinkedList"
    current = self.top
    nodes = []
    while current:
        nodes.append(str(current.value))
        current = current.next
    return " -> ".join(nodes)
 

   '''
      A method to check if my stack is empty
      args:
      int :size
      returns:
      Boolean 
  '''
   def is_empty(self,size):
      if size ==0:
         return True
      else:
         return False
   '''
    A method to add nodes to the top of my stack
    args: 
    int ,value
    return:
    None
    '''

   def push(self,value):
      
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1
        return self.top
   '''
      A method to delete the top node from my stack
      return:the value of deleted node
      
  '''
   def pop(self):
     if self.top is not None:
            temp = self.top.value
            self.top = self.top.next
            
            self.size -= 1
            return temp
     else:
          if self.is_empty(self.size):
           raise Exception("its empty")
     '''
   A method responsible for returning mytop value
   args:None
   return: The value of my Top
   '''
   def peek(self):
    #  node=Node(value)
     if self.top is None:
        if self.is_empty(self.size):
          raise Exception("its empty")
     
     return self.top.value
   


my_stack1=my_stack()
my_stack1.push(5)
my_stack1.push(6)
print(my_stack1.pop())
print(my_stack1.peek())