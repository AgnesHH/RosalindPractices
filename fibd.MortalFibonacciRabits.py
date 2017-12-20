#!/usr/bin/env python
# m generation are imortal, >m generations are mortal.
# first to get m generations using FIB(m), e.g. if m=3, first get [1,1,2]
# Then from m+1 to n, Fn = Fn-m + Fn-m+1 + ... + Fn-2
def Fabbonacci(m):
    if m == 1:
        return 1
    elif m == 2:
        return 1
    else:
        a = 1
        b = 1
        for i in range(3,m+1):
            c = a + b
            a = b
            b = c
        return c

n,m = 84,20
initial=[]
for i in range(1,m+1):
    initial.append(Fabbonacci(i))
print initial

from collections import deque
FIBs=deque(initial)
for i in range(m+1,n+1):
    listcp = list(FIBs)
    #print listcp
    FIBs.append(sum(listcp[0:-1]))
    FIBs.popleft()
    #print FIBs
print FIBs[-1]


def fib(n,k=1):
  ages = [1] + [0]*(k-1)
  for i in xrange(n-1):
    print ages
    ages = [sum(ages[1:])] + ages[:-1]
  return sum(ages)

print fib(84,20)
