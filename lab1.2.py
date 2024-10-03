# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 11:16:57 2024

@author: s223287
"""

import math

class Indexer:
    
    def __getitem__(self, index):
        return math.sqrt(index ** 5)
 
    
obiekt = Indexer()
obiekt[2]

for i in range(6):
    print(f"{round(obiekt[i], 3) }", end=' ') 
