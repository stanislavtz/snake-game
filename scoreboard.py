from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 18, 'bold')


def get_high_score():
	with open("high-score.txt", mode="r") as file:
		score_list = file.read()
		high_score = score_list.split(" ")[-1]
		return int(high_score)


def save_high_score(score):
	with open("high-score.txt", mode="w") as file:
		file.write(f"High_score = {score}")


class ScoreBoard(Turtle):
	def __init__(self):
		super().__init__()
		self.score= 0
		self.high_score = get_high_score()
		self.color("white")
		self.penup()
		self.goto(0, 260)
		self.hideturtle()

	def display_scores(self):
		self.clear()
		self.write(arg=f"Score: {self.score}. High-score: {self.high_score}", align=ALIGNMENT, font=FONT)

	def increase_scores(self):
		if self.high_score == self.score:
			self.high_score += 1
		self.score += 1

	def game_over(self):
		self.goto(0, 0)
		self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
		save_high_score(self.high_score)