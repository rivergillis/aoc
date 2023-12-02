'''
Bag has 12 red, 13 green, and 14 blue. Determine which games are possible.
After each game (; delim) the cubes are put back into the bag

Now figure out the max totals per game. This'll be the largest amount of cubes
in individual showings, but you need to account for this globally

So if we have 3b5r1g; 5b3r1g the maxes are 5b5r1g
'''

import re

raw_input = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''

with open('input', 'r') as f:
    raw_input = f.read()

# reads the next number in a string and returns it.
def read_next_number(s):
  return int(re.search('\d+', s).group())

total = 0
lines = raw_input.split('\n')
for i,line in enumerate(lines):
  game_id = i+1
  showings = line.split(':')[1].split(';')
  red_max = 0
  blue_max = 0
  green_max = 0
  for showing in showings:
    print(showing)
    red_total = 0
    blue_total = 0
    green_total = 0
    colors = [color.strip() for color in showing.split(',')]
    for color in colors:
      print(color)
      num = read_next_number(color)
      color_string = color.split(' ')[1]
      if color_string == 'green':
        green_total += num
      elif color_string == 'blue':
        blue_total += num
      else:
        red_total += num
      red_max = max(red_max, red_total)
      blue_max = max(blue_max, blue_total)
      green_max = max(green_max, green_total)
  total += red_max * green_max * blue_max

print(total)
