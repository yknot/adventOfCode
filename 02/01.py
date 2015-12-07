dims = open('input').readlines()

dimensions = [sorted([int(d) for d in dim.strip().split('x')]) for dim in dims]

total = 0
ribbon = 0
for d in dimensions:
    total += 3*d[0]*d[1] + 2*d[1]*d[2] + 2*d[0]*d[2]
    ribbon += 2*d[0] + 2*d[1] + d[0]*d[1]*d[2]

print 'Total paper:', total
print 'Total ribbon:', ribbon
