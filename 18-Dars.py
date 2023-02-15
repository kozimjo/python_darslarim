# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 13:32:38 2022

@author: User
"""

# 18-DARS.
# WHILE. RO'YHATLAR VA LUG'AT

#print("Yaqin do'stlaringiz ro'yhatini tuzamiz")
#ismlar = []
#n = 0
#while True:
 #     savol = f"{n+1}-Do'stingiz ismini kiriting: "
  #    ism = input(savol)
   #   ismlar.append(ism)
    #  takrorlash = input("Yana ism qo'shasizmi? (ha/yo'q) -")
     # n += 1
      #if takrorlash != 'ha':
       #   break
#print("Do'stlaringiz ro'yhati")
#for ism in ismlar:
 #   print(ism)
#print("Yaqin do'stlaringiz ro'yhatini tuzamiz:")
#ismlar = []
#n = 1
#while True: 
 #   savol = f"{n}-do'stingiz ismini yozing: - "
  #  ism = input(savol)
   # ismlar.append(ism)
    #takror_surash = input("Yana ism qo'shasizmi? (ha/yo'q) - ")
    #n += 1
    #if takror_surash != 'ha':
     #   break
#print("Dostlaringiz ismi")
#for ism in ismlar:
 #   print(ism)

#print("Do'stlaringiz ro'yhatini tuzing")
#n = 1
#dustlar = []
#while True:
 #   savol = f"{n}-do'stingiz ismini kiriting: - "
  #  ism = input(savol)
   # dustlar.append(ism)
    #n += 1
    #takror_sura = input("Yana ism kiritasizmi? (ha/yo'q') - ")
    #if takror_sura != 'ha':
     #   break
#print("Do'stlaringiz ro'yhati")
#for ism in dustlar:
 #       print(ism.title())

#print("Dustlarizi ismini yozing")
#n = 1
#dustlar = []
#while True:
 #   savol = f"{n}-dustingiz ismini yozing - "
  #  ism = input(savol)
   # dustlar.append(ism)
    #n += 1
    #takror = input("Yana ism kiritasizmi? (yes/no)- ")
    #if takror == 'yes':
     #   continue
    #else: 
     #   break
#print("Do'stlaringiz ismi")
#for ism in dustlar:
 #   print(ism.title())

#print("Do'stlaringiz ro'yhatini tuzamiz")
#dostlar = []
#n=1
#while True:
 #   savol = f"{n}-do'stingizni ismini kiriting - "
  #  ism = input(savol)
   # dostlar.append(ism)
    #n += 1
    #takrorlash = input("Yana ism qo'shasizmi? (yes/no) - ")
    #if takrorlash != 'yes':
     #   break
#print("Dostlaringiz ro'yhati")
#for ism in dostlar:
 #   print(ism.title())

#print("Dustlarni ro'yhati")
#dostlar = []
#n = 1
#while True:
    #avol = f"{n}-do'stingiz isminikiriting - "
    #ism = input(savol)
    #dostlar.append(ism)
    #takrorlash = input("Yana ism qo'shasizmi? - (yes/no) - ")
    #n += 1
    #if takrorlash == 'yes':
   #     continue
  #  else: 
 #       break
#print("Do'stlaringiz ro'yhati")
#for ism in dostlar:
    #print(ism.title())
#LUG'AT TO'LDIRISH

#print("Do'stlaringiz ro'yhatini tuzamiz!")
#dostlar = {}
#ishora = True 
#while ishora: 
 #   ism = input("Do'stingiz ismini kiriting - ")
  #  yosh = input("Do'stingiz yoshini kiriting - ")
   # dostlar[ism] = int(yosh)
    #takror = input("Yana ism kiritasizmi? (yes/no) - ")
    #if takror == "no":
     #   ishora = False
#for ism, yosh in dostlar.items():
 #   print(f"{ism.title()}ning yoshi {yosh}-da")
    
# RO'YHATLAR ICHIDAN QIYMATNI OLIB TASHLASH
cars = ['gentra', 'nexia', 'matiz', 'bmw', 'gentra', 'cobalt', 'spark', 'gentra']
car = 'matiz'
while car in cars:
    cars.remove(car)
    print(cars)
    