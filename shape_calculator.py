class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.height * self.width
  
  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    rectangle = ""
    if self.height > 50 or self.width > 50:
      return "Too big for picture."
    for row in range(self.height):
      if row == self.height:
        rectangle =  rectangle + "*" * self.width
      else:
        rectangle =  rectangle + "*" * self.width + "\n"
    
    return rectangle

  def get_amount_inside(self, other):
    return self.get_area() // other.get_area()

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"
      

class Square(Rectangle):
  def __init__(self, side):
    super(Square,self).__init__(side, side)

  def set_side(self, side):
    self.width = side
    self.height = side

  def __str__(self):
    return f"Square(side={self.width})"

