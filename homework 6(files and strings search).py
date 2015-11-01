# coding: utf-8

import os
import argparse

#find generator

def find (rash):
    for filename in os.listdir(path):
        if filename.endswith(rash):
            for i, line in enumerate(open (filename)):
                
                yield filename, i, line
#grep generator
               
def grep (gen, substr):
    for name, i, s in gen:
        if substr in s:
            yield name, i, s
        #print (name, i, s)

#searching necesary data
path = input('Enter directory to search or choose "." to search in this one ') 
ftype = input('Enter filetype like .<filetype> to search ')
subs = input ('Enter which substring you want to find ')

for name, i, s in grep (gen = find(ftype), substr = subs ):
    print (name, i, s)
                

