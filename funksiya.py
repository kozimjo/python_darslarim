# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 12:38:46 2023

@author: User
"""

# FUNKSIYA

    # Funksiya ma'lum bir vazifani bajrishga mo'ljallangan kodlar yig'indisidir. 
# Funksiyalar, odatda, ma'lumotlarni qabul qilib oladi, 
#ularni qayta ishlaydi va biror natija qaytaradi.
# Misol uchun print() funksiyasi matn yoki ifoda qabul qiladi va uni 
#konsolga chiqaradi, rang() funksiyasi esa ma'lum oraliqdagi 
#sonlarni yaratish uchun ishlatiladi. 
    # Aslida, xar qanday funksiyaning ortida ham bir necha qatordan iborat 
#kod bo'ladi, lekin biz funksiyaga murojaat etganda uning nomini yozamiz holos. 
#Funksiya ortidagi kod esa biz uchun yashirin bo'lib qolaveradi. Funksiyalarning
#qulayligi ham shunda. Dastur davomida ma'lum kodlarni qayta qayta yozmaslik 
#uchun biz ularni jamlab, bitta funksiya ichiga joylashimz va dastur davomida 
#bu kodlarga fnksiya nomi orqali murojaat etishimiz mumkin. 

# Oddiy funksiya yaratamiz. Bu funksiyaga mutojaat etganimizda "Assalomu alaykum"
#degan habarni chiqarsin.

# def salom_ber():
#     """Salom beruvchi funksiya""" # docstring
#     print("Assalomu alaykum!")

# #Biz bu yerda Pythonga def operatori orqali funksiya yaratayotganimizni bildirdik.
# # def dan so'ng funksiyamizga 
# salom_ber()
# def alik_ol():
#     """Salomga alik oluvchi funksiya""" # docstring
#     print("Va alaykum assalom!")


# Qiymat Qabul qilivchi funksiya
# def salom_ber(ism):
#     """Foydalanuvchiga salom beruvchi funksiya""" #docstring
#     print(f"Assalomu alaykum! hurmatli {ism.title()} aka")

# FUNKSIYAGA BIR NECHTA ARGUMENT UZATISH

# def toliq_ism(ism, familiya):
#     """Foydalanuvchining to'liq ismini qaytaruvchi funksiya""" #docstring
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
# toliq_ism('kozim', 'muxtorov')

# def yosh_hisobla(ism, tyil):
#     """Foydalanuvchi yoshini hissoblovchi funksiya"""
#     print(f"{ism.title()} {2023-tyil} yosha")

# yosh_hisobla(ism='kozim', tyil=1984)

# def yos_hisobla(ism, tyil):
#     """Foydalanuvchi yoshini hissoblovchi funksiya"""
#     print(f"User name: {ism.title()}\n"
#           f"Age: {2023-tyil}")
# yos_hisobla(ism='kozim', tyil=1984)

# def yosh_hisobla(ism, tyil):
#     """Foydalanuvchini yoshini chiqaruvchi funksiya"""
#     print(f"{ism} {2023-tyil} yoshda")

# yosh_hisobla(tyil=1984, ism='kozim')

# STANDART QIYMAT

# def yosh_hisobla(tugilgan_yil, joriy_yil=2023):
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
# yosh_hisobla(1984)

#Funksiyaga murojaat etishdagi hatoliklar
# def yosh_hisobla(tugilgan_yil, joriy_yil=2023):
#     """Tug'ilgan yildan yoshini hisoblaymiz"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
# tyil = int(input("Tug'ilgan yilingizni kiriting:"))
# yosh_hisobla(tyil)
# def yosh_hisobla(tugilgan_yil, joriy_yil=2023):
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
# yosh_hisobla(1986)
# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum")
# salom_ber()
# def toliq_ism(ism, familiya):
#      print(f"Foydalanuvchi ismi: {ism.title()}\n"
#            f"Foydalanuvchi familiyasi: {familiya.title()}")
# toliq_ism('kozim', 'muxtorov')
# def tug_yil(ism, yosh):
#     """Foydalanuvchidan yoshini so'rab, yilini chiqaruvchi funksiya"""
#     print(f"Hurmatli {ism.title()} siz {2023-yosh} yilda tug'ilgansiz")
# ism = input("Ismingizni kiriting: ")
# yosh = int(input("Yoshingizni kiriting: "))
# tug_yil(ism, yosh)
# def kv_kub(son):
#     """Kvadrat va kubni hissoblovchi funksiya"""
#     print(f"{son} ning kvadrati {son**2}ga teng. {son} ning kubi {son**3}ga teng")
# son = int(input("Istalgan sonni kiriting: "))
# kv_kub(son)
# def juft_toq(son):
#     """Foydalanuvchidan son olib juft yoki toqligini aniqlovchi funksiya"""
#     if son%2:
#         print(f"{son} toq son")
#     else:
#         print(f"{son} juft son")
# son = int(input("Istalgan sonni kiriting: "))
# juft_toq(son)
# def katta_son(x, y):
#     """Katta sonni aniqlovchi funksiya"""
#     if x>y:
#         print(f"{x} soni {y} dan katta")
#     elif x==y:
#         print("Sonlar teng")
#     else:
#         print(f"{x} soni {y} dan kichik")
# x = int(input("Birinchi sonni kiriting: "))
# y = int(input("Ikkinchi sonno kiriting: "))
# katta_son(x, y)

