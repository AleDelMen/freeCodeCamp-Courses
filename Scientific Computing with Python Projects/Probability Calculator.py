import copy
import random

#This code is for a class called Hat, which represents a hat with a certain number of balls in it. 
class Hat:
  #The __init__ method initializes the hat with a certain number of balls of different colors. 
  def __init__(self, **kwargs):
    self.contents = []
    for k, v in kwargs.items():
      self.contents += v * [k]

  #The draw method randomly draws a certain number of balls from the hat.
  def draw(self, num):
    try:
      balls = random.sample(self.contents, num)
    except:
      balls = copy.deepcopy(self.contents)

    for ball in balls:
      self.contents.remove(ball)

    return balls

#The experiment function runs a simulation to see how often the expected balls are drawn.
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0
  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    balls = hat_copy.draw(num_balls_drawn)

    eb_list = []
    for k, v in expected_balls.items():
      eb_list += v * [k]

    if contains_balls(eb_list, balls):
      M += 1

  probability = M / num_experiments
  return probability

#The contains_balls function checks to see if the expected balls are in the list of actual balls
def contains_balls(exptected_balls, actual_balls):
  for b in exptected_balls:
    if b in actual_balls:
      actual_balls.remove(b)
    else:
      return False
  return True

hat1 = Hat(yellow=3, blue=2, green=6)
print(hat1.contents)
hat2 = Hat(red=5, orange=4)
print(hat2.contents)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
print(hat3.contents)

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)
