from collections import defaultdict
import sys


class Queuer(object):
    def __init__(self):
        self.q_0 = []
        self.q_1 = []

        self.w_0 = False
        self.w_1 = False

        self.total = 0

    def add(self, val, pid):
        """add to opposite queue"""
        if pid == 0:
            self.q_1.append(val)
        else:
            self.total += 1
            self.q_0.append(val)

    def get(self, pid):
        """get from opposite queue if possible"""
        # checks if deadlocked
        if self.w_0 and self.w_1:
            print(self.total)
            sys.exit()

        if pid == 0:
            if len(self.q_0):
                self.w_0 = False
                return self.q_0.pop(0)
            else:
                self.w_0 = True
                return None
        else:
            if len(self.q_1):
                self.w_1 = False
                return self.q_1.pop(0)
            else:
                self.w_1 = True
                return None


class Prog(object):
    def __init__(self, lines, qer, pid):
        """initalize"""
        self.regs = defaultdict(int)
        self.regs['p'] = pid
        self.idx = 0
        self.lines = lines
        self.qer = qer
        self.pid = pid

    def cast(self, val):
        """if int return int else return char"""
        try:
            return int(val)
        except ValueError as ve:
            return self.regs[val]

    def run_cmd(self):
        """run a command"""
        try:
            cmd, x, y = self.lines[self.idx].split()
        except ValueError as ve:
            cmd, x = self.lines[self.idx].split()

        if cmd == 'snd':            # play sound of freq X
            self.qer.add(self.cast(x), self.pid)
        elif cmd == 'set':          # set reg X to val Y
            self.regs[x] = self.cast(y)
        elif cmd == 'add':          # increase reg X by val Y
            self.regs[x] = self.regs[x] + self.cast(y)
        elif cmd == 'mul':          # set reg X to X * Y
            self.regs[x] = self.regs[x] * self.cast(y)
        elif cmd == 'mod':          # set reg X to X mod Y
            self.regs[x] = self.regs[x] % self.cast(y)
        elif cmd == 'rcv':          # recover freq of last sound played if X != 0
            res = self.qer.get(self.pid)
            if res is None:
                return
            self.regs[x] = res
        elif cmd == 'jgz':          # jumps by Y if X > 0
            if self.cast(x) > 0:
                self.idx += self.cast(y)
                return

        self.idx += 1


raw = open('input').read().splitlines()
q = Queuer()
pid_0 = Prog(raw, q, 0)
pid_1 = Prog(raw, q, 1)

while True:
    pid_0.run_cmd()
    pid_1.run_cmd()
