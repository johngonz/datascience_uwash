# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 03:56:20 2015

@author: johngonz
Matrix Multiply problem in the Simple Python MapReduce Framework
Note:  This problem receive input of pairs [matrix, i, j, value] where matrix
 is a string either 'a' or 'b' and i, j, and value are integers.  It outputs
product matrix AxB in the form [i,j,value]

To run it on command prompt type,
 python multiply.py data/matrix.json > problem6.json
 This writes the output of running multiply on matrix.json to 
 problem6.json.  Output can be compared to solutions/multiply.json.
"""
import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: the row,column index pairs needed to compute the [i,j] entry of AxB
    # value: record
    value = record
    if record[0] == "a":
        for k in [0,1,2,3,4]:
            key=(record[1], k)
            mr.emit_intermediate(key, value)
    else:
        for k in [0,1,2,3,4]:
            key=(k, record[2])
            mr.emit_intermediate(key, value)    

def reducer(key, list_of_values):
    # key: [row,column] index of AxB
    # value: list of entries of A and B needed to compute AxB[i,j].
    A_entries = []
    B_entries=[]
    for v in list_of_values:
        if v[0] == "a": 
            A_entries.append(v)
        else:
            B_entries.append(v)
    entry = 0
    for r in A_entries:
        for s in B_entries:
            if r[2] == s[1]:
                entry += r[3]*s[3]
    
    C_entry = [key[0],key[1],entry]
    mr.emit(C_entry)

#    mr.emit(list(OrderedDict.fromkeys(asymm_list)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
