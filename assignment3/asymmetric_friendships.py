# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 15:22:02 2015

@author: johngonz
Asymmetric Friend Relationships Social Network Analysis problem in the
Simple Python MapReduce Framework
Note:  This program outpus all friendships which are not symmetric, this is not
what the instructions of the problem say but the author thought this made more
sense than outputting the full symmetric relation.  

To run it on command prompt type,
 python friend_count.py data/friends.json > problem4.json
 This writes the output of running asymmetric_friendships on friends.json to 
 problem4.json.  Output can be compared to solutions/friend_count.json but it
 does not match since this program does not outpu the full symmetric relation.
"""
import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key1: person
    # key2: friend
    # value: The [person,friend] pair
    key1 = record[0]
    key2 = record[1]
    value = record
    mr.emit_intermediate(key1, value)
    mr.emit_intermediate(key2, value)

def reducer(key, list_of_values):
    # key: person or friend
    # value: list of [person, friend] relationships that key appears in.
    for pair in list_of_values:
        if pair[0]==key and [pair[1],pair[0]] not in list_of_values:
            mr.emit(pair)

#    mr.emit(list(OrderedDict.fromkeys(asymm_list)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