# def daraja_top(x, n):
#     """Sonning darajsini aniqlovchi funksiya"""
#     print(f"{x} ning {n}-darajasi {x**n} ga teng")
# x = int(input("Darajalanuvchini kiriting: "))
# n = int(input(f"{x}ning Nechanchi darajasini bilmoqchisiz?: "))
# daraja_top(x, n)
# def daraja(x, n=2):
#     """Darajani aniqlovchi funksiya"""
#     print(f"{x} ning {n} darajasi {x**n} ga teng")
# daraja(88)
# def qoldiq(son):
#     for n in range(2,11):
#         if not son%n:
#             print(f"{son} {n} ga qoldiqsiz bo'linadi")
# qoldiq(20)
# def toliq_ism_yasa(ism, familiya):
#     """To'liq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism
# talaba1 = toliq_ism_yasa('faxriddin', 'umarov')
# talaba2 = toliq_ism_yasa('leonel', 'messi')
# print(f"Darsga kelmaganlar: {talaba1.title()} va {talaba2.title()}")

# def toliq_ism_yoz(ism, familiya, otasi):
#     """To'liq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya} {otasi}"
#     return toliq_ism.title()
# ishchi1 = toliq_ism_yoz('kozim', 'muxtorov', 'komolovich')
# ishchi2 = toliq_ism_yoz('shukur', 'abdullayev', 'adhamovich')
# print(f"Ishchilarimiz ro'yhati: {ishchi1} va {ishchi2}")

#IXTIYORIY ARGUMENTLAR

# def talabalar_ismi(ism, familiya, otasi = ''):
#     """To'liq ismlarni chiqaruvchi funksiya"""
#     if otasi:
#         ismlar = f"{ism} {familiya} {otasi}"
#     else:
#         ismlar = f"{ism} {familiya}"
#     return ismlar.title()
# talaba_1 = talabalar_ismi('diyor', 'mahkamov')
# talaba_2 = talabalar_ismi('rustam', 'inoyarov', 'jallodovich') 
# print(f"Talabalrimiz ro'yhati: {talaba_1} va {talaba_2}")   

# Funksiyadan lug'at qaytarish

# def talabalr_info(ismi, manzili, yili, fakulteti, turmushi=None):
#     """Talabalar haqida ma'lumot beruvchi funksiya"""
#     talaba = {'ismi':ismi,
#                "manzili":manzili,
#                'yili':yili,
#                "fakulteti":fakulteti,
#                'turmushi':turmushi}
#     return talaba
# talaba1 = talabalr_info('kozim muxtorov', 'quqon', 1984, 'energetika', 'oilali')
# talaba2 = talabalr_info('xushnuda kasimova', "farg'ona", 1986, 'sotsiologiya')
# talabalar = [talaba1, talaba2]
# print("Institutimiz talabalari to'yhati")
# for talaba in talabalar:
#     if talaba:
#         turmushi = talaba['turmushi']
#     else:
#         turmushi = "nomalum"
#     print(f"{talaba['ismi'].title()}ning manzili {talaba['manzili'].title()}:", 
#           f"tug'ilgan yili {talaba['yili']} yil, oilaviy holati - {talaba['turmushi']}")

#FUNKSIYADAN RO'YHAT QAYTARAMIZ

# def oraliq(a, b):
#     sonlar = []
#     while a<b:
#         sonlar.append(a)
#         a += 1
#     return sonlar
# print(oraliq(0,11))
# print(oraliq(11,31))
# def oraliq(min, max):
#     sonlar = []
#     while max>min:
#         sonlar.append(min)
#         min += 1
#     return sonlar
# print(oraliq(1, 11))

# def masofa(x, y, z = ''):
#     yulak = [] #bo'sh ro'yhat
#     while x<y:
#         if z:
#             yulak.append(x)
#             x+=z
#     return yulak
# print(masofa(0, 21, 2))
# def oraliq(min, max):
#     son = []
#     while min<max:
#         son.append(min)
#         min += 1
#     return son
# print(oraliq(1, 15))

# def oraliq(x, y):
#     sonlar = []
#     while x<y:
#         sonlar.append(x)
#         x+=1
#     return sonlar
# print(oraliq(1, 11))

