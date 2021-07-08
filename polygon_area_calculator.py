
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width},height={self.height})"

    def set_height(self, height):
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width * 2) + (self.height * 2)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture"
        string = ""
        for row in range(self.height):
            for col in range(self.width):
                string += "*"
            string += "\n"
        return string
    
    def get_amount_inside(self, instance):
        num_in_height = self.height // instance.height
        num_in_width = self.width // instance.width
        total = num_in_width + num_in_height
        if num_in_height == 0 or num_in_width == 0:
            return 0
        return total - 1



class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        self.side = length
        self.height = length
        self.width = length

    def __str__(self):
        return f"Square(side={self.side})"

    def set_height(self, height):
        Rectangle.height = height
        Rectangle.width = height
    
    def set_width(self, width):
        Rectangle.width = width
        Rectangle.height = width
    
    def get_area(self):
        return self.side ** 2

    def get_perimeter(self):
        return (self.side * 4)

    def get_diagonal(self):
        return (self.side ** 2 + self.side ** 2) ** 0.5
    
    def set_side(self, side):
        self.side = side

    def get_picture(self):
        if self.side > 50:
            return "Too big for picture"
        string = ""
        for row in range(self.side):
            for col in range(self.side):
                string += "*"
            string += "\n"
        return string
    
    def get_amount_inside(self, instance):
        num_in_height = self.side // instance.height
        num_in_width = self.side // instance.width
        total = num_in_width + num_in_height
        if num_in_height == 0 or num_in_width == 0:
            return 0
        return total - 1


