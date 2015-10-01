# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 15:09:30 2015

@author: johngonz
Friend Count Social Network Analysis problem in the Simple Python MapReduce Framework

To run it on command prompt type,
 python friend_count.py data/friends.json > problem3.json
 This writes the output of running friend_count on friends.json to 
 problem3.json.  Output can be compared to solutions/friend_count.json.
"""
import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person
    # value: friend
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: person
    # value: list of person's friends
    r=[key,len(list_of_values)]
    mr.emit(r)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
