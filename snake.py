from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.squares = []
        self.create_snake()

    # Method that create the snake
    def create_snake(self):
        for position in STARTING_POSITION:
            square = Turtle("square")
            square.color("blue")
            square.penup()
            square.goto(position)
            self.squares.append(square)

    # Method move
    def move(self):
        for square_number in range(len(self.squares) - 1, 0, -1):
            x_coordinate = self.squares[square_number - 1].xcor()
            y_coordinate = self.squares[square_number - 1].ycor()
            self.squares[square_number].goto(x_coordinate, y_coordinate)
        self.squares[0].forward(20)
