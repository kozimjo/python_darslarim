# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 11:47:53 2022

@author: User
"""

son1 = float(input("Birinchi sonni kiriting : "))
son2 = float(input("Ikkinchi sonni kiriting : "))
if son1 == son2:
    print("Sonlar teng")
elif son1 > son2:
    print(f"{son1}- soni {son2}- sonidan katta")
else:
    print(f"{son2}- soni {son1}- sonidan katta")