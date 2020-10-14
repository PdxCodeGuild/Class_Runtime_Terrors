from turtle import *


def head():
    circle(50)  # head
    fillcolor("black")
    begin_fill()
    left(-90)


def neck():
    forward(100)  # stick neck
    right(90)


def arm():
    forward(100)  # arm
    left(180)
    forward(200)  # arm
    right(180)


def body():
    forward(100)
    left(90)
    forward(150)


def legs():
    left(45)
    forward(100)
    right(180)
    forward(100)
    left(90)
    forward(100)


head()
neck()
arm()
body()
legs()

done()
