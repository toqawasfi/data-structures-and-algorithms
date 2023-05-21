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
      self.max=0
      self.checker=None

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

   def push(self, value):  
        
         node = Node(value)
         if self.top:
               
               node.next = self.top
               self.top=node
               self.checker=self.top
               
               while  self.checker and self.checker.next:#2 nods +
                  if self.checker.next.value > self.checker.value and self.checker.next.value >self.max:
                     self.max =self.checker.next.valu
                  elif self.checker.value > self.checker.next.value and self.checker.value > self.max:
                       self.max =self.checker.value
              
                 
                  self.checker = self.checker.next
                 
         else:
            self.top = node
            self.max = node.value
                  
                
         # self.top = node
         # self. max=node.value
         # self.size += 1
         
         return self.top,self.max
   '''
      A method to delete the top node from my stack
      return:the value of deleted node
      
  '''
   def pop(self):
    if self.top is not None:
        temp = self.top.value
        self.top = self.top.next
        self.checker = self.top
        self.max = 0
        while self.checker:
            if self.checker.next is None:
                self.max = self.checker.value
            elif self.checker.next.value > self.checker.value and self.checker.next.value > self.max:
                self.max = self.checker.next.value
            elif self.checker.value > self.checker.next.value and self.checker.value > self.max:
                self.max = self.checker.value
            self.checker = self.checker.next
        self.size -= 1
        return temp, self.max
    else:
        if self.is_empty(self.size):
            raise Exception("The stack is empty.")

   # def pop(self):
     
   #   if self.top is not None:
   #          print("top:",self.top)
           
   #          self.max=0
   #          temp = self.top.value
   #          self.top = self.top.next
   #          self.checker=self.top
   #          print("new_top:",self.top)
   #          print("new_max",self.max)
   #          print("self.checker",self.checker.value)
   #          print("self.checker.next",self.checker.next.value)
   #          while  self.checker:#2 nods +
   #                if self.checker.next is None:
   #                   #  self.max=self.top.value
   #                   self.max = self.checker.value
   #                elif self.checker.next.value > self.checker.value and self.checker.next.value >self.max:
   #                   self.max =self.checker.next.value
   #                   # print("max is22",self.max)
   #                   # self.checker = self.checker.next
   #                elif self.checker.value > self.checker.next.value and self.checker.value > self.max:
   #                     self.max =self.checker.value
                 
              
   #                # self.max =self.checker.value
   #                self.checker = self.checker.next
   #                # print("max is11",self.max)
   #          self.size -= 1
   #          return temp,self.max
   #   else:
   #        if self.is_empty(self.size):
   #         raise Exception("its empty")
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
   
   def get_max(self):
    return self.max


my_stack1=my_stack()
my_stack1.push(10)
my_stack1.push(50)
my_stack1.push(90)
my_stack1.push(100)
print(my_stack1.pop())
print(my_stack1.pop())
print(my_stack1.pop())
print(my_stack1.pop())
print(my_stack1.max)
print(my_stack1)
print("Maximum value:", my_stack1.get_max())

# print(my_stack1.get_max()) print("checker_value_next",self.checker.next.value