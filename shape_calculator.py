class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def set_width(self, width):
        self._width = width
    def set_height(self, height):
        self._height = height
    def __str__(self):
        return f"Rectangle(width={self._width}, height={self._height})"
    def get_area(self):
        return self._width * self._height
    def get_perimeter(self):
        return (self._width *2) + (self._height *2)
    def get_diagonal(self):
        return float((self._width ** 2 + self._height ** 2) ** 0.5)

    def get_picture(self):
        if self._height <= 50 and self._width <= 50:
            pic = ''
            for i in range(self._height):
                pic += "*" * self._width + "\n"
            return pic
        else:
            return "Too big for picture."

    def get_amount_inside(self, shape):
        return ((self._width // shape._width) * (self._height // shape._height))
class Square(Rectangle):
    def __init__(self, side):
        self._side = side
        Rectangle.__init__(self, side, side)
    def __str__(self):
        return f"Square(side={self._side})"
    def set_side(self, new_side):
        self._width = new_side
        self._height = new_side
        self._side = new_side
    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)
