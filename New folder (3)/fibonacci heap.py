#!/usr/bin/env python
# coding: utf-8

# In[45]:


class BinomialTree:
    def __init__(self, key):
        self.key = key
        self.children = []
        self.order = 0
    def add_at_end(self, t):
        self.children.append(t)
        self.order = self.order + 1
class BinomialHeap:
    def __init__(self):
        self.trees = []
    def extract_min(self):
        if self.trees == []:
            return None
        smallest_node = self.trees[0]
        for tree in self.trees:
            if tree.key < smallest_node.key:
                smallest_node = tree
        self.trees.remove(smallest_node)
        h = BinomialHeap()
        h.trees = smallest_node.children
        self.merge(h)
        return smallest_node.key
    def get_min(self):
        if self.trees == []:
            return None
        least = self.trees[0].key
        for tree in self.trees:
            if tree.key < least:
                least = tree.key
        return least
    def combine_roots(self, h):
        self.trees.extend(h.trees)
        self.trees.sort(key=lambda tree: tree.order)
    def merge(self, h):
        self.combine_roots(h)
        if self.trees == []:
            return
        i = 0
        while i < len(self.trees) - 1:
            current = self.trees[i]
            after = self.trees[i + 1]
            if current.order == after.order:
                if (i + 1 < len(self.trees) - 1
                    and self.trees[i + 2].order == after.order):
                    after_after = self.trees[i + 2]
                    if after.key < after_after.key:
                        after.add_at_end(after_after)
                        del self.trees[i + 2]
                    else:
                        after_after.add_at_end(after)
                        del self.trees[i + 1]
                else:
                    if current.key < after.key:
                        current.add_at_end(after)
                        del self.trees[i + 1]
                    else:
                        after.add_at_end(current)
                        del self.trees[i]
            i = i + 1
    def insert(self, key):
        g = BinomialHeap()
        g.trees.append(BinomialTree(key))
        self.merge(g)
bheap = BinomialHeap()
bprint= BinomialHeap()
count=0
print('Menu \ninsert <data>\nmin get\nmin extract\nquit\nprint')
while True:
    do = input('What would you like to do? ').split()
    operation = do[0].strip().lower()
    if operation == 'insert':
        data = int(do[1])
        bheap.insert(data)
        bprint.insert(data)
        count+=1
    elif operation == 'min':
        suboperation = do[1].strip().lower()
        if suboperation == 'get':
            print('Minimum value: {}'.format(bheap.get_min()))
        elif suboperation == 'extract':
            count-=1
            print('Minimum value removed: {}'.format(bheap.extract_min()))
            (bprint.extract_min())
    elif operation == 'quit':
        break
    elif operation == 'print':
        print('printing- ')
        for i in range(count):
            print(bprint.extract_min(),end=' ')
            i=i+1
        break


# In[48]:


import math
class FibonacciTree:
    def __init__(self, key):
        self.key = key
        self.children = []
        self.order = 0
    def add_at_end(self, t):
        self.children.append(t)
        self.order = self.order + 1
class FibonacciHeap:
    def __init__(self):
        self.trees = []
        self.least = None
        self.count = 0
    def insert(self, key):
        new_tree = FibonacciTree(key)
        self.trees.append(new_tree)
        if (self.least is None or key < self.least.key):
            self.least = new_tree
        self.count = self.count + 1
    def get_min(self):
        if self.least is None:
            return None
        return self.least.key
    def extract_min(self):
        smallest = self.least
        if smallest is not None:
            for child in smallest.children:
                self.trees.append(child)
            self.trees.remove(smallest)
            if self.trees == []:
                self.least = None
            else:
                self.least = self.trees[0]
                self.consolidate()
            self.count = self.count - 1
            return smallest.key
    def consolidate(self):
        aux = (floor_log2(self.count) + 1)*[None]
        while self.trees != []:
            x = self.trees[0]
            order = x.order
            self.trees.remove(x)
            while aux[order] is not None:
                y = aux[order]
                if x.key > y.key:
                    x, y = y, x
                x.add_at_end(y)
                aux[order] = None
                order = order + 1
            aux[order] = x
        self.least = None
        for k in aux:
            if k is not None:
                self.trees.append(k)
                if (self.least is None
                    or k.key < self.least.key):
                    self.least = k
def floor_log2(x):
    return math.frexp(x)[1] - 1
fheap = FibonacciHeap()
fprint= FibonacciHeap()
count=0
print('Menu \ninsert <data>\nmin get\nmin extract\nquit\nprint')
while True:
    do = input('What would you like to do? ').split()
    operation = do[0].strip().lower()
    if operation == 'insert':
        data = int(do[1])
        fheap.insert(data)
        fprint.insert(data)
        count+=1
    elif operation == 'min':
        suboperation = do[1].strip().lower()
        if suboperation == 'get':
            print('Minimum value: {}'.format(fheap.get_min()))
        elif suboperation == 'extract':
            print('Minimum value removed: {}'.format(fheap.extract_min()))
            fprint.extract_min()
            count-=1
    elif operation == 'quit':
        break
    elif operation == 'print':
        print('printing- ')
        for i in range(count):
            print(fprint.extract_min(),end=' ')
            i=i+1
        break

