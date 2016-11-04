import json

data = json.loads(open('input').read())


def goDeeper(data):
    total = 0
    if type(data) == list:
        for d in data:
            total += goDeeper(d)
    elif type(data) == dict:
        for d in data.keys():
            total += goDeeper(data[d])
    elif type(data) == int:
        return data
    elif type(data) == unicode:
        return 0
    else:
        print type(data)

    return total


total = goDeeper(data)

print total


