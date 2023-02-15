# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 11:54:32 2022

@author: User
"""

#mahsulotlar = ['non', 'un', 'shakar', 'choy', 'tuz', 'yog\'', 'go\'sht', 'tuhum', 'kartoshka', 'piyoz']
#savat = []
#for n in range(5):
 #   savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing - "))

#for mahsulot in savat:
 #   if mahsulot in mahsulotlar:
  #       print(f"Do'konimizda {mahsulot} bor")
   # else:
    #     print(f"Do'konimizda {mahsulot} yo'q")
         
#mahsulotlar = ['non', 'un', 'shakar', 'choy', 'tuz', 'yog\'', 'go\'sht', 'tuhum', 'kartoshka', 'piyoz']
#bor_mahsulotlar = []
#yuq_mahsulotlar = []
#for n in range(5):
 #   savol = input(f"{n+1}-mahsulotni kiriting : ")
  #  if savol in mahsulotlar:
   #     bor_mahsulotlar.append(savol)
    #if savol not in mahsulotlar:
     #   yuq_mahsulotlar.append(savol)
#for savol in bor_mahsulotlar:
 #   print(f"{savol} bor")
#for savol in yuq_mahsulotlar:
 #   print(f"{savol} yo'q")

#mahsulotlar = ['non', 'un', 'shakar', 'choy', 'tuz', 'yog\'', 'go\'sht', 'tuhum', 'kartoshka', 'piyoz']
#savat = []
#for s in range(5):
 #   savat.append(input(f"{s+1}-mahsulotni kiriting : "))
    
#bor_mahsulotlar = []
#mavjud_emas = []
#for savol in savat:
 #   if savol in mahsulotlar:
  #      bor_mahsulotlar.append(savol)
   # else:
    #    mavjud_emas.append(savol)
#if mavjud_emas:
 #   print("Do'konimizda quyidagi mahsulotlar yo'q")
  #  for mahsulot in mavjud_emas:
   #     print(mahsulot)
    #else:
     #   print("uyidagi mahsulotlar bor")
      #  for mahsulot in bor_mahsulotlar:
       #     print(mahsulot)
       
mahsulotlar = ['non', 'un', 'shakar', 'choy', 'tuz', 'yog\'', 'go\'sht', 'tuhum', 'kartoshka', 'piyoz']
savat = []
for n in range(5):
   savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing : "))
bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)
if mavjud_emas:
    print("Do'konimzda quyidagiz mahsulotlar yo'q")
    for mahsulot in mavjud_emas:
        print(mahsulot)
    else:
        print("Do'konimizda quyidagi mahsulotlar bor")
        for mahsulot in bor_mahsulotlar:
            print(mahsulot)