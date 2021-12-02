def read_int(f):
  file = open(f, 'r')
  result = [int(i) for i in file.readlines()]
  file.close()
  return result

def read_arr(f):
  file = open(f, 'r')
  result = [l.strip().split() for l in file.readlines()]
  file.close()
  return result
