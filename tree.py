class tree():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.level = 1

    def insertL(self, data, parentNode=None, left=None, right=None):
        newNode = tree(data, left, right)

        if parentNode == None:
            self.left = newNode
            self.left.level = self.level + 1
            return self.left
        else:
            parentNode.left = newNode
            parent.left.level = self.level + 1
            return parent.left

    def insertR(self, data, parentNode=None, left=None, right=None):
        newNode = tree(data, left, right)
        if parentNode == None:
            self.right = newNode
            self.right.level = self.level + 1
            return self.right

        else:
            parentNode.right = newNode
            parent.right.level = self.level + 1
            return parent.right

    def showTree(self, currentNode=None):
        if currentNode == None:
            currentNode = self

        print(" (", end="")

        if currentNode.left != None:
            self.showTree(currentNode.left)

        print(str(currentNode.data)+"", end="")

        if currentNode.right != None:
            self.showTree(currentNode.right)

        print(") ", end="")


parent = None  # createNodeTree functon creates a tree and assign its value to parent


def createNodeTree(value, _parent=None):
    global parent
    if _parent == None:
        _parent = tree(value)
        parent = _parent

    newValue = value // 2

    if newValue >= 1:
        tl = _parent.insertL(newValue)
        tr = _parent.insertR(newValue)
        createNodeTree(newValue, tl)
        createNodeTree(newValue, tr)
    else:
        return


height = 0  # setHeight functon set height


def setHeight(tree):
    global height
    if tree is not None:
        if height < tree.level:
            height = tree.level
        setHeight(tree.left)
        setHeight(tree.right)
    else:
        return


createNodeTree(20)
# parent.right.right.right.right.insertL(45)
setHeight(parent)

width = 2**(height-1)

'''
parent.showTree()
print("\n------Height : ", height, "\n-------Width : ", width)
'''
