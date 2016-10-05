class _(object):
    def __init__(self):
        self.__ = 0

    def __call__(self):
        self.__ <<= 1
        return self

    def __getitem__(self, item):
        self.__ = (self.__ << 1) | 1
        return self

    def __invert__(self):
        string = bytearray()
        while self.__:
            string.append(self.__ & 0xff)
            self.__ >>= 8
        print(string)
        return self

    def _(self):
        return self

_ = _()

~_  ()()[:]()()()()[:] ()[:][:]()()[:]()() ()[:][:]()[:][:]()() \
    ()[:][:][:]()()[:]() ()[:][:]()[:][:][:][:] ()[:][:][:]()[:][:][:] \
    ()()[:]()()()()() ()()[:]()[:][:]()() ()[:][:]()[:][:][:][:] \
    ()[:][:]()[:][:]()() ()[:][:]()[:][:]()() \
    ()[:][:]()()[:]()[:] ()[:]()()[:]()()()
