# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 01:09:01 2017

@author: colpus
Main calling module

"""
import xRatDefs as xRD
import xRatImgCalcs as xImg



tmpX = xRD.CoOrd
print (tmpX)

# bb = xRD.ImgCircle
# print ('chk this', bb.iRadius)

class ICcle:
    def _init_(self, gg):
        self.bRad = 2.34
bb=ICcle(4)
#bb.bRad = 23
print (bb.bRad)

backVal = xImg.getImageData ()

print (backVal)
print('hello world - calling')

