#!/usr/bin/env python

import sys
myfile=sys.argv[1]

with open(myfile,'r') as f:
    #alllines=f.readlines()
    name='me'
    seq='ATGC'
    for line in f:
        if line[0] == '>':
            print name,(seq.count('G')+seq.count('C'))/float(len(seq))
            seq=''
            name=line[1:]
        else:
            seq+=line.replace('\n','')
    else:
        print name,(seq.count('G')+seq.count('C'))/float(len(seq))



