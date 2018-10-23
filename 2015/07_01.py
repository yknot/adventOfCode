import numpy as np

class op():
    def __init__(self, inVal, outVal):
        self.outVal = outVal
        if len(inVal) == 1:
            self.operation = 'NONE'
            self.rside = self.tryInt(inVal[0])
        elif len(inVal) == 2:
            self.operation = inVal[0]
            self.rside = self.tryInt(inVal[1])
        elif len(inVal) == 3:
            self.operation = inVal[1]
            self.lside = self.tryInt(inVal[0])
            self.rside = self.tryInt(inVal[2])

    def tryInt(self, value):
        try:
            return np.uint16(value)
        except:
            return value

    def canGetVal(self, wires):
        if self.operation == 'NONE' or self.operation == 'NOT':
            return self.rside in wires or isinstance(self.rside, np.uint16)
        else:
            return (self.rside in wires or isinstance(self.rside, np.uint16)) \
                and (self.lside in wires or isinstance(self.lside, np.uint16))
        return False

    def getSideVal(self, side, wires):
        if isinstance(side, np.uint16):
            return side
        else:
            return wires[side]

    def getVal(self, wires):
        if self.operation == 'NONE':
            wires[self.outVal] = self.getSideVal(self.rside, wires)
        elif self.operation == 'NOT':
            wires[self.outVal] = ~ self.getSideVal(self.rside, wires)
        elif self.operation == 'AND':
            wires[self.outVal] = self.getSideVal(self.lside, wires) & self.getSideVal(self.rside, wires)
        elif self.operation == 'OR':
            wires[self.outVal] = self.getSideVal(self.lside, wires) | self.getSideVal(self.rside, wires)
        elif self.operation == 'LSHIFT':
            wires[self.outVal] = self.getSideVal(self.lside, wires) << self.getSideVal(self.rside, wires)
        elif self.operation == 'RSHIFT':
            wires[self.outVal] = self.getSideVal(self.lside, wires) >> self.getSideVal(self.rside, wires)



cmds = open('input2').readlines()
cmds = [c.strip() for c in cmds]
cmds = [c.split('->') for c in cmds]

wires = {}
operations = []
for cmd in cmds:
    operations.append(op(cmd[0].strip().split(), cmd[1].strip()))

while len(operations) > 0:
    canDo = [o for o in operations if o.canGetVal(wires)]
    operations = [o for o in operations if not o.canGetVal(wires)]
    for c in canDo:
        c.getVal(wires)

    


for key, value in sorted(wires.items()):
    print key + ': ' + str(value)
