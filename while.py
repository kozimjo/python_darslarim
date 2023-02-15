# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 11:23:09 2022

@author: User
"""

# while SIKLI
# for sikli bilan while sikli orasidagi farq shuki, for siklining takrorlanishi
# biror ro'yhat (lug'at, to'plam) elementlari soniga bog'langan bo'lsa, 
# while siklinig takrorlanishi biror shartning takrorlanishiga bog'liq. 

#while QANDAY ISHLAYDI?
#while sikli badanidagi kodning necha marta takrorlanishi biror shasrtga bog'langan bo'ladi.
#misol....

#son = 1
#while son <=5:
 #   print(son, end = ' ')
  #  son = son+1

#yuqoridagi dasturni tahlil qilamiz.
# * avval son degan o'zgaruvchi yaradik va unga 1 qiymatni berdik.
# * 2-qatorda esa "toki son 5 dan kichik yoki teng ekan" keyingi qatorlarni bajar dedik.
# * 3-qatorda sonni konsolga chiqar dedik.
# * 4-qatorda songa 1 qo'shdik.
# * 4-qatordan so'ng kod yana 2-qatorga qaytadi va son<=5 shartini tekshiradi,
# agar shart bajarilsa (True), 3-4-qatorlar takrorlanadi.
# * 5-qadamdan so'ng son=5 bo'lganida while sikli to'htaydi. 

#while son<=100:
  #  print(son)
   # son+=20
   
# while va input()

# while sikli yordamida dasturni to'htatish omkoniyatini foydalanuvchiga berishimiz mumkin.

#print("Kiritilgan sonning kvadratini qaytaruvchi dastur. ")
#savol = "Isatalgan son kiriting. to\'htatish uchun 'exit' deb yozing: "
#qiymat = ''
#while qiymat != 'exit':
 #   qiymat = input(savol)
  #  if qiymat != 'exit':
   #     print(float(qiymat)**2)
        
#print("Kiritilgan sonni kvadratinim topish formulasi.")
#son = "Istalgan sonni kiriting! To'xtatish uchun 'exit' deb yozing: "
#qiymat =''
#while qiymat != 'exit':
 #   qiymat = input(son)
  #  if qiymat != 'exit':
   #     print(float(qiymat)**2)

#print("kiritilgan sonni kvadratini qaytaruvchi dastur!")
#savol = 'Istalgan sonni kiriting.'
#savol += "Dasturni to'xtatish uchu 'exit' deb yozing: "
#qiymat = ''
#while qiymat != 'exit':
 #   qiymat = input(savol)
  #  if qiymat != 'exit':
   #     print(float(qiymat)**2)

#ISHORA - FLAG

#print("Kiritlgan sonni kvadratini topish dasturi")
#savol = 'Istalgan sonni kiriting.\n'
#savol += 'Dasturni to\'xtatish uchun "exit" deb yozing: '
#qiymat = ''
#ishora=True
#while ishora:
 #   qiymat = input(savol)
  #  if qiymat == 'exit':
   #     ishora=False
    #else:
     #   print(float(qiymat)**2)
#print("Sonni kvadratini qaytaruvchi dastur")
#savol = 'Istalgan sonni kiriting!\n'
#savol += "To'xtash uchun 'stop' deb yozing: "
#qiymat = ''
#ishora = True
#while ishora:
 #   qiymat = input(savol)
  #  if qiymat == 'stop':
   #     break
    #else:
     #   print(float(qiymat)**2)

#print("Sonni kvadratini qaytaruvchi dastur")
#savol = 'Istalgan sonni kiriting!\n'
#savol += "To'xtash uchun 'stop' deb yozing: "
#qiymat = ''
#ishora = True
#while ishora:
 #   qiymat=input(savol)
  #  if qiymat == 'stop':
   #else:
     #   print(float(qiymat)**2)
     
# break OPERATORI     
     
#print("Sonni kvadratini qaytaruvchi dastur")
#savol = 'Istalgan sonni kiriting!\n'
#savol += "To'xtash uchun 'stop' deb yozing: "
#qiymat = ''
#while True:
 #   qiymat = input(savol)
  #  if qiymat == 'stop':
   #     break
    #else:
     #   print(float(qiymat)**2)

#sonlar = list(range(1,21))
#for son in sonlar:
 #   if son == 10:
  #      break
   # else:
    #    print(f"{son} ning kvadrati {son**2} ga teng!")
#Yuqoridagi kodda dasturimiz son 10 ga yetganda to'xtayapti

# continue OPERATORI

# continue operatori esa, aksincha, ma'lum shart bajarilganda qadam tashlab 
# o'tish uchun mo'ljallangan.

#sonlar = list(range(1,21))
#for son in sonlar:
 #   if son == 12:
  #      continue
   # else:
    #    print(f"{son} ning kvadrati {son**2} ga teng")
# Yuqoridagi kodda dasturimiz son 12 ga yetganda 12 sonini tashlab ketti va
# qolganlarini davom ettirdi. braek operatori esa belgilangan songa yetganda to'xtaydi.

#Juft sonlarni topish dasturi
#son = 0
#while son<200:
 #   son+=1
  #  if son%2 != 0: # agar son toq bo'lsa
   #     continue
    #else:
     #   print(son, end=' ')
     
#Toq sonlarni topish dasturi
#son = 0
#while son <100:
 #   son+=1
  #  if son%2 == 0: #agar son 0 ga teng bo'lsa
   #     continue
    #else:
     #   print(son, end=' ')
    
# ABADIY SIKL TUZOG'I

#Abadiy siklga mantiqiy xatolar sabab bo'lishi mumkin:
    #* noto'g'ri shart, o'zgarmas qiymat, kodlar ketma-ketligidagi xatolar ...
    
#son = 0
#hile son<10:
 #       if son%2 != 0:
  #          continue
   #     else:
    #        print(son)
#yuqorida dastur abadiy davom etadi, sababi biz sonning qiymatini o'zgartirishni 
#esdan chiqardik.

#son = 0
#while son <10:
    
 #   if son%2 != 0:
  #              continue
   # else:
    #    print(son)
    #son += 1
#bu dastur ham abadiy davom etadi. sababi songa 1 ni oxirida qo'sh deb yozdik.
#else gacha yetib kelmasdan kod orqaga qaytaveradi

#son = 1
#while son > 0:
 #   son += 1
  #  if son%2 != 0:
   #     continue
    #else:
     #   print(son)
#yuqridagi dasrturda esa son > 1 bo'lgani ucgun abadiy davom etaveradi.


# savol = 'Sevimli kitoblarizi kiriting'
# savol += 'Kitoblarni kiritib b\'lgach "exit" deb yozing: '
# while True:
#     kitob = input(savol)
#     if kitob == 'exit':
#         break
# print('Rahmat')

# savol = "Yoshingizni kiriting."
# savol += "\nTo'xtash uchun 'exit' yoki 'quit' deb yozing: "
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     yosh = int(qiymat)
#     if yosh < 7:
#         narh = 2000
#     elif 7 <= yosh < 18:
#         narh = 3000
#     elif 18 <= yosh < 65: 
#         narh = 10000
#     else:
#         narh = 0
#     if narh == 0:
#         print("Sizga kirish bepul ")
#     else:
#         print(f"Sizga kirish {narh} so'm")

# savol = "Yoshingizni kiriting."
# savol += "\nTo'xtash uchun 'exit' yoki 'quit' deb yozing: "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     yosh = int(qiymat)
#     if yosh <7:
#         narx=0
#     elif 7<= yosh <18:
#         narx=5000
#     elif 18<= yosh <60:
#         narx=15000
#     else: narx = 0
#     if narx == 0:
#         print("Sizga kirish bepul")
#     else:
#         print(f"Sizga kirish {narx} so'm")

# savol = 'Kiritilgan sonning ildizini qaytaruvchi dastur.\n'
# savol += 'Musbat son kiriting: '
# savol += "(Dasturni to'xtatish uchun 'exit' deb yozing): "
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     elif float(qiymat) < 0:
#         continue
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")


# print("Do'stlaringiz ro'yhatini tuzamiz")
# dostlar = []
# n=1
# while True:
#     savol = f"{n}-do'stingiz ismini yozig: "
#     ism = input(savol)
#     dostlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (yes/no): ")
#     if javob == 'yes':
#         n+=1
#         continue
#     else:
#         break
# print("Ro'yhat tuzildi")
# for ism in dostlar:
#     print(ism.title())


# while yordamida lug'atni to'ldirish.

# while sikli yordamida lug'atlarni ham shakllantirish mumkin.
# quyidagi kodda ism bu kalit, yosh esa qiymat. 

# print("Tanishlar yoshini saqlaymiz")
# tanishlar = {}
# ishora = True
# n=1
# while ishora:
#     ism = input(f"{n}-tanishizi ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     tanishlar[ism]=int(yosh)
#     takror = input("Yana tanishiz bormi? (yes/no): ")
#     n+=1
#     if takror == "no":
#         ishora = False
# for ism, yosh in tanishlar.items():
#     print(f"{ism.title()} {yosh} yoshda")

# print("Buyurtmalaringizni kiriting!")
# mahsulotlar = []
# n=1
# while True:
#     savol = input(f"{n}-buyurtmangizni kiriting: ")
#     mahsulotlar.append(savol)
#     takror = input("Yana mahsulot qo'shasizmi? (yes/no): ")
#     n+=1
#     if takror == "no":
#         break
# print("Mahsulotlar ro'yhati tuzildi.")
# for mahsulot in mahsulotlar:
#     print(mahsulot.title(), end = ' ')

# print("Mahsulotlarni va ularni narxini kiriting!")
# mahsulotlar1 = {}
# ishora = True
# while ishora:
#     tovar = input("Mahsulot nomini kiriting:  ")
#     narx = input(f"{tovar.title()}ning narxini kiriting: ")
#     mahsulotlar1[tovar]=int(narx)
#     takror = input("Yana mahsulot qo'shasizmi? (yes/no): ")
#     if takror == "no":
#         ishora = False
# for tovar in mahsulotlar1:
#     print(tovar.title())

# mevalar = ['tarvuz', 'qovun', 'olma', 'nok', 'anjir']
# korzinka = {'tarvuz':15000,
#               'olma':10000,
#               'nok':20000,
#               'qovun':25000}
# while mevalar:
#     meva = mevalar.pop()
#     if meva in korzinka.keys():
#         narx = korzinka[meva]
#         print(f"{meva.title()} narxi {narx} so'm")
#     else:
#         print(f"{meva.title()} yo'q")

# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
#     print(f"{2022-yosh}-yilda tug'ilgansiz")
# except: 
#     print("Butun son kiritmadingiz")     
# print("Dastur tugadi")
# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
# except:
#     print("Butun son kiritmadingiz.")
# else:
#     print(f"Siz {2022-yosh} yilda tug'ilgansiz")
# x=10
# y=5
# try:
#     a=y/(15-x)
# except ZeroDivisionError:
#         print("0 ga bo'lib bo'lmaydi")
# else:
#         print(a)
        
# mevalar = ['olma', 'banan', 'uzum', 'anor', 'anjir'] 
# try:
#     print(mevalar[5])
# except IndexError:
#     print(f"Ro'yhatda {len(mevalar)}ta mevalar bor")

# user = {"username":"sariqdev",
#         "status":"admin",
#         "email":"kmuhtorov@mail.ru",
#         "phone":"903070479"}
# key = 'mail'
# try:
#     print(f"{user[key]}")
# except KeyError:
#     print(f"Bizda bunday {key} kalit mavjud emas")

# fayl = "data.txt"
# try:
#     f = open(fayl)
# except FileNotFoundError:
#     print(f"{fayl} fayli mavjud emas")

# n = input("Butun son kiriting: ")
# try:
#     n = int(n)
#     x = 20/n
# except ValueError: # agar foydalanuvchi butun son kiritmasa
#     print("Butun son kiritmadingiz")
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")
# else:
#     print(f"x={x}")

# user = {"username":"sariqdev",
#         "status":"admin",
#         "email":"kmuhtorov@mail.ru",
#         "phone":"903070479"}
# key = 'tel'
# try:
#     print(f"Foydalanuvchi: {user[key]}")
# except KeyError:
#     pass

# yosh = input("Yoshingizni kiriting: ")
# try: 
#     yosh = int(yosh)
#     print(f"Siz {2022-yosh} yilda tug'ilgansiz")
# except: # xato yuz bersa bajariluvchi kod
#     print("Butun son kiritmadingiz")
    
# while True:
#     yosh = input("Yoshingizni kiriting: ")
#     if yosh.isdigit():
#         yosh = int(yosh)
#         break
# print(f"Siz {2022-yosh} yilda tug'ilgansiz")

# x = input("Son kiriting: ")
# y = input("Yana bir son kiriting: ")
# try:
#     x=int(x)
#     y=int(y)
#     print(x, '/', y, '=', x/y)
# except ValueError:
#     print("Butun son kiritmadingiz")
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")
