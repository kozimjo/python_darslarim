# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 09:28:27 2023

@author: User
"""
#AMALIYOT

f1 = lambda x:x*10
#print(f1(9))

f2 = lambda x,y:x+y
#print(f2(5,6))

import random as r
f3 = r.sample(range(1001),10)
#print(f3)
kv = list(map(lambda son:son**2, f3))
#print(kv)
#print(list(filter(lambda son:son%2, f3)))

def tubmi(x):
    if x%2==0 or x<2: return False # Son juft yoki 2 dan kichik bo'lsa
    if x==2 or x==3 : return True # Son 2 yoki 3 bo'lsa
    for i in range(3,x,2):         
        if x%i==0:
          if x % 2 == 0 or x < 2:
              return False  # Son juft yoki 2 dan kichik bo'lsa
    if x == 2 or x == 3:
        return True  # Son 2 yoki 3 bo'lsa
    for i in range(3, x, 2):
        if x % i == 0:
            return False
    return True

tub_sonlar = list(filter(tubmi,range(1000)))
print(tub_sonlar)
