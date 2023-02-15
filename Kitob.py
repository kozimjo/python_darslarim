# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 11:47:47 2022

@author: User
"""

# KITOB
#odamlar = int(input("Bugun nechta odam bilan uchrashdingiz? - "))
#ismlar = []
#for n in range(odamlar):
 #   ismlar.append(input(f"{n+1}-uchrashgan odamingizni ismini yozing - "))
#for ism in ismlar:
 #   print(ism.title())
 
# SHARTLAR VA TARMOQLANISH
#Dastur tarmoqlanishi uchun ma'lum bir shartlar bajarilishi kerak.
# yosh>4, til = o'zbek, jins = erkak

# IF ELSE OPERTORI

#son = int(input("Istalgan sonni kititing - "))
#if son >0:
 #       print(son, "Musbat son")
#else:
 #       print(son, "Manfiy son")        
#while True:
 #   takror = input("Yana son kiritasizmi? (yes/no) - ")
  #  if takror != 'yes':
   #     break
    #son2 = int(input("Kyingi sonni kiriting - "))
    #if son2>0:
     #   print(son2, "soni musbat")
   # else:
    #    print(son2, "soni manfiy")

#MATNLARNI SOLISHTIRISH

#Kompyuter uchun 'Kozim', 'KOZIM' va 'kozim' ismlari har hil ismlardir. 
#bu ismlarni solishtirish uchun bir hil ko'rinishga keltirib olamiz!
#ism = 'Kozim'
#ism.lower() == 'kozim'
#Natija: True

#avtolar = ['audi', 'bmw', 'volvo', 'kia', 'mersedes']
#for avto in avtolar:
 #   if avto == 'bmw':
  #      print(avto.upper())
   # else:
    #    print(avto.title())
# yuqoridagi kodda faqat 'bmw' uchun {avto == 'bmw' print(avto.upper())} deb 
# shart qo'yib oldik, avtolar degan ro'yhatdagi boshqa mashinalar uchun 
# print(avto. )

#javob = float(input("6*7 nechchiga teng? - "))
#if javob != 42:
 #   print("Javob hato") 
#else:
 #   print("Javob to'g'ri")

#yosh = int(input("Yoshingiz nechada? - "))
#if yosh>=18:
 #   print("Hush kelibsiz")
#else:
 #   print("Damiz oling")
    
#yil = int(input("Tug'ulgan yilingizni kiriting - "))
#if 2022-yil < 18: 
 #  print(f"{2022-yil} yoshda ekan, sizga kirish mumkin ems!")
#else:
 #   print("Marhamat kiring!")
    
#login = input("Yangi login kiriting - ")
#if len(login) <= 5:
 #   print("Login 5 harfdan ko'p bo'lishi kerak")
    
#cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
#for car in cars:
 #   if car == 'gm':
  #      print(car.upper())
   # else:
    #    print(car.title())
        
#cars = [ 'bmw', 'tesla', 'uz auto', 'mersedec','audi']
#for car in cars:
    #if car != 'bmw':
     #   print(car.title())
    #else:
        #print(car.upper())
#cars.sort()
#print(cars)  

#login = input("Loginingizni kiriting - ")
#if login == 'admin':
 #   print("Hush kelibsiz Admin, foydalanuvchilar ro'yhatini ko'rasizmi?")
#else:
  #  print(f"Hush kelibsiz {login.title()} ")
    
#son1= float(input("Birinchi sonni kiriting : ")) 
#son2 = float(input("Ikkinchi sonni kiritng : ")) 
#if son1 == son2:
 #       print("Sonlar neng ekan")
#else:
        #print("Sonlar teng emas")
   
#son = float(input("Istalgan sonni kiriting: "))
#if son >0:
 #   print(f"{son} musbat son!")
#elif son < 0:
 #   print(f"{son} manfiy son!")
#else: 
 #   print("Nol manfiy ham emas, musbat ham emas!")                     
 
#son = float(input("Qaysi sonni ildizini bilmoqchisiz? : "))
#if son > 0:
 #   print(son**0.5)
#else:
 #   print("Musbat son kiriting!")
 
#number = float(input("Istalgan sonni kiriting: "))
#if (number%2) == 0: 
  #  print("Raqam juft raqam")
#else:
 #   print("Raqam toq raqam")
 
# BIR NECHTA SHARTLARNI TEKSHIRISH

#   if - elif - else ketma ketligi :
#   if bilan boshlangan ketma-ketlik bir nechta elif-lardan iborat bo'lishi mumkin 
#yosh = int(input("Yoshingizni kiriting> "))
#if yosh <= 4:
 #   print("Sizga kirish bepul")
#elif yosh <= 12:
 #   print("Sizga kirish 5000 so'm")
#else:
 #   print("Sizga kirish 10000 so'm") 
    
#YUQORIDAGI KODNI QISQA YOZISH MUMKIN
#yosh = int(input("Yoshingiz nechada? - "))
#if yosh <= 4:
 #   price = 0
#elif yosh <=12:
 #   price = 5000
#else: 
 #   price = 10000
#print(f"Sizga kirish {price} so'm")

# AND VA OR OPERATORLARI

#kun = input("Bugun nima kun? - ")
#if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
    #print("Bugun dam olish kuni")
#else: 
    #print("Bugun ish kuni")
    #print(True or False)
    #print(True or True)
    #print(False or False)
#kun = input("Bugun qanday kun? - ")
#harorat = float(input("Harorat necha gradus? > "))
#if (kun.lower() == 'yakshanba' or kun.lower() == 'shanba') and harorat >= 35:
 #   print("Cho'milgani boramiz")
#elif (kun.lower() == 'yakshanba' or kun.lower() == 'shanba') and harorat < 35:
 #   print("Bugun uyda dam olamiz")
#else:   
 #   print("Axir bugun ish kuniku")
#OR VA AND SHARTLARI BITTA QATORDA ISHLATILGANDA OR SHARTI QATNASHGAN QISMINI () qavsga OLAMIZ!

# IKKI RO'YHATNI SOLISHTIRISH

#menu = ['osh', 'kabob', 'norin', 'somsa', 'manti', 'qozonkabob', 'sho\'rva']
#ovqatlar = ['non', 'osh', 'bosma', 'kabob', 'somsa']
#for ovqat in ovqatlar:
 #   if ovqat in menu:
  #      print(f"Menyuda {ovqat.upper()} bor")
   # else:
    #    print(f"Kechirasiz, menyuda {ovqat.upper()} yo'q")
        
# RO'YHAT BO'SH EMASLIGINI TEKSHIRISH

#list1 = [1, 2, 3]
#len(list1) > 0
#True
#list2 = []
#len(list2) >0
#False

#list_1 = [1]
#if list_1:
 #   print("Ro'yhatda elemeentlar bor")
#else: 
#    print("Ro'yhat bo'sh")
    
#menyu = ['bistrogan', 'bishteks', 'katlet', 'rulet', 'somsa', 'osh', 'kabob', 'norin']
#buyurtmalar = ['somsa', 'osh', 'norin', 'qatiq']
#if buyurtmalar:
 #  for buyurtma in buyurtmalar:
  #     if buyurtma in menyu:
   #     print(f"Bizda {buyurtma} bor")
    #   else:
     #   print(f" Kechirasiz Bizda {buyurtma} yo'q" )
#else: 
 #   print("Savatchangiz bo'sh")    
#son = int(input("Raqam kiriting")) 
#for n in range(2, 20):
 #   if not (son%n):
  #     print(f"{son} soni - {n} soniga qoldiqsiz bo'linadi") 
  
#son = int(input("Son kiriting: "))
#for n in range(2, 20):
 #   if son%n == 0:
  #      print(f"{son}-soni {n}-soniga qoldiqsiz bo'linadi")
   
# LUG'AT BILAN ISHLASH

# Pythonda lug'at kalit-qiymat juftligining yig'indisidir! Lug'atdagi biror elementning 
# qiymatini ko'rish uchun unga kalit so'z orqali murojaat qilinqdi.
#car = {'model':'ferrari', 'rang':'qizil', 'yil':2022}
#print(car['model'])
#print(car['rang'])
#print(car['yil'])    

#talaba = {'ism':'kozim muxtorov', 'manzil':'farg\'ona', 't_yil':1984, 'yosh':38}
#rint(f"{talaba['ism'].title()}",\
 #     f"{talaba['manzil'].title()} shaxrida",\
  #    f"{talaba['t_yil']}-yilda tug'ulgan", \
   #   f"{talaba['yosh']} yoshda")

#car = {'model':'bmw',
      # 'korobka':'avtomat',
     #  'yil':2022, 
    #   'probeg':0, 
   #    'rang':'qora',
  #     'narh':55000
 #      }
#print("Men tanlagan mashinani modeli-", car['model'].upper(),", rangi esa-", car['rang'], ", Ishlab chiqarilhan yili", car['yil'], "yil")

# get() METODI

#print(car['narx'])
#narx = car.get("narx", "Bunday kalit mavjud emas")
#print(narx)
#narx = car.get('narx')
#print(narx)

# Lug'atga juftlik qo'shish
# bunda lug'at nomi yoziladi va [] ichiga kalit yozilib, = dan keyin qiymat yoziladi.

#talaba = {'ism':'kozim muxtorov', 'manzil':'farg\'ona', 't_yil':1984, 'yosh':38}
#talaba['kurs'] = 4
#talaba['fakultet'] = 'energetika'
#print(talaba)

# BO'SH LUG'AT

#uzb_ing = {}

#uzb_ing['non'] = 'bread'
#uzb_ing['uy'] = 'home'
#zb_ing['hotin'] = 'wife'
#uzb_ing['kitob'] = 'book'
#print(uzb_ing)

# QIYMATNI O'ZGARTIRISH

#car = {}

#ar['model']='tesla'
#car['rang']='qizil'
#car['price']=45000
#print(car)
#car['price']=55000
#print(f"{car['model']}, rangi {car['rang']}, narxi {car['price']}$ ")

# KALIT-QIYMAT JUFTLIGINI O'CHIRISH
# Lug'atdagi elementlarni del operatori yordamida o'chiramiz

#car = {'model':'tesla', 'yil':2022, 'korobka':'avtomat', 'rang':'qizil', 'davlat':'amerika'}
#print(car)
#del car['davlat']
#print(car)

#otam = {'ism':'komoljon', 't_yil':1955, 'manzil':'mingtut', 'malumot':'o\'rta mahsus'}
#onam = {'ism':'oliyaxon', 't_yil':1958, 'manzil':'tog\'ay', 'malumot':'oliy'}
#opam = {'ism':'nazokatxon', 't_yil':1982, 'manzil':'uchkuprik', 'malumot':'oliy'}
#singlim = {'ism':'malikaxon', 't_yil':1991, 'manzil':'uchkuprik', 'malumot':'o\'rta mahsus'}
#hotinim = {'ism':'hushnuda', 't_yil':1986, 'manzil':"farg'ona", 'malumot':'oliy'}
#print(f"Dadam {otam['ism'].title()}, {otam['manzil'].title()}da, {otam['t_yil']}yilda tugilishgan.",\
 #     f"Onam {onam['ism'].title()} esa, {onam['t_yil']}yilda {onam['manzil'].title()}da tug'ilishgan")

#taomlar = {'dadam':'osh',
 #          'onam':'mastava',
  #         "o'zim":'kabob',
   #        'hotin':'osh',
    #       'qizim':'norin'
     #      } 
#print(f" Dadam {taomlar['dadam']}ni, ayam {taomlar['onam']}ni, qizim esa {taomlar['qizim']}ni yaxshi ko'rishadi") 

#python_lugat = {'float':"o'nlik son", 
#                'int':'butun son', 
 #               'list':"ro'yhat", 
  #              'string':'matn',
   #            'for':'sikl',
    #            'del':"o'chirish",
     #           'upper()':'katta harf',
      #          'title()':'bosh katta harf',
       #         'lower()':'bosh kichik harf',
        #        'and va or':'ketma-ket shartlar',
         #       '==':'teng bo\'lsaa',
          #      '!=':'teng bo\'lmasaa'}
#kalit = input("Kalit so'z kiriting : ").lower()
#print(python_lugat.get(kalit, "Bunday so'z mavjud emas"))
#tarjima = python_lugat.get(kalit)
#if tarjima == None:
 #   print("Bunday so'z yo'q")
#else:
 #   print(python_lugat.get(kalit))
 
#kalit = input("Biror so'z kiriting: ")
#print(python_lugat.get(kalit, "Bunday so'z yo'q"))
#savol = input("Biror nima so'rang: ")
#javob = python_lugat.get(savol)
#if javob == None:
 #   print("Bunday so'z yo'q")
#else:
 #   print(javob)
 
# LUGAT ELEMENTLARI BILAN ISHLASH
# items() METODI

#talaba = {'ism':'kozim',
 #         'familiya':'muxtorov',
  #        'yil':1984,
   #       'fakultet':'energetika',
    #      'manzil':'uzbekiston'
          #}
#print(talaba.items())
#print(talaba)

# Bu  metodni to'g'ridan to'g'ri emas, for sikli yordamida chiqarish orqali 
# lug'atdagi barcha elementlarni tushunarliroq shaklda ko'rishimiz mumkin.\

#for kalit, qiymat in talaba.items():
 #   print(f"Kalit: {kalit}")
  #  print(f"Qiymat: {qiymat}")
#Yuqoridagi dasturda talaba lug'atidagi har bir kalit-qiymat juftligini konsolga chiqardik.
#E'tibor bering, for siklida bir emas, ikkita o'zgaruvchi yaratib oldik (kalit-qiymat).
#Bu usul lug'atdagi ma'nolarni chiroyli ko'rinishda chiqarish uchun juda qulay.
#telefonlar = {'kozim':'mi 9s',
 #             'shukur':'mi 6',
  #            'jamshid':'galaxy s21',
   #           'murod':'iphone 13 mini',
    #          'davron':'iphone 11 Pro max'}
#for k, v in telefonlar.items():
 #   print(f"{k.title()}ning telefoni {v}")
    
# .keys() METODI.
# agar lug'atdagi kalit so'zlarni topish talab qilinsa, .keys() metodidan foydalanamiz.

#mahsulotlar = {'sabzi':3000,
 #              'kartoshka':5000,
  #             'piyoz':4000,
   #            "go'sht":85000,
    #           'non':3000,
     #          "yog'":105000}
#print(mahsulotlar.keys())
#print(mahsulotlar.values())
#print("Do'kondagi mahsulotlar va narxlari:")
#for mahsulot in mahsulotlar.keys():
     #print(f"{mahsulot}")
#for k, q in mahsulotlar.items():
    #print(f"{k.title()}ning narxi {q} so'm")
    
# RO'YHAT VA LUG'AT

# for sikli va if yordamida lyg'atdagi biror qiymatlarni alohida chiqarishimiz ham mumkin
#mahsulotlar = {'sabzi':3000,
 #              'kartoshka':5000,
  #             'piyoz':4000,
   #            "go'sht":85000,
    #           'non':3000,
     #          "yog'":105000}
#bozorlik = ['kartoshka', 'non', 'sabzi', 'baliq', 'tuz']
#for mahsulot in mahsulotlar:
 #   if mahsulot in bozorlik:
  #      print(f"{mahsulot.title()}ning narhi {mahsulotlar[mahsulot]}so'm")
#for buyum in bozorlik:
 #   if buyum not in mahsulotlar:
  #      print(f" Kechirasiz bizda {buyum} yo'q")
        
#LUG'AT ELEMENTLARINI TARTIB BILAN CHIQARISH
#Agar elementlarni alifbo tartibida chiqarish kearak bo'lsa, 
#sorted() finksiyasidan foydalanamiz

#print("Do'konimizdagi mahsulotlar")
#for m in sorted(mahsulotlar):
 #   print(m.title())
#mevalar = {'behi':15000,
 #          'hurmo':8000,
  #         'anor':16000,
   #        'shaftoli':9000,
    #       'anjir':12000,
     #      'uzum':20000,
      #     'olma':10000}
#print("Do'kinimizdagi mevalar")
#for m in sorted(mevalar):
 #   print(m.title())
#print("Mevalar narhi")
#for m, n in sorted(mevalar.items()):
 #   print(f"{m.title()}ning narxi-{n} so'm")

# .values() METODI
#Agar lug'atdagi element qiymatlarini topish kerak bo'lsa .values() metodidan foydalanamiz

#cars = {'kozim':'cobalt',
 #       'shukur':'nexia_2',
  #      'faxriddin':'matiz', 
   #     'davron':'trakker',
    #    'otabek':'lasetti'}
#print("Do'stlarimiz quyidagi mashinalarda yirishadi")
#for car in cars.values():
 #   print(car.title())
#for i, m in cars.items():
 #   print(f"{i.title()} - {m}da yuradi")
#print(cars.values())
#telefonlar = {'kozim':'mi s9',
 #             'hakim':'galaxy 9s',
  #            'kirill':'iphone 11 Pro',
   #           'faxriddin':'galaxy 9s',
    #          'shukur':'mi s9',
     #         'jamshid':'galaxy 21s',
      #        'sherzod':'galaxy 21s',
       #       'davron':'iphone 11 Pro'
        #      }
#print("Foydalanuvchilarning telefonlari")
#for tel in telefonlar.values():
 #   print(tel)
    
#Yuqorida telefonlar ro'yhatida bix him markadagi telefonlarni qayta qayat 
#konsolga chiqardi. Agar bir xil turdagi qiymatlarni faqat bittasini chiqarish 
#kerak bo'lsa set() funksiyasidan foydalanamiz.
#for tel in set(telefonlar.values()):
 #   print(tel)

#python_lugat = {'float':"o'nlik son", 
 #               'int':'butun son', 
  #              'list':"ro'yhat", 
   #             'string':'matn',
    #            'if':'shartlarni tekshirish operatori',
     #           'for':'biror amalni qayata-qayta bajarish sikl',
      #          'del':"o'chirish",
       #         'upper()':'katta harf',
        #        'title()':'bosh katta harf',
         #       'lower()':'bosh kichik harf',
          #      'and va or':'ketma-ket shartlar',
           #     '==':'teng bo\'lsaa',
            #    '!=':'teng bo\'lmasaa'}
#for k, q in sorted(python_lugat.items()):
    #print(f"{k} - {q}")

countries = {'turkmaniston':'ashxabod',
             'tojikiston':'dushanbe',
             "qig'iziston":'bishkek',
             "qozog'iston":'ostona',
             'amerika':'vashington',
             'rossiya':'moskva',
             "o'zbekiston":'toshkent',
             'xitoy':'pekin',
             'yaponiya':"tokyo",
             'angliya':'london', 
             'fransiya':'parij',
             'kanada':'ottava',
             'avstraliya':'kanberra',
             'braziliya':'brazilia',
             'argentina':'buenos-aires',
             }
#davlat = input("Qaysi davlatning poytahtini bilmoqchisiz? : ").lower()
#poytaht = countries.get(davlat, "Kechirasiz bizda Bu davlat haqida ma'lumot yo'q")
#print(poytaht.title())
#if poytaht == None:
 #   print("Kechirasiz bunday davlat haqida ma'lumot yo'q")
#else:
 #   print(f"{davlat.title()}ning poytahti - {poytaht.title()}")
#davlat = input("Qaysi davlatni poytahtini bilmoqchisiz? : ").lower()
#poytaht = countries.get(davlat)
#if poytaht == None:
 #   print("Kechirasiz bizda bu davlat haqida ma'lumot yo'q")
#else:
 #   print(f"{davlat.title()}ning poytahti {poytaht.title()}")
 
#menu = {'osh':25000,
 #       "sho'rva":20000,
  #      'kabob':18000,
   #    'mastava':15000,
    #    'bistrogi':20000,
     #   'bifshteks':22000,
      #  'lag\'mon':17000,
       # 'chuchvara':17000,
        #'donar':35000}
#print("3 ta taomga buyurtma bering.")
#ovqatlar = []
#for n in range(3):
 #   ovqatlar.append(input(f"{n+1}-taomga buyurtma bering : "))
#for ovqat in ovqatlar:
 #   if ovqat in menu:
  #      print(f"{ovqat}ning narhi {menu[ovqat]} so'm")
   # else:
    #    print(f"Kechirasiz bizda {ovqat} yo'q")
    
#TO'PLAMLAR

# To'plam (set) ma'lumot turi bo'lib, ro'yhat va lug'at kabi 
#bir nechta elementlarni saqlsh mumkin.
#To'plam yaratish uchu ham katta (jingalak) qavsdan foydalanamiz.

#sonlar = {1, 2, 3, 4, 5}
#print(sonlar)

#ismlar = {'ali', 'vali', 'gani', 'qani'}
#print(ismlar)

#To'plam bir hil elementlarni saqlamaydi.
#sonlar = {1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 2}
#print(sonlar)
#smlar = {'kozim', 'nozim', 'azim', 'kozim', 'kaka', 'nozim', 'ahad'}
#print(ismlar)

#Bo'sh to'plam yaratish uchun set() funksiyasidan foydalanamiz.
#a = set() #bo'sh to'plam

#Ro'yhatdan farqli ravishda set() ichidagi elementlar biror tartibda saqlanmaydi,
# va ularga indeks orqali murojaat qilib bo'lmaydi.

#print(sonlar[0]) #TypeError: 'set' object is not subscriptable

#To'plamlar biror ro'yhatdagi qaytarilgan elementlarni o'chirib tashlash uchun 
#juda qulay.

#mevalar = ['olma', 'anjir', 'banan', 'olma', 'anjir', 'banan']
#mevalar = set(mevalar) 
#print(mevalar)

#Agar to'plamni ro'yhatga o'tkazish talab qilinsa list() funksiyasidan foydalanamiz.

#mevalar = list(mevalar)
#mevalar.append('anor')
#print(mevalar)

#TO'PLAMGA ELEMENT QO'SHISH.

#To'plamga yagona elemnt qo'shish uchun .add() metodidan, 
#bir nechta element qo'shish uchun esa .update() metodidan foydalanamiz.

#sabzavotlar = {'bodring', 'pomidor', 'karam', 'bolgar',}
#print(sabzavotlar)
#sabzavotlar.add('chesnok')
#print(sabzavotlar)
#sabzavotlar.update(['bqalajon', 'kashnich', 'oshqovoq'])
#print(sabzavotlar)
#ESLATMA. .update() funksiyasidan foydalanganda .update([])-shaklida yoziladi.
#Ya'ni () ichiga [] to'rtburchak qavs ham yoziladi.
#sabzavotlar.update(['petrushka'])
#print(sabzavotlar)
#sabzavotlar.update(['don', 'non', 'jon'])
#print(sabzavotlar)

#TO'PLAMDAN ELEMENT O'CHIRISH

#To'plamdan element o'chirish uchun .discard() va .remove() metodlari bor.
#mevalar = {'olma', 'anor', 'uzum', 'banan', 'behi', 'nok'}
#print(mevalar)
#mevalar.discard('olma')
#print(mevalar)
#mevalar.discard('uzum')
#mevalar.remove('anor')
#mevalar.remove('behi')
#mevalar.remove('banan')
#print(mevalar)
#mevalar.discard('nok')
#print(mevalar)

# .discard() va .remove() elementlari bitta vazifani bajaradi, 
#ularnig farqi shuki, agar biz qaytarmoqchi bo'lgan element 
#to'plamda yo'q bo'lsa . remove() metodi hato qaytaradi, .discard() esa 
#hato qaytarmaydi.

#sonlar = {1, 2, 3, 5, 6}
#sonlar.remove(4)
#print(sonlar)
#sonlar.discard(4)
#print(sonlar)

#To'plamdan element ochirishning (sug'urib olishning) yana bir usuli 
# .pop() metodidir. Lekin to'plam elementlari indeksi mavjud bo'lmagani uchun 
# .pop () metodi to'plamdan tasodifiy elementni sug'urib oladi.
#son = sonlar.pop()
#print(son)
#print(sonlar)
#sonlar.pop()
#sonlar.pop()
#son = sonlar.pop()
#print(son)
#print(sonlar)


#TO'PLAMLAR USTIDA AMALLAR

#To'plamlar ustida matematik amallarni ham bajarish mumkin.
#Ikki to'plamni birlashtirish uchun "|" - operatori yoki .union() metodidan foydalanamiz

#A = {1, 2, 3, 4}
#B= {3, 4, 5, 6, 7}
#c = A|B
#print(c)
#d= A.union(B)
#print(d)
#mevalar = {'olma', 'anor', 'anjir', 'pomidor'}
#sabzavotlar = {'bodring', 'pomidor', 'oshqovoq'}
#mev_sab = mevalar|sabzavotlar
#print(mev_sab)
#ms = mevalar.union(sabzavotlar)
#print(ms)

#To'plamlarni birlashtirganda ikki to'plam ichidagi bir hil elementlar
#takror chiqarilmaydi. Faqat bittasi chiqariladi.

#Ikki to'plamning kesishmasini yoki (bir hil elementlarini) topish uchun 
# "&"-operatoridan yoki .intersection() metodidan foydalanamiz.
#print(A&B) 
#print(A.intersection(B))
#print(mevalar&sabzavotlar)
#print(mevalar.intersection(sabzavotlar))

#Ikki to'plam orasidagi farqni tipish uchun esaa (-) operatoridan foydalanamiz 
# yoki .diference() metodidan foydalanamiz.
# B to'plamning A to'plamdan farqi deganda (A-B) A to'plamga kiruvchi, lekin 
# B to'plamda yo'q elementlar tushuniladi.
#print(A-B) 
#print(B-A)
#print(A.difference(B))
#print(B.difference(A))

#To'plam orasidagi farqni simmetrik topish uchun ^ operatori yoki 
# .symmetric_difference()metodidan foydalanamiz.
# Simmetrik farq deb A va B to'plamga kiradigan, lekin bir vaqtda ikkalasiga 
# kirmaydigan elementlar tushuniladi. Ikkalasida ham bori simmetrik farqqa kirmaydi
#print(A^B) 
#print(A.symmetric_difference(B))

#ranglar = {'qizil', 'sariq', 'yashil'}
#ranglar.add('ko\'k')
#ranglar.update(['qora', 'oq'])
#ranglar.add('kulrang')
#print(ranglar)

#set1 = {10, 20, 30, 40, 50}
#set2 = {30, 40, 50, 60, 70}
#set3 = (set1&set2)
#print(set3)
#print(set1-set2)
#print(set2-set1)
#print(set1^set2)
#print(set1.symmetric_difference(set2))

#bozorlit = {'choy', 'non', 'kartoshka', 'tuxum', 'sut'}
#mahsulotlar = {'non', 'sut', 'tuxum', 'olma', 'un', 'tuz'}
#mahsulot = bozorlit.intersection(mahsulotlar)
#print(mahsulot)
#print(bozorlit-mahsulotlar)
#mahsulotlar.update(['choy', 'kartoshka'])
#print(mahsulotlar)
#print(bozorlit-mahsulotlar)
#print(mahsulotlar-bozorlit)

#ranglar ={'qizil', 'ko\'k', 'yashil'}
#ranglar.add('oq')
#ranglar.update(['qora', 'sariq', 'pushti', 'kulrang'])

#set1 = {10, 20, 30, 40, 50}
#set2 = {30, 40, 50, 60, 70}
#set3 = set1&set2
#print(set1.intersection(set2))
#print(set1^set2)
#print(set2.symmetric_difference(set1))

#bozorlik = {'choy', 'non', 'kartoshka', 'tuxum', 'sut'}
#mahsulotlar = {'non', 'sut', 'tuxum', 'olma', 'un', 'tuz'}
#mahsulot = mahsulotlar&bozorlik
#print(mahsulot)
#print(bozorlik.difference(mahsulotlar))
#print(bozorlik-mahsulotlar)
#mahsulotlar.update(['choy', 'kartoshka'])
#print(mahsulotlar)
#print(bozorlik-mahsulotlar)


