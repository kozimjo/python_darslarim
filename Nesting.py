# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 11:38:25 2022

@author: User
"""

# NESTING 

#Lug'at ichida lug'at, yoki ro'yhat ichida lug'at.

#Lug'atlar ro'yhati

car0 = {'model':'cobalt', 
        'rang':'kulrang',
        'yil':2013,
        'narx':9000,
        'km':215000,
        'korobka':'mexanika'}

car1 = {'model':'nexi-2',
        'rang':'mokriy asfalt', 
        'yil':2010, 
        'narx':6000,
        'km':250000,
        'korobka':'mexanika'}
car2 = {'model':'gentra',
        'rang':'oq', 
        'yil':2022, 
        'narx':16000,
        'km':0,
        'korobka':'avtomat'}

#car = car0
#print(f"Model-{car['model']},\
 #     rangi-{car['rang']},\
  #    yili-{car['yil']},\
   #   probeg-{car['km']},\
    #  korobkasi-{car['korobka']},\
     # narxi-{car['narx']}$")
#car = car1
#print(f"Model-{car['model']},\
 #     rangi-{car['rang']},\
  #    yili-{car['yil']},\
   #   probeg-{car['km']},\
    #  korobkasi-{car['korobka']},\
     # narxi-{car['narx']}$")
#car = car2
#print(f"Model-{car['model']},\
 #     rangi-{car['rang']},\
  #    yili-{car['yil']},\
   #   probeg-{car['km']},\
    #  korobkasi-{car['korobka']},\
     # narxi-{car['narx']}$")
#Bundan ham osonroq yo'li bor

#Buning uchun barcha lug'atlarni bitta ro'yhatga jamlaymiz,
#va for siklidan foydalanamiz.

#cars = [car0, car1, car2]
#for car in cars:
    #print(f"Model-{car['model']},\
     # rangi-{car['rang']},\
      #yili-{car['yil']},\
      #probeg-{car['km']},\
      #korobkasi-{car['korobka']},\
      #narxi-{car['narx']}$")
#Ro'yhat ichidagi istalgan lug'atga indeks bo'yicha murojaat etish ham mumkin.
#print(cars[2])
#Lug'atdagi elementga mutojaat etish uchun esa quyidagiz usuldan foydalanamiz.
#print(cars[2]['model'], cars[2] ['narx'], cars[0]['narx'])
#print(f"{cars[2]['model']}",
 #     f"{cars[2]['rang']}",
  #    f"{cars[2]['narx']}")

#for sikli yordamida, bo'sh lug'atlar ro'yhatini ham yaratib olish mumkin.

#cobalts = []
#for n in range(10):
 #   new_car = {'model':'cobalt',
  #             'rang':None,
   #            'yil':2022,
    #           'narx':None,
     #          'km':0,
      #         'korobka':'avto'}
    #cobalts.append(new_car)
#for cobalt in cobalts[:3]:
 #   cobalt['rang'] = 'stalnoy'
#for cobalt in cobalts[3:7]:
 #   cobalt['rang'] = 'qora'
#for cobalt in cobalts[7:]:
 #   cobalt['rang'] = 'oq'
#for cobalt in cobalts[:4]:
 #   cobalt['korobka'] = 'mexanika'
#for cobalt in cobalts:
 #   if cobalt['korobka'] == 'avto':
  #      cobalt['narx']=15000
   # else:
    #    cobalt['narx']=11000
#for cobalt in cobalts:
 #   print(cobalt.values())

#cobalts = []
#for n in range(10):
 #   new_car = {'model':'cobalt',
  #             'yil':2022,
   #            'rang':None,
    #           'narx':None,
     #          'korobka':'avto', 
      #         'km':0}
    #cobalts.append(new_car)
#for cobalt in cobalts[:5]:
 #   cobalt['rang']='qizil'
#for cobalt in cobalts[5:]:
 #   cobalt['rang']='oq'
#for cobalt in cobalts[:5]:
 #   cobalt['korobka']='mexanika'
#for cobalt in cobalts:
 #   if cobalt['korobka']=='mexanika':
  #      cobalt['narx']=12000
   # else:
    #    cobalt['narx']=16000
#for cobalt in cobalts:         
 #   print(cobalt.values())
 
#LUG'AT CIHIDA RO'YHAT

#Bir kalitga bir nechta qiymatlar berish talab etilsa qiymatlarni ro'yhat 
# ko'rinishida yozish o'rinlidir.
#Misol uchun bir tashkilotda bir nechta dasturchilar ishlaydi va har bir 
#dasturchi turli daasturlash tillarini biladi.

#dasturchilar = {'faxriddin':['python', 'c++'],
 #               'muzaffar':['java script', 'c#'],
  #              'kozim':['python', 'sql', 'r'],
   #             'zohid':['html', 'java script'],
    #            'maryam':['front end']}
#for ism, tillar in dasturchilar.items():
 #   print(f"\n{ism.title()}:", end = ' ')
  #  for til in tillar:
        #print(f"{til.upper()}", end = ' ')
#Yuqoridagi lug'at ichidagi ro'yhatda kalitdan keyin qiymatni [] to'rtburchak 
# qavs ichiga oldik.


#LUG'AT ICHIDA LUG'AT.

#Lug'at ichida lug'atni quyidagicha yozamiz. lug'atni kalitini qiymatini ham 
#lug'at qilib olamiz.

#hamkasblar = {
 #   'faxriddin':{'familiya':'mutalifov',
  #               'yil':1988,
   #              'malumot':'oliy',
    #             'tillar':['python', 'c#']
     #            },
    #'shukur':{'familiya':'abdullayev',
     #         'yil':1985,
      ##       'tillar':['java script', 'c++']
        #      },
    #'kozim':{'familiya':'muxtorov',
     #        'yil':1984,
      #       'malumot':'oliy',
       #      'tillar':['python', 'sql', 'r']}
    #}
#for ism, info in hamkasblar.items():
 #   print(f"\n{ism.title()} {info['familiya'].title()},"
  #        f"{info['yil']}-yilda tug'ulgan.\n",
   #       f"Ma'lumoti: {info['malumot']}.\n",
    #      "Quyidagi tillarni biladi")
    #   print(til.upper())

#elon = {'familiyasi':'elon mask',
 #       'sohasi':'tadbirkor',
  #      'vatani':'amrika',
   #     'yil':1971,
    #    'asarlari':['tesla', 'starlink', 'spasex']}
#alisher = {'familiyasi':'alisher navoiy',
 #          'sohasi':'shoir',
  #         'vatani':"o'zbekiston",
   #        'yil':1441,
    #       'asarlari':['hamsa', 'farhod-shirin']}
#ibn_sino = {'familiyasi':'ibn sino',
 #           'sohasi':'tibbiyot',
  #          'vatani':"o'zbekiston",
   #        'asarlari':['tib ilmi', 'shariat ilmi']}
#michael = {'familiyasi':'michael jackson',
 #       'sohasi':'san\'at',
  #      'vatani':'amrika',
   #     'yil':1958,
    #    'asarlari':['black or white', 'star']}

#mashxurlar = [elon, alisher, ibn_sino, michael]
#for shaxs in mashxurlar:
 # familiyasi = shaxs['familiyasi']
  #sohasi = shaxs['sohasi']
  #vatani = shaxs['vatani']
  #yil = shaxs['yil']
  #asarlari = shaxs['asarlari']
  #print(f"Ismi {familiyasi.title()}, ",
   #     f"Asarlari {asarlari}")
   
#seriallar = {'iroda':['saroy javohiri', 'qalbim chechagi', 'qashqirlar'],
 #            'hushnuda':['qish sonatasi', 'qora deniz', 'muhtasham 100 yil'],
  #           'kozim':['qashqirlar', 'turmadan qochish', 'tahtlar uyini']}
#for ism, serial in seriallar.items():
 #   print(f"\n{ism.title()}ning sevimli seriallari:")
  #  for kino in serial:
   #     print(kino.title())
   
davlatlar = {'amerika':{'capital':'washington',
                        'area':'3,796,742 km2',
                        'population':'331,893,745',
                        'GDP':'$25.035 trillion'},
             'canada':{'capital':'ottawa',
                        'area':'9,984,670 km2',
                        'population':'39,292,355',
                        'GDP':'$2.240 trillion'},
             'braziliya':{'capital':'brazilia',
                        'area':'8,515,767 km2',
                        'population':'217,240,060',
                        'GDP':'$3.680 trillion'},
             'argentina':{'capital':'buinos aires',
                        'area':'2,780,400 km2',
                        'population':'47,327,407',
                        'GDP':'$1.207 trillion'},
             'egipt':{'capital':'cairo',
                        'area':'1,010,408 km2',
                        'population':'107,770,524',
                        'GDP':'$1.493 trillion'},
             'janubiy afika':{'capital':'pretoria',
                        'area':'1,221,037 km2',
                        'population':'60 604 992',
                        'GDP':'$949 billion'},
             'morocco':{'capital':'robot',
                        'area':'446,300 km2',
                        'population':'37,984,655',
                        'GDP':'$359.671 billion'},
             "o'zbekiston":{'capital':'toshkent',
                        'area':'448,978 km2',
                        'population':'36,001,262',
                        'GDP':'$335.222 billion'}
             }
#savol = input("Qaysi davlat haqida bilmoqchisiz?: ").lower()
#if savol in davlatlar:
 #   info=davlatlar[savol]
    
  #  print(f"\n{savol.title()}ning poytahti {info['capital'].title()}.",
   #       f"\nMaydoni-{info['area']}.",
    #     f"\nYalpi daromadi -{info['GDP']}")
#else:
 #   print("Kechirasiz bizda bunday davlat haqida ma'lumot yo'q")

