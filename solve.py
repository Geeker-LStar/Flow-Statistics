import time
from random import randrange, choice, randint
from itertools import groupby

class Solve:
    def __init__(self):
        self.fakeLst = []
        
    def fakeGet(self, fshts=5):
        macs = [":".join(["%02x" % x for x in map(lambda x: randint(0, 255), range(6))]) for _ in range(40)]
        while 1:
            time.sleep(randrange(5, 50)/100)
            now = time.time()
            a = [now, randrange(-120, -30), choice(macs)]# 时间戳，强度，MAC
            self.fakeLst.append(a)
            for i in self.fakeLst:
                if now-i[0] >= fshts:
                    self.fakeLst.remove(i)
            # os.system("cls")
            # for i in self.fakeLst:
            #     print(i)


    def solveData(self, lstp):
        lstp = sorted(lstp, key=lambda s: s[0], reverse=True)# TIME
        # for i in lstp:
        #     if i[2] == None:
        #         lstp.remove(i)
        # lstp = sorted(lstp, key=lambda s: s[2])# MAC
        lst0 = []
        lst1 = []
        for i in lstp:
            if i[2] not in lst0:
                print(i)
                lst0.append(i[2])
                lst1.append(i[1])
        lstp = list(zip(lst0, lst1))
        ttl = len(lstp)
        # for i in lstp:
        #     print(i)
        n = 9
        x = []
        y = []
        for k, g in groupby(sorted(lstp, key=lambda s: s[1]), key=lambda x: x[1]//n):
            x.append('{}~{}'.format(k*n, (k+1)*n-1))
            y.append(len(list(g)))
        return x, y, ttl

