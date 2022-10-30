rooms = {}

def create_map():
  for room_string in open("map.txt").readlines():
    coords, room = create_room(room_string)
    rooms[coords] = room
  return rooms

templates = {"holding cell":{"message":"You are in a holding cell. You don't see anything useful","type":"empty"}}
def create_room(room_string):
  room_coords_string = room_string.split(":")[0]
  room_coordinates = tuple(map(int,room_coords_string.split(",")))
  room_attributes = room_string.strip().split(":")[1].split(",")
  room = {}
  room["message"] = room_attributes[0]
  room["type"] = room_attributes[1]
  if room.get("type") in ["armor", "defense", "weapon", "item"]:
    room["item"] = room_attributes[2]
    room["strength"] = int(room_attributes[3])
  elif room.get("type") == "enemy":
    stats_string = room_attributes[2]
    enemy_stats = [int(i) for i in stats_string.split(" ")]
    room["stats"] = enemy_stats
  return room_coordinates, room