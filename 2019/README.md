# Advent of Code

## Utilities

Shameless rip off of [Peter Norvig's](https://github.com/norvig/pytudes/blob/master/ipynb/Advent-2018.ipynb) utility functions for advent of code. So far I have:

- `read_input` to read the input file every day and use a parsing function
- `integers` to cast integer looking values
- `mapt` which returns a tuple of the result of map
- `cat` which just joins on the empty string

## Profiling

To load the extension in iPython enabling the line profiler library first run this magic command `%load_ext line_profiler`.
Then to run the profiler we use the command `%lprun -f fcn_name fcn_name(args)`.
This will return results per line with number of hits, the total time, time per hit, and percentage of the time. This can help identify bottlenecks in your code.

```
Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    15                                           def find_pwd(low, high):
    16         1          9.0      9.0      0.0      count = 0
    17         1          1.0      1.0      0.0      i = low
    18       899        722.0      0.8      2.1      while i < high:
    19       898       1132.0      1.3      3.3          tmp_str = str(i)
    20                                                   # dummy check to skip hundreds of values
    21      4817       4816.0      1.0     14.1          for j in range(5):
    22      4236       7162.0      1.7     21.0              if int(tmp_str[j]) > int(tmp_str[j + 1]):
    23       317        644.0      2.0      1.9                  i = int(tmp_str[:j] + (tmp_str[j] * (6 - j)))
    24       317        316.0      1.0      0.9                  break
    25       898       1140.0      1.3      3.3          if str(i) != tmp_str:
    26       317        226.0      0.7      0.7              continue
    27
```



## Day 4

### Part 1

#### Optimizations

- Trivial brute force solution takes 1.72s and 490,000 loops

```
def find_pwd(low, high):
    count = 0
    i = low
    while i < high:
        tmp_str = str(i)
    
        # check if two adjacent numbers
        if not any([1 if a == b else 0 for a, b in zip(tmp_str, tmp_str[1:])]):
            i += 1
            continue

        # check if increasing
        if any([1 if int(a) > int(b) else 0 for a, b in zip(tmp_str, tmp_str[1:])]):
            i += 1
            continue
            
        count += 1
        i += 1

    return count
```

- Skip every 10k 0.737s and 200,000 loops

```
        if int(tmp_str[0]) > int(tmp_str[1]):
            i = int(tmp_str[0] * 6)
            continue
```
 - Apply all the way down 0.00675s and 900 loops
 
```
        for j in range(5):
            if int(tmp_str[j]) > int(tmp_str[j + 1]):
                i = int(tmp_str[:j] + (tmp_str[j] * (6 - j)))
                break
        if str(i) != tmp_str:
            continue
```