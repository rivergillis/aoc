'''
Now search for * and at each * search n/e/s/w/diagonals for a number
If we see a digit, expand left and right and find the whole number


CURRENT PROBLEM: when searching the directions, we might overlap.
Getting 35 from both south and southwest.

Fix? Could hardcode if we go left in south then we got southwest
81375336 INCORRECT (too low)
81463996 CORRECT
'''


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

# Expands left and right to find a number within s[start_i]. Returns None if no number exists.
# Returns num, start_i_of_num
def get_whole_number(s,start_i):
  if not s[start_i].isdigit():
    return None

  i = start_i
  # go left
  while i >= 1 and s[i-1].isdigit():
    i -= 1
  left_i = i

  # go forward and capture number
  digits = []
  while i < len(s) and s[i].isdigit():
    digits.append(s[i])
    i += 1
  
  return int(''.join(digits)), left_i

# returns gear ratio if it exists.
def consume_next_gear(line, north_line, south_line, start_i, line_num):
  # Look for all adjacents to find numbers
  # Must have found EXACTLY two numbers to be a gear ratio
  found_nums = set()

  if i > 0:
    w = get_whole_number(line, i-1)
    nw = get_whole_number(prev_line, i-1)
    sw = get_whole_number(next_line, i-1)
    if w:
      found_nums.add(w + (line_num,))
    if nw:
      found_nums.add(nw + (line_num-1,))
    if sw:
      found_nums.add(sw + (line_num+1,))
  if i < len(line)-1:
    e = get_whole_number(line, i+1)
    ne = get_whole_number(prev_line, i+1)
    se = get_whole_number(next_line, i+1)
    if e:
      found_nums.add(e + (line_num,))
    if ne:
      found_nums.add(ne + (line_num-1,))
    if se:
      found_nums.add(se + (line_num+1,))
  n = get_whole_number(prev_line, i)
  s = get_whole_number(next_line, i)
  if n:
    found_nums.add(n + (line_num-1,))
  if s:
    found_nums.add(s + (line_num+1,))
  
  print(f'found these {found_nums}')
  if len(found_nums) == 2:
    tot = 1
    for n in found_nums:
      tot *= n[0]
    return tot
  return None

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
    if line[i] != '*':
      i += 1
      continue
    found_num = consume_next_gear(line, prev_line, next_line, i, j)
    print(f'found_num is {found_num}')
    if found_num:
      total += found_num
    i+=1


print(total)