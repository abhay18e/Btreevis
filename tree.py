class tree():
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
        
    def insertL(self,data,parentNode=None,left=None,right=None):
        newNode = tree(data,left,right)
        if parentNode == None:
            self.left = newNode
        else:
            parentNode.left = newNode
            
        return newNode
    
    def insertR(self,data,parentNode=None,left=None,right=None):
        newNode = tree(data,left,right)
        if parentNode == None:
            self.right = newNode
        else:
            parentNode.right = newNode
            
        return newNode
    
    def showTree(self,currentNode=None):
        if currentNode == None:
            currentNode = self
            
        print("(",end="")
        
        if currentNode.left != None:
            self.showTree(currentNode.left)
            
        print(str(currentNode.data)+"",end="")
        
        if currentNode.right != None:
            self.showTree(currentNode.right)
            
        print(")",end="")
        
     
     
t1 = tree(100)
t1.insertR(80)
t1.insertL(20).insertR(25)

t1.showTree()
