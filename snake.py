from turtle import Turtle

INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
COLOR = "white"
SHAPE = "square"
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
	def __init__(self):
		self.segments = []
		self.create_snake()
		self.head = self.segments[0]

	def create_snake(self):
		for position in INITIAL_POSITIONS:
			new_segment = self.create_segment(position)
			self.segments.append(new_segment)

	@staticmethod
	def create_segment(position):
		segment = Turtle()
		segment.penup()
		segment.shape(SHAPE)
		segment.color(COLOR)
		segment.goto(position)
		return segment

	def move(self):
		for index in range(len(self.segments) - 1, 0, -1):
			current = self.segments[index]
			previous = self.segments[index-1]

			new_xcor = previous.xcor()
			new_ycor = previous.ycor()
			current.goto(new_xcor, new_ycor)
		self.head.forward(MOVE_DISTANCE)

	def up(self):
		if self.head.heading() != DOWN:
			self.head.setheading(UP)

	def down(self):
		if self.head.heading() != UP:
			self.head.setheading(DOWN)

	def left(self):
		if self.head.heading() != RIGHT:
			self.head.setheading(LEFT)

	def right(self):
		if self.head.heading() != LEFT:
			self.head.setheading(RIGHT)

	def grow_up(self):
		last_segment = self.segments[-1]
		new_segment = self.create_segment(last_segment.position())
		self.segments.append(new_segment)




