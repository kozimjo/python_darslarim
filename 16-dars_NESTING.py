#16-DARS. NESTING
malibus=[]
for n in range(10):
    new_car={'model':'malibu',
             'yil':2022,
             'rang':None, #rangi noma'lum
             'km':0,
             'korobka':None, 
             'narh':None #narhi noma'lum
             }
    malibus.append(new_car)
#for malibu in malibus:
        #print(malibu)
for malibu in malibus[:3]:
    malibu['rang']='qizil'
    malibu['korobka']='avto'
    for malibu in malibus[3:7]:
     malibu['rang']='oq'
     malibu['korobka']='mehanika'
    for malibu in malibus[6:]:
     malibu['rang']='qora'
     malibu['korobka']='avto'
car0={'model':'nexia 3', 
      'rang':'oq',
      'yil':2021,
      'km':0,
      'korobka':'mehanika',
      'narh':9000
      }
car1={'model':'gentra', 
      'rang':'qora',
      'yil':2022,
      'km':0,
      'korobka':'avtomat',
      'narh':13000
      }
car2={'model':'kobalt', 
      'rang':'kulrang',
      'yil':2022,
      'km':0,
      'korobka':'mehanika',
      'narh':11000
      }
car=car2 #car0=car deb olganimizi sababi print qilganimizda,
         # har safar car0 o'rniga car deb yozamiz, 
         #car0ni car1 ga almshtirish ham oson bo'ladi.
#print(f"Modeli-{car['model'].title()}, " 
      #f"rangi {car['rang']}," 
      #f"ishlab chiqarilgan yili {car['yil']} yil," 
      #f"narhi {car['narh']}$," 
      #f"yurgan masofasi {car['km']}km,"  
      #f"korobkasi-{car['korobka']}")
# YUQORIDAGIDAN ham oson yo'li bor! 
#Buning uchun cars=[car0, car1, car2] degan ro'yhat yaratib olamiz.
#cars=[car0, car1, car2] 
#for car in cars:
    #print(f"Modeli-{car['model'].title()}, "
          #f"rangi-{car['rang']}, "
          #f"yili-{car['yil']} yil, "
          #f"yurgan masofasi-{car['km']}km, "
          #f"korobkasi-{car['korobka']}, "
          #f"narhi-{car['narh']}$")
  #print(cars[1] ['narh'])
  #print(f"{cars[2]['narh']}, "
        #f"{cars[2]['rang']}, "
        #f"{cars[2]['model']}")
#malibus=[]
#for n in range(10):
 #   new_car={'marka':'malibu',
  #           'rang':None,
   #          'yil':2022,
    #         'narh':None,
     #        'km':0,
      #       'korobka':'mehanika'
       #      }
    #malibus.append(new_car)
#for malibu in malibus[:3]:
 #   malibu['rang']='qizil'
#for malibu in malibus[3:7]:
#    malibu['rang']='qora'
 #   malibu['korobka']='avto'
#for malibu in malibus[7:]:
 #   malibu['korobka']='avto'
  #  malibu['rang']='yashil'
#for malibu in malibus:
 #  if malibu['korobka']=='avto':
  #    malibu['narh']=40000
   #else:
    #  malibu['narh']=35000
#for malibu in malibus:
 #   print(malibu)
#Lug'at ichida ro'yhat
#dasturchilar={'kozim':['python', 'sql', 'r'],
 #             'shukur':['js', 'c#'],
  #            'fahriddin':['c++', 'j', 'css'],
   #           'davron':['htl', 'php', 'js']
    #            }
#for ism, tillar in dasturchilar.items():
 #   print(f"\n{ism.title()} quyidagi tillarni biladi:")
  #  for til in tillar:
   #     print(til.upper(), end=' ')
#LUG'AT ICHIDA LUG'AT-
#hamkasblar={
 #           'kozim':{'familiya':'muxtorov',
  #                   'manzil':'fargona',
   #                  'yil':1984,
    #                 'malumoti':'oliy',
     #                'tillar':['hython', 'r', 'sql']
      #               },
       #     'furqat':{'familiya':'toshmatov',
        #              'manzil':'yaypan',
         #             'yil':1988,
          #            'malumoti':'urta',
           #           'tillar':['js', 'html', 'php']
            #          },
            #'fahriddin':{'familiya':'mutalifov',
             #            'manzil':'gorskiy',
              #           'yil':1987,
               #          'malumoti':'oliy',
                #         'tillar':['js', 'python']}
                 #        }
#for ism, malumotlar in hamkasblar.items():
 #   print(f"\n{ism.title()}ning familiyasi-{malumotlar['familiya'].title()},",
  #        f"Manzili-{malumotlar['manzil'].upper()},",
   #       f"tug'ulgan yili-{malumotlar['yil']}yil,",
    #      f"darajasi-{malumotlar['malumoti']},\n",
     #     "Va quyidagi tillarni biladi:")
    #for til in malumotlar['tillar']:
     #   print(til.upper(), end=' ')
#Adabiyot (ilm-fan, san'at, internet) olamidagi 
#4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. 
#Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni 
#konsolga chiqaring.
#elon={'ism':'Elon Mask',
     # 'vatani':'amerika',
      #'faoliyati':'kashfiyotchilik',
      #'t_yili':1971,
      #'asarlari':['tesla', 'spise-x', 'starlink', 'solarcity']
      #}
#bill={'ism':'Bill Geyts',
      #'vatani':'amerika',
      #'faoliyati':'dasturchi',
      #'t_yili':1955,
      #'asarlari':['microsoft', 'exel', 'word']
      #}
#michael={'ism':'Michael Jakson',
     # 'vatani':'amerika',
      #'faoliyati':'rok yulduzi',
    #  't_yili':1958,
    #  'asarlari':['son', 'alone', 'dangerous']
    #  }
