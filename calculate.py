class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Create an instance of the Rectangle class
rect = Rectangle(10, 3)

# Calculate and print the area and perimeter of the rectangle
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())

