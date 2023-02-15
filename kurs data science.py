# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 16:10:52 2022

@author: User
"""

#ON-LINE KURS
#app_costs=1.99
#app_costs += 6.99
#print(app_costs)
#x=100
#x+=2
#print(x)
#x-=2
#print(x)
#x*=2
#print(x)
#x/=2
#print(x)
#x**=2
#print(x)
#x**=4
#print(x)

#INTEGERS AND FLOATS
#print(6.99*1)
#print(0+1.99)
#print(type(0))
#print(type(0.0))
#print(6.99+0)
#print(1.99*2)
#print(int(6.99))
#print(float(10))
#print(int(6.99))
#print(float(900.0))
#print(round(6.99))
#print(round(1.99))
#print(round(0.0))
#minecraft_cost=6.99
#print(round(minecraft_cost))
#print(minecraft_cost)
#minecraft_cost=round(minecraft_cost)
#print(minecraft_cost)
#print('a'+'b')
#print('a' + ' ' + 'b')
#print('men'+'seni'+'sevaman')
#print('men' + ' '+ 'seni' + ' ' + 'sevaman')
#print('r'*1)
#print('b'*5)
#print('olma' " "*9)
#print('kozim '  *4)
#facebook="Facebook's rating is"
#fb_rating_str='3.5'
#fb=facebook+ ' ' + fb_rating_str
#print(fb)
#print(int('4')+1)
#print(float('6.6')+8)
#a=2
#b=5
#print(a+b)
#print(str(a)+str(b))
#line_1=''' Men futbolni sevaman,
 #       chunki u juda qiziqarli o'yin.
  #      Uni har kuni ko'rgim keladi'''
#line_2='''_________________
#qator1
#qator2
#qator3'''
#print(line_1)
#print(line_2)
#row_1=['Facefook', 'USD', 0.0, 463211, 3.5]
#print(len(row_1))
#list1=[1, 6, 0, 7]
#print(len(list1))
#list2=[]
#print(len(list2))
#row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
#app_name = row_1[0]
#n_of_ratings = row_1[3]
#rating = row_1[-1]
#fb_rating_data = [row_1[0], row_1[3], row_1[-1]]
#print(fb_rating_data)

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.9, 'USD', 698516, 4.5]
row_5 = ['Micecraft: Pocked Edition', 6.99, "USD", 522012, 4.5]
#fb_rating_data = [row_1[0], row_1[3], row_1[-1]]
#insta_rating_data = [row_2[0], row_2[3], row_2[-1]]
#minecraft_rating_data = [row_5[0], row_5[3], row_5[-1]]
#total_rating = fb_rating_data[2] + insta_rating_data[2] + minecraft_rating_data[2]
#average_rating = total_rating/3
#print(average_rating)

#List Slicing. Ro'yhatni kesish. Bunda ro'yhatdagi kerakli ma'lumotlarni 
#alohida yozib o'tirmasdan kesib olish mumkin.

#row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
#cc_pricing_data = [row_3[0], row_3[1], row_3[2]] #uzun kod
#print(cc_pricing_data)

#cc_pricing_data = row_3[0:3] #qisqa kod
#print(cc_pricing_data)
#first_3 = row_3[:3]
#last_3 = row_3[-3:]
#print(first_3)
#print(last_3)
fb_last_3 = row_1[-3:]
minecraft_4_5 = row_5[2:4]
#print(fb_last_3)
#print(minecraft_4_5)
data_set = [row_1, row_2, row_3, row_4, row_5]
#print(data_set[0])
#print(data_set[-1])
#print(data_set[:2])
#insta_row = data_set[1]
#insta_rating = insta_row[-1]
#print(insta_row)
#print(insta_rating)
#print(data_set[0][-1])
avr_ratnig = (data_set[0][-1] + data_set[1][-1] + data_set[2][-1] + data_set[3][-1] + data_set[4][-1])/5
print(avr_ratnig)
