class Rectangle: 
  #The __init__ method takes in a width and height, and sets the corresponding attributes. 
  def __init__(self, width, height):
    self.height = height
    self.width = width

  #The __repr__ method returns a string representation of the object. 
  def __repr__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

  #The set_width and set_height methods set the width and height attributes, respectively. 
  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height
  
  #The get_area method returns the area of the Rectangle.
  def get_area(self):
    return self.height * self.width
  
  #The get_perimeter method returns the perimeter.
  def get_perimeter(self):
    return 2* (self.height + self.width)

  #The get_diagonal method returns the diagonal of the Rectangle. 
  def get_diagonal(self):
    return (self.width**2 + self.height**2)**0.5

  #The get_picture method returns a string representation of the Rectangle using asterisks, 
  #but only if the width and height are both less than or equal to 50. 
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    string = ""
    for i in range(self.height):
      string += "*" * self.width + "\n"
    return string

  #The get_amount_inside method returns the number of times a given shape can fit inside the Rectangle. 
  def get_amount_inside(self, shape):
    return  self.get_area() // shape.get_area()

#The Square class inherits from the Rectangle class, and overrides the 
# __init__, __repr__, set_width, set_height, and set_side methods.
class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)

  def __repr__(self):
    return f"Square(side={self.width})"


  def set_side(self, side):
    self.width = side
    self.height = side

  def set_width(self, side):
    self.set_side(side)

  def set_height(self, side):
        self.set_side(side)

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

'''
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8
'''
