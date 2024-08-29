from turtle import Turtle

COLOR = "white"
HEADING = 270
H_DISTANCE = 580
V_DISTANCE = 540


class Border(Turtle):
	def __init__(self):
		super().__init__()
		self.hideturtle()
		self.color(COLOR)

	def draw_horizontal_border(self, position):
		self.penup()
		self.goto(position)
		self.pendown()
		self.forward(H_DISTANCE)

	def draw_vertical_border(self, position):
		self.penup()
		self.goto(position)
		self.pendown()
		self.setheading(HEADING)
		self.forward(V_DISTANCE)