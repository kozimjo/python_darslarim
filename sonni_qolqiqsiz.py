# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 10:32:40 2022

@author: User
"""

#Butun sonni tekshirish

son = int(input("Butun son kiriting : "))
for n in range(2, 100):
    if not (son%n):
        print(f"{son} soni {n} soniga qolqiqsiz bo'linadi")
