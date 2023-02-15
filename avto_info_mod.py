# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 09:49:45 2023

@author: Kozim
"""

# MODUL

# def avto_info(make, model, rangi, korobka, yili, narxi=None):
#     avto = {'make':make,
#             'model':model,
#             'rangi':rangi,
#             'korobka':korobka,
#             'yili':yili,
#             'narxi':narxi}
#     return avto
# def avto_kirit():
#     """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida 
#         ma'lumotlarni bitta ro'yhatga joylash imkonini beruvchi funksiya"""
#     avtolar = []
#     while True:
#         print("\nQuyidagi ma'lumotlarni kiriting", end='')
#         make=input("Ishlab chiqaruvchi: ")
#         model = input("Modeli: ")
#         rangi = input("Rangi: ")
#         korobka = input("Korobkasi: ")
#         yili = int(input("Ishlab chiqarilgan yili: "))
#         narxi = int(input("Narxi: "))
#         avtolar.append(avto_info(make, model, rangi, korobka, yili))
#         javob = input("Yana avto kiritasizmi? (yes/no): ")
#         if javob == 'no':
#             break
#         return avtolar
# def info_print(avto_info):
#     """Avtomobillar haqida ma'lumotkar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
#     print(f"{avto_info['make'].title()}:",
#           f"{avto_info['model'].upper()},",
#           f"{avto_info['rangi']},",
#           f"{avto_info['korobka']},",
#           f"{avto_info['yili']},",
#           f"{avto_info['narxi']}$,")
    
def moshin_malumot(i_ch, marka, rang, yil, korobka, narx, probeg):
    """Ishlab chiqarilgan avto haqida ma'lumot"""
    moshin = {'i_ch':i_ch,
              'marka':marka,
              'rang':rang,
              'yil':yil,
              'korobka':korobka,
              'narx':narx,
              'probeg':probeg}
    return moshin

def moshin_kirit():
    """Foydalanuvchiga moshin_malumot funksiyasi yordamida bir nechta avtolar 
    haqida ma'lumotlarni bitta ro'yhatga joylash imkonini beruvchi funksiya"""
    moshinlar = []
    while True:
        i_ch = input("Kompaniya: ")
        marka = input("Marka: ")
        rang = input("Rang: ")
        yil = int(input("Yili: "))
        korobka = input("Korobkasi: ")
        narx = float(input("Narxi: "))
        probeg = float(input("Yurgan masofasi: "))
        moshinlar.append(moshin_malumot(i_ch, marka, rang, yil, korobka, narx, probeg))
        javob = input("Yana ma'lumot qo'shasizmi? (yes/no): ")
        if javob == 'no':
            break
        return moshinlar

def moshin_mal_print(moshin_malumot):
    """Avtomobillar haqida ma'lumot saqlangan lug'atni konsolga chiqaruvchi funksiya"""
    print(f"\nIshlab chiqaruvchi: {moshin_malumot['i_ch'].title()}.",
          f"\nMarkasi: {moshin_malumot['marka'].upper()}.",
          f"\nRangi: {moshin_malumot['rang']}.",
          f"\nIshlab chiqarilgan yili: {moshin_malumot['yil']}yil.",
          f"\nKorobkasi: {moshin_malumot['korobka']}.",
          f"\nNarxi: {moshin_malumot['narx']}$.",
          f"\nYurgan masofasi: {moshin_malumot['probeg']}km.",
          )
    