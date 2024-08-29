from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 18, 'bold')


class ScoreBoard(Turtle):
	def __init__(self):
		super().__init__()
		self.scores = 0
		self.color("white")
		self.penup()
		self.goto(0, 260)
		self.hideturtle()

	def display_scores(self):
		self.clear()
		self.write(arg=f"Scores: {self.scores}", align=ALIGNMENT, font=FONT)

	def increase_scores(self):
		self.scores += 1

	def game_over(self):
		self.goto(0, 0)
		self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)