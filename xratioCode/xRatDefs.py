# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 01:30:20 2017

@author: colpus
Definitions of data classes
"""

class ImgCircle:
    def __init__(self):
        self.iRadius = 2.34

class CoOrd:
    def __init__(self, t):
        self.xx = t



class ImObjectTest:
    pass

class ImgCoOrd:
    def __init__(self, u, v):
        self.position = CoOrd(u, v)     #coOrd class created elsewhere
