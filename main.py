from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import Brick
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)  # Turn off animation

# Create paddle
paddle = Paddle((0, -250))

# Create ball
ball = Ball()

# Create bricks
colors = ["red", "orange", "yellow", "green", "blue"]
bricks = []
for row in range(5):
    y_pos = 150 - (row * 30)  # Start from top, each row 30 pixels apart
    for col in range(8):
        x_pos = -350 + (col * 100)  # 8 bricks per row, 100 pixels apart
        brick = Brick((x_pos, y_pos), colors[row])
        bricks.append(brick)

# Set up keyboard controls
screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

# Game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # Detect collision with walls
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()
    if ball.ycor() > 280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -230:
        ball.bounce_y()

    # Detect collision with bricks
    for brick in bricks[:]:  # Use slice copy to safely remove during iteration
        if ball.distance(brick) < 40:
            brick.hideturtle()
            bricks.remove(brick)
            ball.bounce_y()

    # Detect paddle miss
    if ball.ycor() < -280:
        game_is_on = False

screen.exitonclick()