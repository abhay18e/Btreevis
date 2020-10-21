from tkinter import *
from tree import parent, height, width
from random import randint

# parent.showTree()
radius = 10
node_verticle_distance = 30
node_horizontal_distance = radius*2

print(height, width)

height_px = 2*radius + (height-1)*(radius*2 + node_verticle_distance)
width_px = 2*radius + (width-1)*(radius*2 + node_horizontal_distance)
print(height_px, width_px)


class Node():
    def __init__(self, height=400, width=400, color="red"):
        self.h = height
        self.w = width
        self.color = color
        self.canvas = Canvas(height=self.h, width=self.w, bg=self.color)
        self.canvas.pack()

        # self.canvas.mainloop()

    def draw(self, x, y, r):
        #print("y: ", y)
        x1 = x-r
        x2 = x+r
        y1 = y-r
        y2 = y+r

        self.canvas.create_oval(x1, y1, x2, y2)
        self.canvas.pack()
        # self.canvas.mainloop()

    def connectLine(self, x1, y1, x2, y2):
        self.canvas.create_line(x1, y1, x2, y2)
        self.canvas.pack()


def drawNodes(node, y=None, x=None):
    global radius, height

    if node is not None:

        n1.draw(x, y, radius)
        y_next = y + node_verticle_distance + 2*radius

        #print("\n>>>>>>>>>>", node.level, ">>>", (height-node.level-1))
        x_left = x - 2**(height-node.level-1)*node_horizontal_distance
        x_right = x + 2**(height-node.level-1)*node_horizontal_distance
        n1.connectLine(x, y, x_left, y_next)
        n1.connectLine(x, y, x_right, y_next)

        # print(x_left,x_right)
        #print(" (", end="")
        drawNodes(node.left, y_next, x_left)
        #print(x, end="")
        drawNodes(node.right, y_next, x_right)
        #print(") ", end="")
    else:
        return 1


#parent.loc["x"] = width_px//2
#parent.loc["y"] = radius
n1 = Node(height_px, width_px)

drawNodes(parent, radius, width_px//2)


n1.canvas.mainloop()
