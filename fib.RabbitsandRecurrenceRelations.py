#!/usr/bin/env python
###n 0 1 2 3 4  5
###  1 1 4 7 13 19 28
### k=3 meaning k rabbits pairs instead of 1 pair are produced by one parent pair.
### Fabonacci sequence + k(n-1)-1=k*n-k-1

#n,k = 34, 2
n,k = 32,4

def DP_Fabonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        a = 1
        b = 1
        for i in range(3,n+1):
            c = a*k + b
            a = b
            b = c
            #print c
        return c
        #return DP_Fabonacci(n-1)+DP_Fabonacci(n-2) ## if recursive method is used
print DP_Fabonacci(n)

#12/5/2017 When I did it wrongly, I was not deriving the 1 1 4 7 19 ... correctly...
