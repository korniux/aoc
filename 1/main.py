def main():
  file = open('1/in.txt', 'r')
  lines = file.readlines()
  file.close()

  result = 0
  for i, val in enumerate(lines):
    isIncreased = i != 0 and int(val) > int(lines[i - 1])
    if isIncreased:
      result += 1
  
  print(result)

main()
