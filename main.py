class Rectangle():
    def __init__(self, color, width, height):
        self.color = color
        self.width = width
        self.height = height

    def display_color(self):
        print(f"Колір цього прямокутника - {self.color}, ширина - {self.width}, висота - {self.height}")

class Square(Rectangle):
    def __init__(self, color, side_length):
        super().__init__(color, width=0, height=0)
        self.width = side_length
        self.height = side_length
        self.side_length = side_length


square = Square("Green", 8)
square.display_color() # Виведе "Color: Green"
print(square.width) # Виведе 8
print(square.height) # Виведе 8
print(square.side_length) # Виведе 8