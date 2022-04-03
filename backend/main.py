import cv2
 
import os
import time
 
import math
from squats import squats
from push_up import pushup
from pull_up import pullup
from crunches import crunches
from weight_lifting import biceps
 
def squatss(f):
        count=0
        calories=0   
        n=10000
        count,calories = squats(int(n),f)
def pushupss(f):
        count=0
        calories=0   
        n=10000
        count,calories = pushup(int(n),f)
    
def pullups(f):
        count=0
        calories=0   
        n=10000
        count,calories = pullup(int(n),f)
        
 
def bicep(f):
        
        count=0
        calories=0
        n=100000
        count,calories = biceps(int(n),f)
  
def crunche(f):
        
        count=0
        calories=0
        n=1000000
        count,calories = crunches(int(n),f)
        
     
bicep(True)
