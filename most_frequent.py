# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 19:02:04 2021

@author: shefi
"""
import operator
S= input('Please enter a string ')
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
            
            
    desc = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
    return desc



print (most_frequent(S))