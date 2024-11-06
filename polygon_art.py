# turtle_graphics_oo
import turtle
import random

turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)
reduction_ratio = 0.618

choice = int(input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: "))


class Drawing:
    def __init__(self,choice):
        self.choice = choice
        self.num_sides = self._generate_num_sides()
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.border_size = random.randint(1,5)

    def _generate_num_sides(self):
        if 1 <= self.choice <= 3:
            return self.choice + 2
        elif self.choice in (4, 8, 9):
            return random.randint(3, 5)
        else:
            return self.choice - 2

    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        turtle.penup()

    def relocate(self):
        turtle.forward(self.size * (1 - reduction_ratio) / 2)
        turtle.left(90)
        turtle.forward(self.size * (1 - reduction_ratio) / 2)
        turtle.right(90)
        self.location[0], self.location[1] = turtle.pos()

    def draw(self):
        if self.choice in (1,2,3,4):
            for _ in range(1):
                self.draw_polygon()
                self.relocate()
                self.size *= reduction_ratio
        else:
            for _ in range(self.num_sides):
                self.draw_polygon()
                self.relocate()
                self.size *= reduction_ratio

# Create multiple drawings with different parameters
for _ in range(20):
    drawing = Drawing(choice)
    drawing.draw()


# Keep the window open until closed manually
turtle.done()