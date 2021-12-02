from readers import read_arr
import numpy

def part1():
  lines = read_arr('2.txt')
  coords = [0, 0]
  
  for d, v in lines:
    axis = int(d in ['up', 'down'])
    coords[axis] += int('-{}'.format(v) if d == 'up' else v)
  
  return numpy.prod(coords)

def part2():
  lines = read_arr('2.txt')
  coords = [0, 0, 0] # h, a, d

  for d, v in lines:
    if d == 'forward':
      coords[0] += int(v)
      coords[2] += coords[1] * int(v)
    else:
      coords[1] += int('-{}'.format(v) if d == 'up' else v)
    
  return coords[0] * coords[2]

print('Part 1: {}'.format(part1()))
print('Part 2: {}'.format(part2()))
