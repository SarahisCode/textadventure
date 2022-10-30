from combat import simulate_combat
from mapper import create_map
#from door_factory import encounter_door

rooms = create_map()
valid_locations = rooms.keys()

class DataError(Exception):
  pass

class BrokenFunctionError(Exception):
  pass

directions = ["north","south","east","west"]
class RoomLocation:

  def __init__(self, coordinates):
    self.coordinates = coordinates

  def get_coordinates(self):
    return self.coordinates
  
  def get_room(self):
    return rooms[(self.coordinates)]

  def clear_room(self):
    new_dict = {}
    new_dict["message"] = room["message"]
    new_dict["type"] = "empty"
    rooms[self.coordinates] = new_dict

def move_using_input():
  moved = False
  while not moved:
    direction = get_direction()
    moved = attempt_move(direction)
  

def attempt_move(direction):
  full_direction = expand(direction)
  if full_direction:
    new_location = find_new_location(full_direction)
    if wall_at(new_location):
      print("You ran into a wall")
      return False
    else:
      move_to(new_location)
      return True
  else:
    print("That direction is invalid")
    return False

def get_direction():
  new_direction = input("Which way do you want to move?(North, east, south, west) ").lower()
  return new_direction

abbreviations = [lambda x:x,lambda x:x[0]]#I know that the direction itself isn't really an abbreviation, but it's nice and convenient, so whatever
def expand(direction):
  for valid_direction in directions:
    for abbrev_func in abbreviations:
      if abbrev_func(valid_direction) == direction:
        return valid_direction
  return False

def wall_at(coordinates):
  return coordinates not in valid_locations

def find_new_location(direction):
  current_location = player_location.get_coordinates()
  move_delta = find_movement(direction)
  new_location = apply_movement(move_delta,current_location)
  return new_location

move_deltas = {"north":[0,1],"south":[0,-1],"east":[1,0],"west":[-1,0]}
def find_movement(direction):
  move_delta = move_deltas[direction]
  return move_delta

def apply_movement(move_map, curr_location):
  new_location = list(curr_location)
  for index,change in enumerate(move_map):
    new_location[index] += change
  return tuple(new_location)

def move_to(new_location):
  global player_location
  player_location = RoomLocation(new_location)

def pick_up_item(item_dict, room):
  item_dict[room["item"]] = room["strength"]
  print("You picked up a", room["item"], "with a strength of", room["strength"])


def char_is_dead(life):
  return life == 0


player_location = RoomLocation((3,3))

life = 100
weapons = {"fist":1}
armor = {"clothes":1}
defense = {"wood":1}
inventory = {}

print('''Prologue: You have been captured by aliens and are currently being held in their spaceship as the aliens work out a ransom for your release. 
You notice a map on the wall. You can't read any of it except for "escape pod", which is in 17 different languages, and one of them is English. 
The aliens forgot to post guards, so you can sneak around.''')

while True:
  room = player_location.get_room()
  room_type = room.get("type")

  print(room.get("message",""))

  if(room_type in ["weapon", "armor", "defense"]):

    if(room_type == "weapon"):
      important_items = weapons
    elif(room_type == "armor"):
      important_items = armor
    elif(room_type == "defense"):
      important_items = defense
    
    important_items = pick_up_item(important_items, room)

  elif(room_type == "enemy"):
    best_damage = max(weapons.values())
    best_armor = max(armor.values())
    best_defense = max(defense.values())

    new_life = simulate_combat(room["stats"], best_damage, life, best_armor, best_defense)
    if(char_is_dead(new_life)):
      break
    else:
      life = new_life
      
  elif(room_type == "item"):
    inventory = pick_up_item(inventory, room)
  elif(room_type == "exit"):
    #find_locked_door()
    #TODO: make the escape pod door locked
    break
  elif(room_type == "empty"):
    pass
  else:
    raise DataError("Room type is invalid")
  player_location.clear_room()
  
  use = ""
  #for later use
  if(use != ""):
    for item in inventory.keys():
      if(item == use.split(" ")[0] and inventory[item] == use.split(" ")[1]):
        if(item == "health potion"):
          prevlife = life
          life += int(inventory[item])
          if(life > 100):
            life = 100
          print("You healed", life-prevlife, "health")
  move_using_input()
print("Thanks for playing!")