# def oraliq(x, y, z=''):
#     sonlar = []
#     while x<y:
#         if z:
#             sonlar.append(x)
#             x+=z
#     return sonlar
# print(oraliq(0, 21, 4))
# def cub(number):
#     return number*number*number
# son = cub(10)    
# print(son)
# def avto_info(kompaniya, model, rangi, korobka, yili, narxi):
# #     avto = {'make':kompaniya,
# #             'modeli':model,
# #             'rangi':rangi,
# #             'korobkasi':korobka,
# #             'yili':yili,
# #             'narxi':narxi}
#     print("Saytimizdagi avtolar ro'yhatini shakllantiramiz.")
# avtolar = []
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting: " , end = '')
#     kompaniya = input("Ishlab chiqaruvchi: ")
#     model = input("Modeli: ")
#     rangi = input("Rangi: ")
#     korobka = input("Korobkasi: ")
#     yili = input("Ishlab chiqarilgan yili: ")
#     narxi = input("Narxi: ")
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narxi))
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob == "no":
#         break
# def user_info(ism, familiya, yil, manzil, yosh, email, tel):
#     """Foydalanuvchi haqida to'liq ma'lumot beruvchi funksiya"""
#     user = {"ismi":ism,
#             "familiyasi":familiya,
#             "yili":yil,
#             "manzili":manzil,
#             "yoshi":yosh,
#             "epochtasi":email,
#             "tel raqami":tel}
#     return user
# users = []
# while True: 
#     ism = input("Ims kiriting: ")
#     familiya = input("Familiya kiriting: ")
#     yil = int(input("Tug'ilgan yil kiriting: "))          
#     manzil = input("Manzil kiriting: ")
#     yosh = int(input("Yosh kiriting: "))
#     email = input("Elektron pochta kiriting: ")
#     tel = int(input("Tel raqam kiriting: "))
#     users.append(user_info(ism, familiya, yil, manzil, yosh, email, tel))
#     javob = input("Yana ma'lumot kiritasizmi? (yes/no): ")
#     if javob == "no":
#         break 
    
# for user in users:
#    print(f"{user['ismi'].title()} {user['familiyasi'].title()}, {user['yili']} yil ,",
#           f"{user['manzili'].title()}da tug'ilgan.",
#           f"{user['yoshi']}yoshda, tel raqami {user['tel raqami']}, e-pochtasi - {user['epochtasi']}")
# def katta_son(x, y, z):
#     """Son qabul qilib eng kattasini qaytaruvchi funksiya"""
#     max = x
#     if y>=max:
#         max=y
#     if z>=max:
#         max = z
#     return max
# print(katta_son(6, 7, -8))    
# def aylana_info(radius, p=3.14):
#     aylana = {"radius":radius,
#               'diametr':radius*2,
#               'perimetr':2*radius*p,
#               'yuza':p*radius**2}
#     return aylana
# print(aylana_info(6))

#Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing 
#(tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)
# def tub_sonlar_top(min,max):    
#     tub_sonlar = []    
#     for n in range(min,max+1):
#         tub = True
#         if (n==1):
#             tub = False
#         elif(n==2):
#             tub = True
#         else:
#             for x in range(2,n):
#                 if(n%x==0):
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
                
#     return tub_sonlar

# print(tub_sonlar_top(1, 99))
# def tub_sonlar(min, max):
#     tubsonlar = []
#     for n in range(min, max+1):
#         tub =True
#         if (n==1):
#             tub = False
#         elif (n==2):
#             tub = True
#         else:
#             for x in range(2, n):
#                 if (n%x==0):
#                     tub = False
#         if tub:
#             tubsonlar.append(n)
#     return tubsonlar
# print(len(tub_sonlar(1, 1000)))
#Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi 
#ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing. 
#Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan 
#ketma-ketlik Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had 
#ko’pincha 1 deb olinadi. 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...
# def fibonacci(n):
#     sonlar = []
#     for x in range(n):
#         if x==0 or x==1:
#             sonlar.append(1)        
#         else:
#             sonlar.append(sonlar[x-1]+sonlar[x-2])
#     return sonlar

# print(fibonacci(100))


# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=baho
#     return baholar

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(baholar)

# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"{ism.title()}ning bahosini qo'ying: ")
#         baholar[ism] = int(baho)
#     return baholar
# talabalar = ['mansur', 'fayzulloh', 'feruz', 'umid', 'axror']
# baholar = bahola(talabalar[:])
# print(baholar)
# print(talabalar)

# def bosh(listlar):
#     listlar = listlar[:]
#     for ism in range(len(listlar)):
#         listlar[ism]=listlar[ism].title()
#     return listlar
# ismlar = ['kozim', 'nozim', 'toyir', 'zoyir']
# yangi = bosh(ismlar)
# bosh(ismlar)
# print(ismlar)
# print(yangi)

# talabalar = ['kaka', 'ronaldo', 'messi']
# def bahola(ismlar):
#     baholar={}
#     for ism in ismlar:
#         baho = input(f"Talaba {ism.title()}ni Baholang: ")
#         baholar[ism]=baho
#     return baholar

# baholar = bahola(talabalar)
# print(baholar)
# print(talabalar)

