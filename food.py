from turtle import Turtle
import random

SHAPE = "circle"
COLOR = "blue"


class Food(Turtle):
	def __init__(self):
		super().__init__()
		self.shape(SHAPE)
		self.shapesize(0.5, 0.5)
		self.color(COLOR)
		self.penup()
		self.create_food()

	def create_food(self):
		random_x = random.randint(-280, 280)
		random_y = random.randint(-280, 240)
		self.goto(random_x, random_y)

