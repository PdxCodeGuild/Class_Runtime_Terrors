#lab 1 turtle
#using the example for N-sided figure and color fill

from turtle import *
fillcolor('green')
begin_fill()

edge_length = 500
no_face = 8

i = 0
while i < no_face:
	forward(edge_length/no_face)
	right(360/no_face)
	i = i + 1

end_fill()
done()
