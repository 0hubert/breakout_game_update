from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard
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
colors = ["red", "purple", "white", "indigo", "blue"]
bricks = []
for row in range(5):
    y_pos = 150 - (row * 30)  # Start from top, each row 30 pixels apart
    for col in range(8):
        x_pos = -350 + (col * 100)  # 8 bricks per row, 100 pixels apart
        brick = Brick((x_pos, y_pos), colors[row])
        bricks.append(brick)

# Create scoreboard (moved before game loop)
scoreboard = Scoreboard()

def reset_game():
    global game_is_on, bricks
    game_is_on = True
    ball.reset_position()
    paddle.goto(0, -250)
    scoreboard.reset()
    
    # Clear existing bricks
    for brick in bricks:
        brick.hideturtle()
    bricks.clear()
    
    # Recreate bricks
    for row in range(5):
        y_pos = 150 - (row * 30)
        for col in range(8):
            x_pos = -350 + (col * 100)
            brick = Brick((x_pos, y_pos), colors[row])
            bricks.append(brick)

# Set up keyboard controls
screen.listen()
screen.onkey(paddle.move_left, key="Left")
screen.onkey(paddle.move_right, key="Right")
screen.onkey(reset_game, key="space")  # Changed to use reset_game function

# Single game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.move()

    # Detect collision with walls
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()
    if ball.ycor() > 280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle.left_paddle) < 40 and ball.ycor() < -230:
        ball.bounce_y()
        # Sharper angle to the left
        ball.dx *= 1.5  # Increase horizontal speed
        if ball.dx > 0:  # If ball is moving right
            ball.dx *= -1  # Change direction to left
    
    elif ball.distance(paddle.right_paddle) < 40 and ball.ycor() < -230:
        ball.bounce_y()
        # Sharper angle to the right
        ball.dx *= 1.5  # Increase horizontal speed
        if ball.dx < 0:  # If ball is moving left
            ball.dx *= -1  # Change direction to right

    # Detect collision with bricks
    for brick in bricks[:]:
        if ball.distance(brick) < 40:
            brick.hideturtle()
            bricks.remove(brick)
            ball.bounce_y()
            scoreboard.score += 1
            scoreboard.clear()
            scoreboard.update_scoreboard()
            
            # Check for win condition
            if scoreboard.score >= 40:
                scoreboard.game_won()
                game_is_on = False
                screen.update()

    # Detect paddle miss
    if ball.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False
        screen.update()
        # Keep checking for space bar press even after game ends
        while not game_is_on:
            screen.update()
            if screen.getcanvas().winfo_exists():  # Check if window is still open
                continue
            else:
                break

screen.exitonclick()