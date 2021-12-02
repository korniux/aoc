from readers import read_int

def calc(list_in):
    is_inc = [i != 0 and val > list_in[i - 1] for i, val in enumerate(list_in)]
    return is_inc.count(True)

def part1():
  lines = read_int('1.txt')
  return calc(lines)
  

def part2():
  lines = read_int('1.txt')
  triads = [sum(lines[i:i+3]) for i, _ in enumerate(lines)]
  return calc(triads)

print('Part 1: {}'.format(part1()))
print('Part 2: {}'.format(part2()))
