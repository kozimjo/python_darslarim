# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 10:27:26 2022

@author: User
"""

# loginni tekshirish

foydalanuvchilar = ['kozim', 'nozim', 'azim', 'rustam', 'anvar']
login = input("Yangiz login tanlang : ")
if login.lower() in foydalanuvchilar:
    print(f"Bu {login} logini band, boshqa login kiriting")
else:
    print(f"Hush kelibsiz {login.title()}")