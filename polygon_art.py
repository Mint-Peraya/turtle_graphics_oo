# turtle_graphics_oo
import turtle
import random


class Polygon:
    def __init__(self,num_sides, size, orientation, location, color, border_size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size

    def draw(self):
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

    def move(self):
        turtle.forward(self.size * (1 - reduction_ratio) / 2)
        turtle.left(90)
        turtle.forward(self.size * (1 - reduction_ratio) / 2)
        turtle.right(90)
        self.location[0], self.location[1] = turtle.pos()


class PolygonArt:
    def __init__(self):
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)

    def setup(self,choice):
        if 1 <= choice <= 3:
            num_sides = choice + 2
        elif choice in (4, 8, 9):
            num_sides = random.randint(3, 5)
        else:
            num_sides = choice - 2
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        border_size = random.randint(1, 5)
        art = Polygon(num_sides, size, orientation, location, color, border_size)
        return art

    def em_setup(self,choice):
        if 1 <= choice <= 3:
            num_sides = choice + 2
        elif choice in (4, 8, 9):
            num_sides = random.randint(3, 5)
        else:
            num_sides = choice - 2
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        border_size = random.randint(1, 5)
        art = EmbeddedPolygon(num_sides, size, orientation, location, color, border_size)
        return art

    def run(self):
        choice = int(input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: "))
        if choice in (1,2,3,4):
            for i in range(20):
                art = self.setup(choice)
                art.draw()
        elif choice == 9:
            num_sides = random.randint(3, 5)
            for i in range(20):
                for j in range(num_sides):
                    art = self.em_setup(choice)
                    art.draw()
        else:
            for i in range(20):
                art = self.em_setup(choice)
                art.draw()


class EmbeddedPolygon(Polygon):
    def __init__(self, num_sides, size, orientation, location, color, border_size, level = 5):
        super().__init__(num_sides, size, orientation, location, color, border_size)
        self.level = level

    def draw(self):
        self.level = random.randint(1, 5)
        while self.level > 0:
            super().draw()
            super().move()
            self.size *= reduction_ratio
            super().draw()
            self.level -= 1
            self.location[0], self.location[1] = turtle.pos()
        self.location[0] += self.size * (1 - reduction_ratio) / 2
        self.location[1] += self.size * (1 - reduction_ratio) / 2


reduction_ratio = 0.618
run = PolygonArt()
run.run()
turtle.done()
