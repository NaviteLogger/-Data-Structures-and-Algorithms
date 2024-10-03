# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 11:32:02 2024

@author: s223287
"""

class Indexer:
    
    l = [1,2,3,4,5,6,7,8,9]
    
    def __getitem__(self, index):
        print(f"getitem: {index}")
        return self.l[index]
                

X = Indexer()