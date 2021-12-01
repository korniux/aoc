def main():
  file = open('1/in.txt', 'r')
  lines = [int(i) for i in file.readlines()]
  file.close()

  triads = [sum(lines[i:i+3]) for i, _ in enumerate(lines)]

  def calc(list_in):
    is_inc = [i != 0 and val > list_in[i - 1] for i, val in enumerate(list_in)]
    return is_inc.count(True)

  print('Part 1: {}'.format(calc(lines)))
  print('Part 2: {}'.format(calc(triads)))

main()
