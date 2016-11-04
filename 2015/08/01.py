
# part 1
print sum(len(s.strip()) - len(eval(s)) for s in open('input'))


