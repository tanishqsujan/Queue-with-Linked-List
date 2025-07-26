class GFG:
    #Node of a doubly linked list
    class Node:
        data= 0
        prev= None
        next= None
        
        #Function to get a new node
        @staticmethod
        def getnode(data):
            newnode= GFG.Node()
            newnode.data= data
            newnode.prev= None
            newnode.next= None
            return newnode
        
        
    #A structure to represent a deque
    class Deque:
        front= None
        rear= None
        Size= 0
        
        def __init__(self):
            self.front= None
            self.rear= None
            self.Size= 0
            
        #Function to check whether deque is empty or not
        def isEmpty(self):
            return (self.front == None)
        
        
        #Function to return the number of elements in the deque
        def size(self):
            return self.Size
        
        def insertFront(self,data):
            newnode= GFG.Node.getnode(data)
            
            #If true then new element cannot be added and it is an overflow condition
            if (newnode == None):
                print("Overflow\n", end= "")
            else:
                
                #If deque is empty
                if(self.front== None):
                    self.rear= newnode
                    self.front= newnode
                else:
                    newnode.next= self.front
                    self.front.prev= newnode
                    self.front= newnode
                    
                #Increments count of elements by 1
                self.Size += 1
                
        #Function to insert an element at the rear end
        def insertRear(self,data):
            newnode= GFG.Node.getnode(data)
            
            #If true then new element cannot be added and it is an 'Overflow' condition
            if (newnode == None):
                print("Overflow\n", end= "")
            else:
                
                #If deque is empty
                if (self.rear == None):
                    self.front= newnode
                    self.rear= newnode
                else:
                    newnode.prev= self.rear
                    self.rear.next= newnode
                    self.rear= newnode
                self.Size += 1
                
        #Function to delete the element from the front end
        def deleteFront(self):
            
            #If deque is empty then
            #Underflow condition
            if (self.isEmpty()):
                print("Underflow\n", end= "")
            else:
                temp= self.front
                self.front= self.front.next
                
                #If only one element was present
                if (self.front== None):
                    self.rear= None
                else:
                    self.front.prev= None
                    
                    
                #decrements count of elements