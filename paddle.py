from turtle import Turtle

class Paddle:
    def __init__(self, position):
        # Create left half of paddle
        self.left_paddle = Turtle()
        self.left_paddle.shape("square")
        self.left_paddle.color("green")
        self.left_paddle.shapesize(stretch_wid=1, stretch_len=4)
        self.left_paddle.penup()
        self.left_paddle.goto(position[0] - 40, position[1])  # Offset to the left
        
        # Create right half of paddle
        self.right_paddle = Turtle()
        self.right_paddle.shape("square")
        self.right_paddle.color("green")
        self.right_paddle.shapesize(stretch_wid=1, stretch_len=4)
        self.right_paddle.penup()
        self.right_paddle.goto(position[0] + 40, position[1])  # Offset to the right
    
    def move_left(self):
        if self.left_paddle.xcor() > -350:
            self.left_paddle.setx(self.left_paddle.xcor() - 60)
            self.right_paddle.setx(self.right_paddle.xcor() - 60)
    
    def move_right(self):
        if self.right_paddle.xcor() < 350:
            self.left_paddle.setx(self.left_paddle.xcor() + 60)
            self.right_paddle.setx(self.right_paddle.xcor() + 60)

    def goto(self, x, y):
        self.left_paddle.goto(x - 40, y)
        self.right_paddle.goto(x + 40, y)
