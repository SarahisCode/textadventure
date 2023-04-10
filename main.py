class Mapper:
  def __init__(self, map):
    self.map = map

  def get_room(self, coordinates):
    return self.map[coordinates]
    
class Character:
  direction_to_movement = {"north":(0,1), "south":(0,-1), "east":(1,0), "west":(-1,0)}
  
  def __init__(self):
    self.location = (0,0)

  def get_location(self):
    return self.location

  def move_direction(self, direction):
    movement = Character.direction_to_movement[direction]
    self.location = (self.location[0]+movement[0],self.location[1]+movement[1])
    return self.location

new_map = Mapper({(0,0):["bla bla bla"]})
you = Character()
def get_map():
  global new_map
  return new_map

def get_room(coordinates):
  global new_map
  return new_map.get_room(coordinates)

def get_location():
  global you
  return you.get_location()

to_direction = {"n":"north", "s":"south", "e":"east", "w":"west"}
directions = ["north", "east", "south", "west"]
def accept_direction():
  with open("inputs.txt", "r") as f:
    inputs = f.readlines()
    for answer in inputs:
      formatted_ans = answer.strip().lower()
      if formatted_ans in to_direction.keys():
        return to_direction[formatted_ans]
      elif formatted_ans in directions:
        return formatted_ans
  return "No valid direction found"

def move_character(direction):
  global you
  new_location = you.move_direction(direction)
  return new_location

  
