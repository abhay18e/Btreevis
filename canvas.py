from tkinter import Canvas
from tree import root, height, width

# root.showTree()
radius = 10
node_verticle_distance = 30
node_horizontal_distance = radius*2

print(height, width)

height_px = 2*radius + (height-1)*(radius*2 + node_verticle_distance)
width_px = 2*radius + (width-1)*(radius*2 + node_horizontal_distance)
print(height_px, width_px)
#creating canvas
canvas = Canvas(height=height_px, width=width_px, bg="red")
canvas.pack()
    

def drawCircle(x, y, r):
    x1 = x-r
    x2 = x+r
    y1 = y-r
    y2 = y+r
    canvas.create_oval(x1, y1, x2, y2)


def connectLine(x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2, width=3)


def drawNode(node, y=None, x=None):
    global radius, height

    if node is not None:

        drawCircle(x, y, radius)
        y_next = y + node_verticle_distance + 2*radius
        x_left = x - 2**(height-node.level-1)*node_horizontal_distance
        x_right = x + 2**(height-node.level-1)*node_horizontal_distance
        drawNode(node.left, y_next, x_left)
        drawNode(node.right, y_next, x_right)

    else:
        return 1


drawNode(root, radius, width_px//2)


canvas.mainloop()
