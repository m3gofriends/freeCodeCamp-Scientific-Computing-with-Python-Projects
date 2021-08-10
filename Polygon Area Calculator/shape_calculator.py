class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height="+ str(self.height) + ")"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if(self.width > 50 or self.height > 50):
            return "Too big for picture."
        string = ""
        for i in range(self.height):
            for j in range(self.width):
                string += '*'
            string += '\n'
        return string

    def get_amount_inside(self, another_shape):
        return self.get_area() // another_shape.get_area()
            
class Square(Rectangle):

    def __init__(self, length):
        self.length = length

    def __str__(self):
        return "Square(side=" + str(self.length) + ")"

    def set_side(self, length):
        self.length = length

    def set_width(self, length):
        self.length = length

    def set_height(self, length):
        self.length = length

    def get_area(self):
        return self.length ** 2

    def get_perimeter(self):
        return 4 * self.length

    def get_diagonal(self):
        return (2 * self.length ** 2) ** 0.5

    def get_picture(self):
        if(self.length > 50):
            return "Too big for picture."
        string = ""
        for i in range(self.length):
            for j in range(self.length):
                string += '*'
            string += '\n'
        return string
