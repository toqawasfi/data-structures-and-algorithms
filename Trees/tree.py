class TreeNode():
    '''
    Class contains three instances root,left and right
    '''
    def __init__(self,root):
        self.root=root
        self.left=None
        self.right=None
class Binary_Tree():
    '''
    class to travers my tree using different wany (preorder,inorder and post order)
    
    '''
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        self.max=-1000
    
    def in_order(self,my_arr):
        '''
        Method to traverse my tree as the following (left,root,right)
        args:list
        return list
       
        '''
       
        if self.left:
            self.left.in_order(my_arr)
        if self.value is not None:
            my_arr.append(self.value)
        if self.right:
            self.right.in_order(my_arr)
        return my_arr

    def pre_order(self,my_arr):
        '''
        Method to traverse my tree as the following (root,left,right)
        args:list
        return list
       
        '''
       
        my_arr.append(self.value)
        # print(self.value)
        if self.left:
            self.left.pre_order(my_arr)
        if self.right:
            self.right.pre_order(my_arr)
   
    def post_order(self,my_arr):
        '''
        Method to traverse my tree as the following (left,right,root)
        args:list
        return list
       
        '''
      
        if self.left:
            self.left.post_order(my_arr)
        if self.right:
            self.right.post_order(my_arr)
        # print(self.value)
        my_arr.append(self.value)
    
    
    def breadth_traversal(self):
        result = []
        my_queue = []
        my_queue.append(self)

        while my_queue:
            node = my_queue.pop(0)
            result.append(node.value)

            if node.left:
                my_queue.append(node.left)
            if node.right:
                my_queue.append(node.right)
        
        print(result)
        return result

            
            
        


        
class Binary_Search_Tree(Binary_Tree):
    '''
    A class contains three methods to print the tree ,to add nodes and to search for a node
    receives a Binary_Tree class 
    '''
    def __init__(self, value=None):
        super().__init__(value)

    def print_nodes(self):
        '''
        method to print my tree
        args:None
        return:Nonne
        '''
        nodes = []
        if self.left:
            nodes.extend(self.left.print_nodes())
        nodes.append(str(self.value))
        if self.right:
            nodes.extend(self.right.print_nodes())
        return nodes
    def Add(self,value):
        '''
        A method to add nodes
        args:value(int)
        returns:None
        
        '''
        
        if self.value>self.max:  #How iam checking my max
            self.max=self.value
        elif value>self.max:
            self.max=value 

        if value<self.value :
            if self.left is None:
                self.left = Binary_Search_Tree(value)
                
            else:
                self.left.Add(value)
        else:
            if self.right is None:
                self.right = Binary_Search_Tree(value)
                self.max=self.right.value
               
            else:
                self.right.Add(value)


    def Contains(self,value):
        '''
        A method to search for value
        args:value(int)
        returns:Bool
        
        '''
       
        if value == self.value:
            return True
        elif value < self.value and self.left is not None:
           return self.left.Contains(value)
        elif value > self.value and self.right is not None:
            return self.right.Contains(value)
        return False
    
    def tree_max(self):
        '''
        A method finds max value in a tree.
        args:None
        return:value(int)
        '''
        return self.max

       
            
       
        


my_arr = []
tree = Binary_Search_Tree(20)
tree.Add(5)
tree.Add(3)
tree.Add(100)
tree.Add(70)
tree.Add(90)
tree.Add(40)
tree.breadth_first_traversal()
# tree.in_order(my_arr)
# print(my_arr)
# print(tree.Contains(5))  

print(tree.print_nodes()) 
# print("my_max",tree.tree_max())    
