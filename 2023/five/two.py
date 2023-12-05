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

Now I think we need to work backwards?
OR
How to test using the seeds themselves as a range?
For each RANGE. Check if that is within another range

seed 82 -> 84 -> 84 -> 84 -> 77 -> 45 -> 46 -> 46
x x x x 77x (84 still in set) 45x 46x (45 still in set) 46x (45,54 snuck in though)
45,54 <- 45,54 <- 45,54 <- 72,86 <- 79,93 <- 79,93 <- 79,93 <- 79,93
where is the problem?

WE SHOULD STOP MATCHING ONCE WE HAVE COMPLETED MATCHING THE ENTIRE RANGE (fuck)
when we match (79,98)->(81,100) with leftover (99,930) we want to
stop matching the overlapped portion this level and continue matching the leftover 99,930
but how do we know when to stop matching the leftovers?
! if the leftovers didn't match with anything this level, stop matching.

79,93 -> 79,93 + (81,95) via 52,50,48

mapping tree should be
  79,14 seed -> 81,95 soil -> 81,95 fert
->81,95 water ->  


146071405 TOO HIGH despite passing tests
104070863 TOO HIGH despite passing tests
'''

#seeds: 79 14 55 13
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
#with open(fname, 'r') as f:
#    raw_input = f.read()
lines = raw_input.strip().split('\n')

# dst1 is input. dst2 is output
# Does 79+14(93) fit within 50+48(98)? What is the OVERLAPPING range?
# max 79,50 is 79. min of 93,98 is 93. So overlap is 79-93.
# that transforms into a new range of 81-95
# what about an input range of 79-930?
#
# overlap becomes 79-98 so transform (79,98)->(81,100)
# but then we still have the leftover seeds (99,930)
# but now we have some overlap in these new mappings? It is probably fine.
# 
# produces up to three ranges
# mapped_range, pre_range, post-range
def range_in_range(instart, inend, outdst, outsrc, outrange):
  range_end = min(inend,outsrc+outrange)
  range_begin = max(instart,outsrc)
  if range_begin > range_end:
    return None, (instart, inend), None
  diff = outdst-outsrc
  result_range = (range_begin+diff, range_end+diff)

  pre_range = None
  post_range = None

  if range_begin > instart:
    pre_range = (instart, range_begin-1)
  if range_end < inend:
    post_range = (range_end+1, inend)
  return result_range, pre_range, post_range

#print(f'range test{range_in_range(79, 79+14, 52, 50, 48)}')
#print(f'range test{range_in_range(74, 77, 45, 77, 23)}') # 77,77 matches then we carryover 74-76
#quit()


mappings = [[] for i in range(7)]
seed_ranges = []

mapping_idx = -1
for line in lines:
  line = line.strip()
  if len(seed_ranges) == 0:
    tmp_seeds = [int(x) for x in line.split(':')[1].strip().split(' ')]
    print(tmp_seeds)
    for i in range(0, len(tmp_seeds), 2):
      seed_ranges.append((tmp_seeds[i], tmp_seeds[i] + tmp_seeds[i+1]))
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

print(seed_ranges)
print(mappings)
assert(len(mappings) == 7)

# At each level, build up ranges_to_eval for the next level

end_vals = []
# iterate each seed through all seven mappings
for seed_range in seed_ranges:
  ranges_to_eval = [set() for i in range(8)]
  ranges_to_eval[0].add(seed_range)
  for mapping_level_idx, mapping_level in enumerate(mappings):
    ranges_this_level = ranges_to_eval[mapping_level_idx]
    ranges_next_level = ranges_to_eval[mapping_level_idx+1]
    print(f'mapping level {mapping_level_idx} ranges to eval {ranges_this_level}')
    while len(ranges_this_level) > 0:
      current_range = ranges_this_level.pop()
      matched_this_level = False
      #unmatched_ranges = set()
      for mapping in mapping_level:
        destination,source,outrange = mapping
        found_range,pre_range,post_range = range_in_range(current_range[0], current_range[1], destination, source, outrange)
        # these carry forward to the next mapping level
        if found_range:
          print(f'creating {found_range} from {current_range} at level {mapping_level_idx} via mapping {destination}, {source}, {outrange}')
          ranges_next_level.add(found_range)
          matched_this_level = True
          if pre_range:
            print(f'adding pre_range {pre_range}')
            ranges_this_level.add(pre_range)
          if post_range:
            print(f'adding post_range {post_range}')
            ranges_this_level.add(post_range)
          #if current_range in ranges_this_level:
          #  ranges_this_level.remove(current_range)
          break
       # (79,98)->(81,100) with leftover (99,930). Get the 79,98 part out of this level.
       # We shouldn't carryover the leftover until we know it doesn't match with anything this level
       #infinite loop. (74,77)->(45,45)+(74,77) ?? 

      if not matched_this_level:
        # carryover unmatched leftovers to next level
        ranges_next_level.add(current_range)

  end_vals.append(ranges_to_eval[-1])

#print(seed_sources)
#print(mappings)
#print(end_vals)
#print(min(end_vals))


min_found = float('inf')
for end_val_set in end_vals:
  print(f'end val set {end_val_set}')
  for range in end_val_set:
    min_found = min(min_found, range[0], range[1])

print(min_found)