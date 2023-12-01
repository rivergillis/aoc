'''
For each line, get the first and last digit and combine them. That's the number
Ex

1abc2         --> 1 (first) and 2 (last) is 12
pqr3stu8vwx   --> 3 and 8 is 38
a1b2c3d4e5f   --> 1 and 5 is 15
treb7uchet    --> 7 is both first and last, so 77
'''

raw_input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

with open('one.input', 'r') as f:
    raw_input = f.read()

lines = raw_input.split('\n')

def get_number(line):
  first_digit = None
  last_digit = None
  for c in line:
    if c.isdigit():
      if first_digit == None:
        first_digit = c
      else:
        last_digit = c
  if last_digit is None:
    last_digit = first_digit
  
  return int(first_digit) * 10 + int(last_digit)


numbers = [get_number(line) for line in lines]
print(sum(numbers))