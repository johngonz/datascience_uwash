# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 12:15:31 2015

@author: johngonz

Inverted Index problem in the Simple Python MapReduce Framework

To run it on command prompt type,
 python inverted_index.py data/books.json > problem1.json
 This writes the output of running inverted_index on books.json to 
 problem1.json.  Output can be compared to solutions/inverted_index.json.
"""

import MapReduce
import sys
from collections import OrderedDict

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
      mr.emit_intermediate(w, key)

def reducer(key, list_of_values):
    # key: word
    # value: list of document IDs where 'word' appears
    # The list_of_values contains duplicates, so the below two commands/
    # will remove duplicates from the list, but the second one actually/
    # retains order.  
#    mr.emit((key, list(set(list_of_values) ) ))
    mr.emit((key, list(OrderedDict.fromkeys(list_of_values) ) ))
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