#navoiy={'ism':'Alisher Navoiy',
     # 'vatani':'amerika',
      #'faoliyati':'rok yulduzi',
      #'t_yili':1958,
      #'asarlari':['hamsa', 'sabai sayyor', 'munojot']
      #}
#mashxurlar=[elon, bill, michael, navoiy]
#for shahs in mashxurlar:
    #ism=shahs['ism']
    #vatani=shahs['vatani']
    #faoliyati=shahs['faoliyati']
    #tyili=shahs['t_yili']
    #asarlari=shahs['asarlari']
    #print(f"{ism} {vatani.title()}lik, faoliyati-{faoliyati}, {tyili}yili tug'ulgan")
#Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. 
#For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.
#for shahs in mashxurlar:
 #   ism=shahs['ism']
  #  asarlari=shahs['asarlari']
   # print(f"\n{ism}ning mashxur asarlari:")
    #for asar in asarlari:
       #print(asar)
#sino={'ism':'ibn sino',
 #     'vatani':"o'zbekiston",
  #    't_yili':980,
   #   'faoliyati':'tabib',
    #  'asarlari':['tib ilmi', 'ilmi qulub']
     # }
#navoiy={'ism':'alisher navoiy',
 #       'vatani':"o'zbekiston",
  #      't_yili':1441,
   #     'faoliyati':'shoir',
    #    'asarlari':['hamsa', 'sabai sayor', 'munojot']
     #   }
#mask={'ism':'elon mask',
 #     'vatani':'usa',
  #    't_yili':1971,
   #   'faoliyati':'biznesmen',
    #  'asarlari':['spase_x', 'tesla', 'solar city']
     # }
#mashxurlar=[sino, navoiy, mask]
#for odam in mashxurlar:
 #   ism=odam['ism']
  #  vatani=odam['vatani']
   # t_yili=odam['t_yili']
    #faoliyati=odam['faoliyati']
    #print(f"{ism.title()}ning vatani-{vatani.upper()},",
 #         f"tug'ulgan yili-{t_yili}yil, ",
  #        f"faoliyati-{faoliyati}")
#for odam in mashxurlar:
     #   ism=odam['ism']
    #    asarlari=odam['asarlari']
   #     print(f"{ism.title()}ning mashxur asarlari:")
  #      for asar in asarlari:
 #           print(asar.title())
#Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang.
#Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida 
#lug'artga saqlang. Natijani konsolga chiqaring.
#seriallar={'xushnuda':['qashqirlar makoni', 'muxtasham yuz yil', 'ishq ertagi'],
     #      'iroda':['qalbim chechagi', 'ramayana', 'qotillik izidan'],
      #     'kozim':['qashqirlar makoni', 'turmadan qochish', 'game of trones'],
       #    'miraziz':['sonic', 'minecraft', 'yulduzlar jangi']
        #   }
#for ism, serial in seriallar.items():
 #   print(f"\n{ism.title()}ning sevimli seriallari:")
  #  for kino in serial:
   #     print(kino.title())
#Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, 
#foydalanuvchi so'ragan davlat haqida ma'lumot bering. Agar davlat sizning 
#lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan 
#xabarni chiqaring.
davlatlar={
          'amerika':{'tili':'ingliz',
                     'maydoni':9833520,
                     'poytahti':'washington',
                     'aholisi':331893745,
                     'dini':'xristian'},
              'hindiston':{'tili':'hind',
                           'maydoni':3287263,
                           'poytahti':'new delhi',
                           'aholisi':1375586000,
                           'dini':'hinduizm'},
              'turkiya':{'tili':'turk',
                         'maydoni':783356,
                         'poytahti':'anqara',
                         'aholisi':84680273,
                         'dini':'musulmon'},
              'xitoy':{'tili':'xitoy',
                           'maydoni':9596961,
                           'poytahti':'pekin',
                           'aholisi':1410539758,
                           'dini':'buddizm'}
              }
#for davlat, info in davlatlar.items():
 #   print(f"\n{davlat.upper()}ning rasmiy tili {info['tili'].title()} tili,\n",
  #        f"Maydoni-{info['maydoni']}km2,\n",
   #       f"Poytahti-{info['poytahti'].title()},\n",
    #      f"Aholisi soni-{info['aholisi']} kishi,\n",
     #     f"Dini-{info['dini']}")
#davlat=input("Qaysi davlat haqida ma'lumot olishni istaysiz?-").lower()
#if davlat in davlatlar:
 #   info=davlatlar[davlat]
  #  print(f"\n{davlat.capitalize()}ning rasmiy tili-{info['tili']},",
   #       f"\nMaydoni-{info['maydoni']} km2,",
    #      f"\nPoytahti-{info['poytahti'].title()} shaxri,",
     #     f"\nAholisi soni-{info['aholisi']} kishi,",
      #    f"\nDini-{info['dini']}")
#else:
 #       print("Kechirasiz bizda bu davlat haqida ma'lumot mavjud emas!")
#ism=input("Ismingiz nima?-")      
#savol= f"Salom, {ism.title()} yoshingiz nechchida?"
#yosh=input(savol)
#yosh=int(yosh)
#ism=input("Ismingiz nima?")
#savol=f"Salom {ism.title()} mening hotinimni ismi ham {ism.title()}"
#ism2=input(savol)
#ism=input("Ismingiz nima?")
#savol=f"{ism} bo'yingiz necha metr?"
#buy=input(savol)
#buy=float(buy)
#ogirlik=input(f"{buy} og'irligiz qncha?")
son=15
while son <= 88:
    print(son, end=' ')
    son -= 5
print("dastur yakunlandi")