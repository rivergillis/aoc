'''
Sum all of the numbers that are adjacent (n/e/s/w and diagonally)
to a symbol. Symbols are anything that isn't a number or a .
In example: 114 and 58 are the only exclusions.

So iterate and consume lines, checking the above and below line.
'''

import re

raw_input = '''
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
'''

with open('input', 'r') as f:
    raw_input = f.read()

lines = [line.strip() for line in raw_input.strip().split('\n')]

def is_symbol(c):
  return (not c.isdigit()) and c != '.'


# returns i for first character after number, number if valid
def consume_next_number(line, north_line, south_line, start_i):
  valid = False

  i = start_i
  digits = []
  while i < len(line) and line[i].isdigit():
    digits.append(line[i])

    # check validity
    if i > 0:
      if is_symbol(line[i-1]):
        valid = True
      if is_symbol(prev_line[i-1]):
        valid = True
      if is_symbol(next_line[i-1]):
        valid = True
    if i < len(line)-1:
      if is_symbol(line[i+1]):
        valid = True
      if is_symbol(prev_line[i+1]):
        valid = True
      if is_symbol(next_line[i+1]):
        valid = True
    if is_symbol(prev_line[i]) or is_symbol(next_line[i]):
      valid = True

    i += 1

  num_val = int(''.join(digits))
  if not valid:
    num_val = None
  return i, num_val

total = 0
for j,line in enumerate(lines):
  # fake padding
  prev_line = '.' * len(line)
  next_line = '.' * len(line)
  if j > 0:
    prev_line = lines[j-1]
  if j < len(lines) - 1:
    next_line = lines[j+1]
  
  i = 0
  while i < len(line):
    # find the start of the next number
    if not line[i].isdigit():
      i += 1
      continue
    # start of number
    i, found_num = consume_next_number(line, prev_line, next_line, i)
    if found_num:
      total += found_num


print(total)