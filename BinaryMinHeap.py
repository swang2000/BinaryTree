'''
1. Realize a binary mini heap using list in Python
2. Insert function
3. Delete function

Parent(r) =(r−1)/2 if r≠0.
Left child(r) =2r+1 if 2r+1≤n.
Right child(r) =2r+2 if 2r+2≤n.
Left sibling(r) =r−1 if r is even.
Right sibling(r) =r+1 if r is odd and r+1≤n.

def pushup(self, i):
    while (i-1)//2 >=0:
        if self.heaplist[(i-1)//2] > self.heaplist[i]:
            self.heaplist[(i - 1) // 2], self.heaplist[i] = self.heaplist[i], self.heaplist[(i-1)//2]
        i = (i-1) //2

def pushdn(self, i):
    while (2*i +1) < self.currentsize:
        if self.heaplist[2*i +1] < self.heaplist[2*i +2]:
            if self.heaplist[2*i +1] < self.heaplist[i]:
                self.heaplist[2 * i + 1], self.heaplist[i] = self.heaplist[i], self.heaplist[2*i +1]
            i = 2*i + 1
        else:
            if self.heaplist[2*i +2] < self.heaplist[i]:
                self.heaplist[2 * i + 2], self.heaplist[i] = self.heaplist[i], self.heaplist[2*i +2]
            i = 2 * i + 2
    if 2*i +1 == self.currentsize:
        if self.heaplist[2 * i + 1] < self.heaplist[i]:
            self.heaplist[2 * i + 1], self.heaplist[i] = self.heaplist[i], self.heaplist[2 * i + 1]

def add(self, v):
    self.heaplist.append(v)
    self.currentsize += 1
    self.pushup(self, self.currentsize)


def remove(self,v):
    for i in range(self.currentsize):
        if self.heaplist[i] == v:
            self.heaplist[i] = self.heaplist.pop()
            self.currentsize -= 1
            self.pushdn(i)



'''






class BinHeap:
    def __init__(self):
        self.heaplist = []
        self.currentsize = 0

    def pushup(self, i):
        while (i - 1) // 2 >= 0:
            if self.heaplist[(i - 1) // 2] > self.heaplist[i]:
                self.heaplist[(i - 1) // 2], self.heaplist[i] = self.heaplist[i], self.heaplist[(i - 1) // 2]
            i = (i - 1) // 2

    def pushdn(self, i):
        while 2*i +1 < self.currentsize:
            if self.heaplist[(2*i+1)] <= self.heaplist[(2*i+2)]:
                if self.heaplist[i] > self.heaplist[(2*i+1)]:
                    self.heaplist[(2*i+1)], self.heaplist[i] = self.heaplist[i], self.heaplist[(2*i+1)]
                    i = 2*i +1
            elif self.heaplist[(2*i+2)] < self.heaplist[(2*i+1)]:
                if self.heaplist[i] > self.heaplist[(2*i+2)]:
                    self.heaplist[(2*i+2)], self.heaplist[i] = self.heaplist[i], self.heaplist[(2*i+2)]
                    i = 2*i + 2
        if 2*i +1 == self.currentsize:
            if self.heaplist[i] < self.heaplist[(2 * i + 1)]:
                self.heaplist[(2 * i + 1)], self.heaplist[i] = self.heaplist[i], self.heaplist[(2 * i + 1)]

    def insert(self, v):
        self.currentsize += 1
        self.heaplist.append(v)
        self.pushup(self.currentsize -1)

    def delv(self, v):
        for i in range(self.currentsize):
            if self.heaplist[i] == v:
                self.heaplist[i] = self.heaplist.pop()
                self.currentsize -= 1
                self.pushdn(i)
                break




binhp = BinHeap()
binhp.insert(2)
binhp.insert(3)
binhp.insert(5)
binhp.insert(8)
binhp.insert(4)
binhp.insert(1)
binhp.insert(7)
binhp.delv(3)





