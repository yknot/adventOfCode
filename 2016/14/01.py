from hashlib import md5

def match_in_a_row(s, n=5, c=None):
    """find n characters in a string s that equal c"""
    for i, v in enumerate(s[:-(n - 1)]):
        if v != c:
            continue
        if all(v == s[i + j] for j in range(1, n)):
            return True
    return False


def find_in_a_row(s, n=3):
    """find n characters in a string s"""
    for i, v in enumerate(s[:-(n - 1)]):
        if all(v == s[i + j] for j in range(1, n)):
            return v
    return None




class KeyGetter(object):
    def __init__(self, salt):
        """initialize"""
        self.salt = salt
        self.forward_idx = 0
        self.idx = 0

    def buf_init(self):
        """create 1000 hash values"""
        self.buffer = []
        for _ in range(1000):
            hash_str = '{}{}'.format(self.salt, self.forward_idx).encode()
            self.buffer.append(md5(hash_str).hexdigest())
            self.forward_idx += 1

    def solve(self):
        """find the 64th key"""
        # init the 1000
        self.buf_init()

        keys = 0
        while keys != 64:
            # check if possible key
            res = find_in_a_row(self.buffer.pop(0))
            if res:
                for b in self.buffer:
                    # if found a 5 in a row
                    if match_in_a_row(b, c=res):
                        keys += 1
                        break

            # add new one to end and iterate
            hash_str = '{}{}'.format(self.salt, self.forward_idx).encode()
            self.buffer.append(md5(hash_str).hexdigest())
            self.forward_idx += 1
            self.idx += 1

        return self.idx - 1



# test example
salt = 'abc'
kg = KeyGetter(salt)
assert kg.solve() == 22728

# real example
salt = 'qzyelonm'
kg = KeyGetter(salt)
print(kg.solve())