from swampy.World import World


class Canvas():
    """creates the window

        attributes: width, height, color
    """


class Rectangle():
    """attributes: x1,x2,y1,y2,color"""


class Point():
    """attributes: x,y"""


class Circle():
    """attributes: x,y,radius"""


world = World()


def draw_rect(c,r):
    angle = world.ca(width=window.width,height=window.height,background=window.color)
    bbox = [[box.x1, box.y1],[box.x2, box.y2]]
    angle.rectangle(bbox,fill=box.color)


def draw_point(c,p):
    b = world.ca(width=window.width,height=window.height,background=window.color)
    point = [[p.x,p.y],[p.x,p.y]]
    b.rectangle(point)


def draw_circle(cir):
    hello = World()
    e = hello.ca(width=window.width,height=window.height,background=window.color)
    e.circle([cir.point.x,cir.point.y],cir.radius, outline="green", fill="black")
    hello.mainloop()

box = Rectangle
box.x1 = -40
box.x2 = 40
box.y1 = -60
box.y2 = 60
box.color = 'red'

window = Canvas()

window.width = 400
window.height = 600
window.color = 'white'

point = Point()
point.x = 40
point.y = 50

circle1 = Circle()
circle1.point = Point()
circle1.point.x = 10
circle1.point.y = 10
circle1.radius = 40

circle2 = Circle()
circle2.point = Point()
circle2.point.x = 20
circle2.point.y = 20
circle2.radius = 50

circle3 = Circle()
circle3.point = Point()
circle3.point.x = 30
circle3.point.y = 30
circle3.radius = 75


draw_rect(window,box)


draw_point(window,point)


draw_circle(circle1)
draw_circle(circle2)
draw_circle(circle3)

world.mainloop()
