# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 13:56:53 2022

@author: Kozim
"""

#17-DARS. INPUT() VA WHILE()OPERATORLARI
#ism=input("Ismingiz nima? ")
#savol=f"{ism.title()} yoshingiz nechada?"
#ism2=input(savol)
#savol2=f"Yoshingiz {ism2}da bo'lsa hali yosh ekansiz!"
#print(savol2)
#son=1
#while son <=10:
 #   son += 1
  #  print(son,end=' ')
#print("Dastur yakunlandi")
#print("Istalgan sonni kvadratini topish dasturi")
#savol="Istalgan sonni kiriting!-"
#savol += "Dasturni to'htatish uchun 'exit' deb yozing\n"
#qiymat = ''
#while qiymat != 'exit':
#    qiymat = input(savol)
 #   if qiymat != 'exit':
  #      print(float(qiymat)**2)
#print("Dastur yakunlandi")
#son = 0
#while son <=20:
 #   son += 1
  #  print(son, end=' ')
#print("Dastur yakunlandi")
#print("Istalgan sonni kvadratini topish dasturi")
#savol = "Istalgan sonni kiriting! Dasturni to\'htatish uchun 'exit' deb yozing\n"
#qiymat = ' '
#while qiymat != 'exit':
#    qiymat = input(savol)
 #   if qiymat != 'exit':
  #      print(float(qiymat)**2)
#print("Dastur yakunlandi")
#print("Lyuboy sonni kvadratini topish dasturi!")
#son = "Istalgan sonni kiriting! Dastirni to'xtatish uchun 'exit' deb yozing\n:"
#son_2 = ''
#while son_2 != 'exit':
 #   son_2 = input(son)
  #  if son_2 != 'exit':
   #     print(float(son_2)**2)
#print("Tamom")
#print("Istalgan sonni kvadratini hissoblovchi dastur")
#son='Istalgan sonni kiriting' 
#son =+ "Dasturni to'xtatish uchun 'stop' deb yozing\n>"  
#print("Har qanday sonni kvadratini topish dasturi")
#son = "Istalgan sonni kiriting"
#son += 'Dasturni tamomlash uchun "stop" deb yozing\n>'
#qiymat = ''
#while qiymat != 'stop':
#    qiymat = input(son)
 #   if qiymat != 'stop':
  #      print(float(qiymat)**2)
#else:
 #   print("Tamom")
#print("Istalgan sonni kvadratini topish dasturi")
#son = "Istalgan sonni kiriting. "
#son += " Dasturni yakunlash uchun 'jinni' deb yozing\n>" 
#ishora = True
#hile ishora:
 #     qiymat = input(son)
  #    if qiymat == 'jinni':
   #       ishora = False
    #  else: 
     #     print(float(qiymat)**2)
     
#print('tamom')
#print("Hohlagan sonni kvadratini topish dasturi") 
#son = "Istalgan sonni kiriting! "
#son += "Dasturni to'xtatish uchun 'exit' deb yozing\n>"
#while True:
 #   qiymat = input(son)
  #  if qiymat == 'exit':
   #     break
    #else:
     #   print(float(qiymat)**2)
#print("Tamom")
#sonlar = list(range(101))
#for son in sonlar:
 #   if son == 101:
  #      break
   # else:
    #    print(f"{son}ning kvadrati {son**2}ga teng")
#sonlar = list(range(1, 10))
#for son in sonlar:
 #   if son == 5:
  #      continue
   # print(f"{son}ning kvadrati {son**2}ga tenf")
#Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi
# stop so'zini yozishi bilan dasturni to'xtating
#kitoblar = "Yaxshi ko'rgan kitoblaringizni kiriting."
#kitoblar += "Yaxshi ko'rgan kitoblaringizni kiritib bo'lgach 'stop' deb yozing\n>"
#while True:
 #   kitob = input(kitoblar)
  #  if kitob == 'stop':
   #     break
#print("Rahmat")
#Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 
#7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. 
#Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin 
#va chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda 
#dastur to'xtasin (ikkita shartni ham tekshiring).
#savol = "Yoshingizni kiriting: "
#while True:
 #   qiymat = input(savol)
  #  if qiymat == 'exit' or qiymat == 'quit':
   #     break
   # yosh = int(qiymat)
    #if yosh <=7:
     #   narh = 2000
   # elif 7 <= yosh < 18:
    #    narh = 3000
    #elif 18<= yosh < 65:
     #   narh = 10000
   # else: narh = 0
   # if narh == 0:
    #    print("Sizga chipta bepul")
    #else:
     #   print(f"Chipta {narh} so'm")
#savol = "Yoshingizni kiriting: "
##   qiymat = input(savol)
  #  if qiymat == 'exit' or qiymat == 'quit':
   #     break
    #yosh = int(qiymat)
    
#    if yosh < 7:
 #       narh = 0
  #  elif 7 <= yosh <18:
   #     narh = 3000
    #elif 18 <= yosh < 65:
     #   narh = 10000
    #else: narh = 0
    #if narh == 0:
    #    print("Sizga kirish bepul")
    #else:
     #   print(f"Sizga kirish {narh} so'm")
#savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
#savol += "Musbat son kiriting "
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

#while True:
 #   qiymat = input(savol)
  #  qiymat =float(qiymat)
   # if qiymat<0:
    #    continue
    #elif (qiymat)=='Exit':
     #   break
    #else:
     #   ildiz = float(qiymat**0.5)
      #  print(f"{qiymat} ning ildizi {ildiz} ga teng")


#savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
#savol += "Musbat son kiriting "
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

#while True:
 #   qiymat = input(savol)
  #  if qiymat=='exit':
   #     break
    #elif float(qiymat)<0:
     #   continue # agar foydalanuvchi manfiy son kiritsa tsiklni takrorlaymiz
    #else:
     #   ildiz = float(qiymat)**(0.5)
      #  print(f"{qiymat} ning ildizi {ildiz} ga teng")
