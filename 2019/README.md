# Advent of Code

## Utilities

Shameless rip off of [Peter Norvig's](https://github.com/norvig/pytudes/blob/master/ipynb/Advent-2018.ipynb) utility functions for advent of code. So far I have:

- `read_input` to read the input file every day and use a parsing function
- `integers` to cast integer looking values
- `mapt` which returns a tuple of the result of map
- `cat` which just joins on the empty string

## Profiling



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