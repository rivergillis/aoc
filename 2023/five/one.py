'''
Convert the seeds through every single mapping
First parse to get a list of mappings.
Will always have 7 mappings + initial set of sources

mappings = list(dict) where len(mappings)=7

18 25 70
input 81 output should be 74.
81-25=56. 18+56=74.
mapping 74 against mapping level [[45, 77, 23], [81, 45, 19], [68, 64, 13]] should yield 78
64+13=77
'''

raw_input = '''
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
'''

import os
fname = 'input'
if os.path.isfile('input2'):
  fname = 'input2'
with open(fname, 'r') as f:
    raw_input = f.read()
lines = raw_input.strip().split('\n')

mappings = [[] for i in range(7)]
seed_sources = []

mapping_idx = -1
for line in lines:
  line = line.strip()
  if len(seed_sources) == 0:
    seed_sources = [int(x) for x in line.split(':')[1].strip().split(' ')]
    continue
  # now find the mappings
  if len(line) == 0:
    continue
  if not line[0].isdigit():
    mapping_idx += 1
    continue
  
  # Now create the mapping and don't expand it
  mapping = [int(x) for x in line.split(' ')]
  mappings[mapping_idx].append(mapping)

assert(len(mappings) == 7)

for mapping_level in mappings:
  print(mapping_level)

end_vals = []
# iterate each seed through all seven mappings
for seed in seed_sources:
  print(f'seed {seed}')
  current_val = seed
  for mapping_level in mappings:
    found_mapping = False
    print(f'mapping {current_val} against mapping level {mapping_level}')
    for mapping in mapping_level:
      if found_mapping:
        break
      # search through each pair to find if this seed fits in any range
      destination,source,range = mapping
      if current_val >= source and current_val <= source+range:
        diff=current_val-source
        print(f'converting {current_val} to {destination+diff} via mapping {mapping}')
        current_val=destination+diff
        found_mapping = True
  end_vals.append(current_val)
      
  
#print(seed_sources)
#print(mappings)
print(end_vals)
print(min(end_vals))