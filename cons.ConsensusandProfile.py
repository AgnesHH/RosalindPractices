#!/usr/bin/env python

import sys
myfile=sys.argv[1]
DNAStrings=[]
seq=''
with open(myfile,'r') as f:
    for line in f:
        if line[0] == '>':
            if seq:
                DNAStrings.append(seq)
            seq=''
        else:
            seq+=line.replace('\n','')
    DNAStrings.append(seq)

#print (DNAStrings)
#ACGT profile matrix generation
hash={'A':0,'C':1,'G':2,'T':3}
Profile=[]
for i in range(0,4):
    Profile.append([0]*len(DNAStrings[0]))
for seq in DNAStrings:
    for i in range(0,len(seq)):
        nt = seq[i]
        #print (nt,i)
        Profile[hash[nt]][i]+=1

order='ACGT'
from numpy import array
ProfileT = array(Profile).transpose()
#print (ProfileT)
Consensus=''
for i in range(0,len(ProfileT)):
    Consensus+=order[list(ProfileT[i]).index(max(ProfileT[i]))]
print (Consensus)

for i in range(0,len(Profile)):
    Profileinstr=' '.join(str(j) for j in Profile[i])
    print (order[i]+': '+' '.join(str(j) for j in Profile[i]))
