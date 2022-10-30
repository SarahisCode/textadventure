from time import sleep


def simulate_combat(enemy_stats, player_attack, player_life, armor, defense):
  print("You have encountered an alien")
  start_life = player_life
  total_life = player_life + armor
  enemy_attack, current_enemy_life = enemy_stats
  enemy_does_damage = enemy_attack - defense
  while True:
    player_life = take_turn("The alien", "You", player_life, enemy_does_damage)
    if(player_life == 0):
      return 0
    wait()
    current_enemy_life = take_turn("You", "The alien", current_enemy_life, player_attack)
    if(current_enemy_life == 0):
      return min(start_life, total_life)
    wait()


def take_turn(attacker, defender, defender_life, attacker_damage):
  new_defender_life = update_life(defender_life, attacker_damage)
  if defender == "You":
    word = "have"
  else:
    word = "has"
  print(attacker, "did", attacker_damage, "damage.", defender, word, new_defender_life, "life left")
  if new_defender_life == 0:
    print_dead(defender)
    return 0
  return new_defender_life


def print_dead(entity):
  if entity == "The alien":
    print("The alien died")
  elif entity == "You":
    print("You died :(")
  else:
    print("Invalid entity")


def update_life(life, damage):
  new_life = life-damage
  if new_life < 0:
    new_life = 0
  return new_life


def wait():
  sleep(0.5)