#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:25:52 2019

@author: swilson5
"""
import math


class Calculator: 
    def __init__(self, data): #arguments
       #attributes
        self.length = len(data)
        self.data = data
        self.mean = self.calc_mean(data)
        self.median = self.calc_median(data)
        self.variance = self.variance(data)
        self.stand_dev = self.variance**0.5
    
    def _calc_mean(self):
        return sum(data)/len(data)
    def _calc_median(self, data):
        if len(data)%2 == 0:
            mid_left = self.data[self.length // 2 -1]
            mid_right = self.data[self.length // 2 ]
            avg = (mid_left + mid_right) / 2
        else:
            avg = data[len(data) // 2] 
            return avg
    def add_data(self, new_data):
        return self.data.extend(new_data)
    def remove_data(self, new_data):
        return self.data.remove(new_data)
    def variance(self, data):
        return sum([(i-self.calc_mean(self.data))**2 for i in self.data])/(len(self.data)-1)