# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 01:30:20 2017

@author: colpus
Definitions of data classes
"""

class ImgCircle:
    def _init_(self):
        self.iRadius = 2.34

class CoOrd:
    def _init_(self, ix, iy):
 #       ix._init_ = 35
        self.xx = ix
        self.yy = iy
    iyyy = 23

class ImObjectTest:
    pass

class ImgCoOrd:
    def _init_(self, u, v):
        self.position = CoOrd(u, v)     #coOrd class created elsewhere
