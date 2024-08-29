from turtle import Screen
import time

from snake import Snake
from food import Food
from border import Border
from scoreboard import ScoreBoard

screen = Screen()

screen.setup(700, 700)
screen.bgcolor("black")
screen.title("The Snake Game")

screen.tracer(0)
screen.listen()

is_game_over = False

snake = Snake()
food = Food()
score_board = ScoreBoard()

border = Border()

border.draw_horizontal_border((-290, 250))
border.draw_horizontal_border((-290, -290))

border.draw_vertical_border((-290, 250))
border.draw_vertical_border((290, 250))

screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

while not is_game_over:
	screen.update()
	time.sleep(0.1)
	snake.move()
	score_board.display_scores()

	# Detect collision with food
	if snake.head.distance(food) < 15:
		food.create_food()
		snake.grow_up()
		score_board.increase_scores()

	# Detect collision with wall
	if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 250 or snake.head.ycor() < -290:
		is_game_over = True
		score_board.game_over()

	# Detect collision with tail
	for segment in snake.segments[3:]:
		if segment.distance(snake.head) < 10:
			is_game_over = True
			score_board.game_over()
			break

screen.exitonclick()
