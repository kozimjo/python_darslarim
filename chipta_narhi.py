# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 11:39:45 2022

@author: User
"""

# Chipta narhini belgilash

yosh = int(input("Yoshingiz nechada? : "))
if yosh <=4:
    narh = 0
elif 18 > yosh >4:
    narh = 10000
elif yosh >= 18:
    narh = 20000
else: 
    narh = 0
print(f" Sizga kirish {narh} so'm")