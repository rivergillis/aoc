'''
For each line, get the first and last digit and combine them. That's the number
Ex

two1nine          -> 29
eightwothree      -> 83
abcone2threexyz   -> 13
xtwone3four       -> 24
4nineeightseven2  -> 42
zoneight234       -> 14
7pqrstsixteen     -> 76

ans 281

So, same as the last answer just search for the 10 hardcoded strings too

54185 is incorrect?? Test cases pass
PROBLEM IS OVERLAP: zoneight234. 'one' and 'eight' are valid but we dont check eight
So need to start checking at every index. Even if we get a digit back, must only return i+1
'''

raw_input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

stringmap = {'one': 1,
             'two': 2,
             'three': 3,
             'four': 4,
             'five': 5,
             'six': 6,
             'seven': 7,
             'eight': 8,
             'nine': 9}

with open('one.input', 'r') as f:
    raw_input = f.read()

lines = raw_input.split('\n')

# returns digit,i for first i after the number. If no number, digit is None
def read_digit(line, start_i):
  if line[start_i].isdigit():
    return int(line[start_i]), start_i+1
  
  remaining_len = len(line) - start_i
  
  for matcher,val in stringmap.items():
    if len(matcher) > remaining_len:
      continue
    if line[start_i:start_i+len(matcher)] == matcher:
      return val, start_i+1
  
  return None, start_i + 1

def get_number(line):
  if line == '':
    return
  first_digit = None
  last_digit = None

  i = 0
  while i < len(line):
    digit, i = read_digit(line, i)
    if digit is None:
      continue
    if first_digit == None:
      first_digit = digit
    else:
      last_digit = digit
  if last_digit is None:
    last_digit = first_digit

  return first_digit * 10 + last_digit


numbers = [get_number(line) for line in lines if line != '']
print(sum(numbers))