#!/usr/bin/env python

m,n,k=21,15,19

def mendel(m,n,k):
    S=float(m+n+k)*(m+n+k-1)
    print (m*(m-1)*0.75 + k*(k-1) + m*n + 2*n*k +2*m*k )/S

mendel(m,n,k)

