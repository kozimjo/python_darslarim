# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 11:22:01 2023

@author: User
"""

# MOSLASHUVCHAN FUNKSIYA

# *args USULI

# def yigindi(*sonlar):
#     summa = 0
#     for son in sonlar:
#         summa += son
#     return summa
# print(yigindi(5,8,9,4)) 

# def summa(*sonlar):
#     return sum(sonlar)
# print(summa(9,10,20))

# def yigindi(a, b, *sonlar): #bu yerda 'a' va 'b' majburiy argumentlardir 
#     return a+b+sum(sonlar)
# print(yigindi(5, 10, 2, 20, 3))
# print(yigindi(1)) #yigindi() missing 1 required positional argument: 'b'

# def jami(*sonlar):
#     """Kiritilgan sonlarni yig'indisini hisoblaydigan funksiya"""
#     return sum(sonlar)
# print(range(jami()))
      
# def summa(x, y, *numbers):
#     return x+y+sum(numbers)
# print(summa(1, 2))
# print(summa(3, 4, 5))
# print(summa(6, 7, 8, 9))
# print(summa(10))

# **kwargs usuli

# def avto_info(kompaniya, model, **malumotlar):
#     """Avto haqidagi ma'lumotlarni lugat ko'rinishida qaytaruvchi funksiya"""
#     malumotlar['kompaniya']=kompaniya
#     malumotlar['model']=model
#     return malumotlar
# avto1=avto_info('bmw', 'x7', rang='qizil', narx=125000)
# avto2=avto_info('mersedes', 's-1000', korobka='mexanika', yil=2023)
# print(f"{avto1['kompaniya'].upper()}: Markasi {avto1['model']}, narxi-{avto1['narx']}$")
# print(avto2)

# def kupaytuvchi(*sonlar):
#     kupaytma = 1
#     for son in sonlar:
#         kupaytma *=son
#     return kupaytma
# print(kupaytuvchi(5,6,7,20,100,9))

# def talaba_info(ism, familiya, **malumotlar):
#     """Talabalar haqida ma'lumot beruvchi funksiya"""
#     malumotlar['ism']=ism
#     malumotlar['familiya']=familiya
#     return malumotlar
# talaba1=talaba_info('Dilnoza', "Turdaliyeva", yil=1984, fakultet='iqtisod')
# talaba2=talaba_info('Nargiza', "Karimova", yil=1981, kurs='bitirgan')
# print(talaba1)
# print(talaba2)

