# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 11:36:46 2024

@author: s223287
"""

class Stepper:
    
    data = [1,2,3,4,5,6,7,8,9,10]
    
    def __getitem__(self, index: int):
        return self.data[i]
    
    def __setitem__(self, index: int, value: int):
        self.data[i] = value
    

instance = Stepper()