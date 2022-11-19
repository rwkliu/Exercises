# Given a string path, where path[i] = 'N', 'S', 'E' or 'W',
# each representing moving one unit north, south, east, or west, respectively. 
# You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.
# Return true if the path crosses itself at any point, false otherwise.

def update_position(direction, position):
  if direction == "N":
    position[1] += 1
  elif direction == "S":
    position[1] -= 1
  elif direction == "E":
    position[0] += 1
  elif direction == "W":
    position[0] -= 1
  return position

def path_cross(input):
  positions = [[0,0]]

  for direction in input:
    pos = positions[len(positions)-1].copy()
    update_position(direction, pos)
    if pos in positions:
      return False
    positions.append(pos)
    
  return True

if __name__ == "__main__":
  print(path_cross("NES"))
  print(path_cross("NESWW"))