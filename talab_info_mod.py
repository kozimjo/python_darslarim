# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 10:39:04 2023

@author: User
"""
def talaba_info(ismi, familiyasi, manzili, fakultet, yoshi):
    """Talaba haqida ma'lumot beruvchi funksiya"""
    talaba = {'ismi':ismi,
              'familiyasi':familiyasi,
              'manzili':manzili,
              'fakultet':fakultet,
              'yoshi':yoshi}
    return talaba

def talaba_kirit():
    """Foydalanuvchidan talaba_info funksiyasi yordamida bir nechta talabalar haqidagi
    ma'lumotni bitta ro'yhatga joylovchi funksiya"""
    talabalar = []
    while True:
        ismi = input("Ismi: ")
        familiyasi = input("Familiya: ")
        manzili = input("Manzili: ")
        fakultet = input("Fakultet: ")
        yoshi = int(input("Yosh: "))
        talabalar.append(talaba_info(ismi, familiyasi, manzili, fakultet, yoshi))
        javob = input("Yana ma'lumot qo'shasizmi: ")
        if javob == 'no':
            break
        return talabalar
def talaba_info_print(talaba_info):
    """Talabalar haqidagi ma'lumotni konsolga chiqaruvchi funksiya"""
    print(f"Talabaning ismi: {talaba_info['ismi'].title()} {talaba_info['familiyasi'].title()}",
          f"Manzili: {talaba_info['manzili'].title()}.",
          f"Fakulteti: {talaba_info['fakultet']}.",
          f"Yoshi: {talaba_info['yoshi']}.",)

