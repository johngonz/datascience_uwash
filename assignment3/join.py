# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 09:44:50 2015

@author: johngonz
Relational join problem in the Simple Python MapReduce Framework

To run it on command prompt type,
 python join.py data/records.json > problem2.json
 This writes the output of running join on records.json to 
 problem2.json.  Output can be compared to solutions/join.json.
"""
import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: order ID
    # value: record containing that order ID
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: order identifier
    # value: list of all records from both tables containing that order ID.
    Order_list = []
    Line_Item_list=[]
    for v in list_of_values:
        if v[0] == "order": 
            Order_list.append(v)
        else:
            Line_Item_list.append(v)
    for r1 in Order_list:
        for r2 in Line_Item_list:
            r=r1.copy()
            r.extend(r2)
            mr.emit(r)
            del(r)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
