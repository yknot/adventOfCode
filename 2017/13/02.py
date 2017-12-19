def calc_delay(inp):
    """calculate the delay"""
    end = max(inp.keys()) + 1
    delay = 0
    while True:
        found = True
        for i in range(end):
            inp_val = inp.get(i)
            if inp_val:
                if (i + delay) % inp_val == 0:
                    found = False
                    break

        if found:
            return delay
        delay += 1


ti_raw = {int(l.split(': ')[0]): (int(l.split(': ')[1]) - 1) * 2
          for l in open('testinput').read().splitlines()}
assert calc_delay(ti_raw) == 10


i_raw = {int(l.split(': ')[0]): (int(l.split(': ')[1]) - 1) * 2
         for l in open('input').read().splitlines()}
res = calc_delay(i_raw)
print(res)
assert res == 3876272
