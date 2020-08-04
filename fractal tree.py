
__author__ : '@rockdevu'

import turtle as tu

s = tu.Turtle()
s.screen.bgcolor('orange')
s.left(90)
s.speed(20)
s.color('white')
s.pensize(5)
s.screen.title('rockdevu')

def draw_fractal(val):
	if (val<10):
		return
	else:
		s.forward(val)
		s.left(30)
		draw_fractal(3*val/4)
		s.right(60)
		draw_fractal(3*val/4)
		s.left(30)
		s.backward(val)
draw_fractal(80)
s = tu.done()