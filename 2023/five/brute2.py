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

import sys
process_iter = int(sys.argv[1])

mappings = [[] for i in range(7)]
seed_sources = set()

mapping_idx = -1
for line in lines:
  line = line.strip()
  if len(seed_sources) == 0:
    tmp_seeds = [int(x) for x in line.split(':')[1].strip().split(' ')]
    seed_sources.add((tmp_seeds[process_iter*2], tmp_seeds[process_iter*2+1]))
      #for i in range(tmp_seeds[1]):
      #  seed_sources.add(tmp_seeds[0] + i)
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
print(seed_sources)

def gen_next_seed_source():
  for seeds in seed_sources:
    for i in range(seeds[1]):
      yield seeds[0] + i


end_vals = []
min_val = float('inf')
# iterate each seed through all seven mappings
for idx,seed in enumerate(gen_next_seed_source()):
  current_val = seed
  for mapping_level in mappings:
    found_mapping = False
    for mapping_level_idx,mapping in enumerate(mapping_level):
      if found_mapping:
        break
      # search through each pair to find if this seed fits in any range
      destination,source,map_range = mapping
      if current_val >= source and current_val <= source+map_range:
        diff=current_val-source
        new_val = destination+diff
        current_val=new_val
        found_mapping = True
  min_val = min(min_val, current_val)
      
#print(seed_sources)
#print(mappings)
#print(end_vals)
print(f'min_val: {min_val}')