# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 08:39:53 2023

@author: User
"""

# import avto_info_mod
# avto1=avto_info_mod.moshin_malumot('kia', 'rlx', 'qora', 2022, 'mehanika', 35000, 33000)
# avto_info_mod.moshin_mal_print(avto1)
# import avto_info_mod as aim
# avto1 = aim.moshin_malumot('hyunday', 'sonata', 'qizil', 2022, "avto", '125000', 56000)
# aim.moshin_mal_print(avto1)
# from avto_info_mod import moshin_malumot, moshin_mal_print
# moshin1=moshin_malumot('daewoo', 'matiz', 'oq', 2002, 'mexanika', 3000, 320000)
# moshin_mal_print(moshin1)
# import talab_info_mod
# talaba1=talab_info_mod.talaba_info('kozim', 'muxtorov', 'qo\'qon', 'energetika', 39)
# talab_info_mod.talaba_info_print(talaba1)

# import talab_info_mod as tim
# talaba1 = tim.talaba_kirit()
# tim.talaba_info_print(talaba1)

# from avto_info_mod import moshin_malumot, moshin_mal_print
# avto3 = moshin_malumot('toyota', 'camaro', 'qora', 2023, 'avtomat', 46000, 0)
# moshin_mal_print(avto3)

# from talab_info_mod import talaba_info, talaba_info_print
# talaba3=talaba_info('xushnuda', 'kasimova', 'fargona', 'iqtisod', 35)
#talaba_info_print(talaba3)

# from talab_info_mod import talaba_info as ti
# from talab_info_mod import talaba_info_print as tip
# talaba = ti('iroda', 'muxtorova', 'mingtut', 'tarih', 33)
# tip(talaba)

# from talab_info_mod import *
# talabalar = talaba_info('kaka', 'ricardo', 'brazil', 'futbol', 45)
# talaba_info_print(talabalar)
# import uzgaruvchi
# avt = uzgaruvchi.avto1[0]
# print(avt)
# import uzgaruvchi
# ikkinchi_element = uzgaruvchi.avto1[1]
# print(ikkinchi_element)

# import math
# x=81
# print(math.sqrt(x))

# import math
# x=5
# n=5
# print(math.pow(x,n))

# from math import pi
# print(pi)
# import math
# print(math.pow(3,3))

# import math
# print(math.log2(128))
# print(math.log10(100))
# import math
# print(math.log2(16))

# import math 
# print(math.log2(128))
# print(math.log10(10000000000))

# Random moduli

# import random 
# son = random.randint(0, 100)
# print(son)

# import random 
# number = random.randint(1,50)
# print(number)

# import random 
# avtolar = ['tahoe', 'equinox', 'malibu', 'trabilazer', 'gentra']
# avto = random.choice(avtolar)
# print(avto)

# choice(x)
# import random as r
# x = list(range(0,100,5))
# print(x)
# print(r.choice(x))

# shuffle(x)-funksiyasi
# import random as r
# x = list(range(11))
# print(x)
# r.shuffle(x)
# print(x)

# sample(x, k) funksiyasi
# from random import sample
# x=list(range(0, 50))
# y=sample(x, k=10)
# print(y)


#lambda - NOMSIZ FUNKSIYA
# lambda argument : ifoda ko'rinishida ishlaydi

# import math
# uzunlik = lambda pi, r:2*pi*r
# print(uzunlik(math.pi, 5))

 
# product = lambda x, y : x**y
# print(product(5,2))
# yuza = lambda a, b, c : a*b*c
# print(yuza(5, 4, 2))
 
# def daraja(n):
#     """Kiritilgan sonni darajasini aniqlovchi funksiya"""
#     return lambda a:a**n
# kvadrat = daraja(2)
# kub = daraja(3)
# print(f"4-ni kvadrati {kvadrat(4)} ga teng",
#       f"\n4-ni kubi {kub(4)} ga teng")

# import math
# doira_yuza = lambda pi, r : pi*r**2
# print(doira_yuza(math.pi, 9), "m2")

# import math 
# silindr_hajmi = lambda pi, r, h : pi*h*r**2
# print(silindr_hajmi(math.pi, 4, 4))

# def daraja(n):
#     return lambda x : x**n
# kvadrat = daraja(2)
# kub = daraja(3)
# print(f"5 ning kvadrati {kvadrat(5)} ga teng.")
# print(f"5 ning kubi {kub(3)} ga teng")

# def daraja(n):
#     return lambda x:x**n
# kvadrat = daraja(2)
# kub = daraja(3)
# kvart = daraja(4)
# print(f"9 ning 4-darajasi {kvart(4)} ga teng")
# print(f"9 ning kubi {kub(3)} ga teng")


# map() FUNKSIYASI

# from math import sqrt
# sonlar = list(range(11))
# ildizlar = list(map(sqrt, sonlar))
# print(ildizlar)

# sonlar = list(range(11))
# def daraja(x):
#     return x*x
# print(list(map(daraja, sonlar)))
# kvadratlar = list(map(lambda x:x*x, sonlar))
# print(kvadratlar)


# sonlar = list(range(21))
# kvadratlar = []
# for son in sonlar:
#     kvadratlar.append(son*son)
# print(kvadratlar)

# a=[10,20,30]
# b=[40,50,60]
# a_plus_b = list(map(lambda x, y :x+y, a,b))
# print(a_plus_b)

# ismlar = ['kozim', 'nozim', 'azim', 'hakim']
# print(list(map(lambda royhat:royhat.upper(), ismlar)))

# def daraja(n):
#     return lambda x:x**n
# kvadrat = daraja(2)
# kub=daraja(3)
# kvant=daraja(4)
# fevant=daraja(5)
# print(f"{kvadrat(7)}, {kub(7)}, {kvant(7)}, {fevant(7)}")

# from math import sqrt
# sonlar = list(range(11))
# ildizlar = list(map(sqrt, sonlar))
# print(ildizlar)

# sonlar = list(range(11))
# def daraja(x):
#     return x**x
# print(list(map(daraja, sonlar)))

# numbers = list(range(15))
# def daraja(x):
#     return x*x
# kvadratlar = list(map(lambda x:x*x, numbers))
# print(kvadratlar)


# a=[1,2,3]
# b=[4,5,6]
# a_b = list(map(lambda x,y:x+y, a,b))
# print(a_b)

# ismlar=['kozim', 'nozim', 'azim', 'hakim']
# print(list(map(lambda ismlar:ismlar.upper(), ismlar)))


#filter FUNKSIYASI

# import random
# sonlar = random.sample(range(100),10)
# def juftmi(x):
#     return x%2==00
# juft_sonlar = list(filter(juftmi, sonlar))
# print(sonlar)
# print(juft_sonlar)

# import random
# raqamlar = random.sample(range(51), 15)
# juft_raqamlar = list(filter(lambda son:son%2==0, raqamlar))
# print(juft_raqamlar)

mevalar = ['anor', 'anjir', 'olma', 'behi', 'shaftoli', 'ananas', 'uzum', 'hurmo',]
mevA = list(filter(lambda meva:meva.startswith('a'), mevalar))
#print(mevA)

# meva = list(filter(lambda meva:len(meva)<=4, mevalar))
# print(meva)
mevalarAR = list(filter(lambda meva : meva.startswith('a') and meva.endswith('r'), mevalar))
#print(mevalarAR)
