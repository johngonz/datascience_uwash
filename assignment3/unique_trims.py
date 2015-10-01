# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 03:36:47 2015

@author: johngonz
Unique trims problem in the Simple Python MapReduce Framework
Note:  This problem receive input of pairs [sequence ID, nucleotides], trims
all nucleotides by 10 characters, and outputs the set of unique nucleotides   

To run it on command prompt type,
 python unique_trims.py data/dna.json > problem5.json
 This writes the output of running unique_trims on friends.json to 
 problem5.json.  Output can be compared to solutions/unique_trims.json.
"""
import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: nucleotide sequence trimmed by 10 characters
    # value: Sequence ID where the nucleotide sequence appeared
    key = record[1][0:len(record[1])-10]
    value = record[0]
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: nucleotide sequence trimmed by 10 characters
    # value: list of Sequence IDs where the nucleotide sequence appeared.
    mr.emit(key)

#    mr.emit(list(OrderedDict.fromkeys(asymm_list)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
