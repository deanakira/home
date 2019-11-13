from turtle import*
shape('turtle')
speed(0)
def square(sidelength=100):
    for i in range(4):
        forward(sidelength)
        right(90)
        
def triangle(sidelength=200):
    for i in range(3):
        forward(sidelength)
        rt(120)


def polygon(sides=4,sidelength=100):
    for i in range(sides):
        forward(sidelength)
        right(360/sides)

polygon(1000,2)
