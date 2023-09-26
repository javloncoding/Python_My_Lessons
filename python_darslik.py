# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 23:49:30 2023

@author: User
"""

# davlatlar = ['uzb', 'rus', 'turkiya', 'germaniya']
# print(len(davlatlar))
# print(sorted(davlatlar, reverse=True))

# j_sonlar = list(range(120, 1200, 2))
# print(j_sonlar)
# print(sum(j_sonlar))
# print(max(j_sonlar) - min(j_sonlar))

# ismlar = ['java', 'otaw', 'ismoy', 'shelby', 'utkir']
# for i in ismlar:
#     print(f"qalisan {i}")
# print(f"kod {len(ismlar)} marta takrorlandi")

# t_sonlar = list(range(11, 100, 2))
# for i in t_sonlar:
#     print(f"{i} ning kubi {i**3} ga teng")

# avtolar = ['nexia', 'malibu', 'bmw', 'gentra']
# for i in avtolar:
#     if i == 'bmw':
#         print(i.upper())
#     else:
#         print(i.title())


# ism = input("login kiriting: ")
# if  ism == 'admin':
#     print(f"Xush kelibsiz, {ism}. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz, {ism}!")

# son = int(input("istalgan son kiriting: "))
# if son > 0:
#     print("musbat son")
# elif son < 0:
#     print("manfiy son")
# else:
#     print("nomanfiy nomusbat son 0")


# ildizli_son = int(input("son kiriting: "))
# if ildizli_son > 0:
#     print(ildizli_son**(1/2))
# else:
#     print("musbat son kiriting")



# j_son = int(input("juft son kiriting: "))
# if j_son % 2:
#     print("juft son kiriting")
# else:
#     print("raxmat")


# yosh = int(input("yoshingizni kiriting: "))
# if yosh <= 4 or yosh >=60:
#     print("sizga kirish tekin")
# elif yosh < 18:
#     print("sizga kirish 10000 so'm")
# elif yosh >=18:
#     print("sizga kirish 20000 so'm")



# mahsulot = ['ananas' , 'anor', 'banan', 'uzum', 'nok', 'olma', 'gilos', 'anjir', 'shaftoli', 'behi']
# savat = []
# for n in range(5):
#     savat.append(input(f"{n+1} - mevani kiriting: "))
# if savat:
#     for mahsulotlar in savat:
#         if mahsulotlar in mahsulot:
#             print(f"{mahsulotlar} mahsulotimiz bor")
#         else:
#             print(f"{mahsulotlar} mahsulotimiz yo'q")
# else:
#     print("meva kiritilmadi")


# mahsulot = ['ananas' , 'anor', 'banan', 'uzum', 'nok', 'olma', 'gilos', 'anjir', 'shaftoli', 'behi']
# savat = []
# bor_mahsulotlar = []
# yoq_mahu=sulotlar = []
# for n in range(5):
#     savat.append(input(f"{n+1} - mevani kiriting: "))
# for mahsulotlar in savat:
#     if mahsulotlar in mahsulot:
#         bor_mahsulotlar.append(mahsulotlar)
#     else:
#         yoq_mahu=sulotlar.append(mahsulotlar)
# if bor_mahsulotlar:
#     print(f"Do'konimizda quyidagi mahsulotlar bor:")
#     for bor in bor_mahsulotlar:
#         print(bor)
# else:
#     print(f"Do'konimizda quyidagi mahsulotlar bor:")
        


# login = ['java', 'admin', 'ake', 'mrx']
# new_login = input("login kiriting: ")
# if new_login in login:
#     print("login band")
# else:
#     print("xush kelibsiz")


# son = int(input("son kiriting: "))
# for i in range(2, 11):
#     if not(son % i):
#         print(f"ushbu {i} soniga qoldiqsiz bo'linadi")


# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else: 
#     print("Savatingiz bo'sh")            


# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# savat = []
# for n in range(5):
#     savat.append(input(f'Savatga {n+1}-mahsulotni qo\'shing: '))
# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# if mavjud_emas:
#   print("Do'konimizda quyidagi mahsulotlar yo'q:")
#   for mahsulot in mavjud_emas:
#       print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
    

# users = ['alisher1983','aziza','yasina', 'umar']
# login = input("Yangi login tanlang:" )
# if login in users:
#     print('Login band, yangi login tanalng!')
# else:
#     print("Xush kelibsiz!")

"""Dictionary (Lug'at)"""

# en_uz = {
#     'apple' : 'olma',
#     'morning' : 'tong',
#     'monday' : 'dushanba',
#     'hello' : 'salom'
#     }
# kalit = input("So'z kiriting: ")
# natija = en_uz.get(kalit)
# if natija == None:
#     print("Bunday so'z mavjud emas")
# else:
#     print(f"{kalit} tarjimasi {natija}" )    


### items() method ###

# men_haqimda = {
#     'ism' : 'javlon',
#     'familiya' : 'abdullayev',
#     'yosh' : 20,
#     't_yil' : 2003,
#     'manzil' : 'toshkent'
#     }
# print(men_haqimda.items())
# for kalit, qiymat in men_haqimda.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat}")
        
# malumot = {
#     'java' : 'redmi 9A',
#     'otaw' : 'redmi S12',
#     'ismoy' : 'nokia',
#     'shelby' : 'poco'
#     }
# for k, q in malumot.items():
#     print(f"{k.title()}ning telefoni {q.title()}")
    

### .keys() method ###

# mahsulotlar = {
#     'olma' : 10000,
#     'o\'rik' : 12000,
#     'uzum' : 9000,
#     'anor' : 14000,
#     'shaftoli' : 15000
#     }
# print(mahsulotlar.keys()

# for mahsulot in mahsulotlar.keys():
#     print(f"{mahsulot.title()}")
# print("Do'konimizda ushbu mahsulotlarimiz bor! ")

# mahsulotlar = {
#     'olma' : 10000,
#     'o\'rik' : 12000,
#     'uzum' : 9000,
#     'anor' : 14000,
#     'shaftoli' : 15000
#     }
# bozorlik = ['uzum', 'olma', 'non', 'pomidor']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()}ning narhi {mahsulotlar[mahsulot]} so'm")
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"{buyum} ham olib keling")


### Lug'at elementlarini tartib bian chaqirish ###

# mahsulotlar = {
#     'olma' : 10000,
#     'o\'rik' : 12000,
#     'uzum' : 9000,
#     'anor' : 14000,
#     'shaftoli' : 15000
#     }
# print("Do'konimizdagi mahsulotlar:")
# for mahsulot in sorted(mahsulotlar):
#     print(f"{mahsulot.title()}")
# print(mahsulotlar.keys())


### .values() method ###

# malumot = {
#     'java' : 'redmi 9A',
#     'otaw' : 'redmi S12',
#     'ismoy' : 'nokia',
#     'shelby' : 'poco',
#     'utkir' : 'redmi S12',
#     'isya' : 'poco'
#     }
# # print(malumot.values())
# # for tel in sorted(malumot.values()):
# #     print(f"{tel.title()}")

# for tel in set(malumot.values()):
#     print(f"{tel.title()}")

# en_uz = {
#     'apple' : 'olma',
#     'banana' : 'banan',
#     'home' : 'uy',
#     'hello' : 'salom',
#     'bye' : 'hayr',
#     'work' : 'ish',
#     'family' : 'oila',
#     'sister' : 'opa'
#     }
# for k, q in sorted(en_uz.items()):
#     print(f"Kalit: {k.title()}")
#     print(f"Qiymat: {q.title()}")


# davlatlar = {
#     'o\'zbekiston' : 'toshkent',
#     'amerika' : 'new-york',
#     'turkiya' : 'istanbul',
#     'russia' : 'moskva'
#     }
# davlat = input("Davlatni kiriting: ").lower()
# if davlat in davlatlar.keys():
#     print(f"{davlat.title()}ning poytaxti {davlatlar[davlat].title()}.")
# else:
#     print(f"Bizda {davlat.title()} davlatining poytaxti mavjud emas!")


# restoran = {
#     'osh' : 20000,
#     'manti' : 18000,
#     'lag\'mon' : 16000,
#     'sho\'rva' : 19000,
#     'chuchvara' : 20000,
#     'kaklet' : 10000,
#     'dimlama' : 18000
#     }
# buyurtma = []
# print("3 ta taom kiriting!")
# for i in range(3):
#     buyurtma.append(input(f"{i+1} - taomni kiriting: ").lower())
# for taom in restoran.keys():
#     if taom in buyurtma:
#         print(f"{taom.title()} taomning narhi {restoran[taom]} so'm.")
# for taom1 in buyurtma:
#     if taom1 not in restoran:
#         print(f"{taom1.title()} taom bizning restoranda mavjud emas!")



### Sets (malumotlar turi) ###

# toys = {"ball", "car", "mishka", "ball", "lamp", "raketa"}
# print(toys)
# print(toys)
# print(toys)


### NESTING ###

### LIST ni ichiga LUG'ATLAR ni joylash

# car0 = {
#         'model' : 'gentra',
#         'yil' : 2019,
#         'narh' : 23000,
#         'karobka' : 'avtomat'
#         }
# car1 = {
#         'model' : 'lasetti',
#         'yil' : 2022,
#         'narh' : 33000,
#         'karobka' : 'avtomat'
#         }
# car2 = {
#         'model' : 'kaptiva',
#         'yil' : 2020,
#         'narh' : 40000,
#         'karobka' : 'mexanika'
#         }
# cars = [car0,car1,car2]
# for car in cars:
#     print(f"{car['model'].title()}, "
#           f"{car['yil']}-yil, "
#           f"{car['narh']}$")
# print(cars[0]['model'])

# malibus = []
# for i in range(10):
#     new_car = {
#         'model': 'malibu',
#         'yil': 2023,
#         'narh': None,
#         'km': 0,
#         'rang': None,
#         'karobka': 'avtomat'
#         }
#     malibus.append(new_car)
# for malibu in malibus[:3]:
#     malibu['rang'] = ['qora']
# for malibu in malibus[3:7]:
#     malibu['rang'] = ['oq']
#     malibu['karobka'] = ['mexanika']
# for malibu in malibus[7:]:
#     malibu['rang'] = ['qizil']
    
# for malibu in malibus:
#     if malibu['karobka']=='avtomat':
#         malibu['narh']=55000
#     else:
#         malibu['narh']=50000
# for malibu in malibus:    
#     print(malibu)


### LUG'ATNI ichiga LIST joylash 

# dasturchilar = {
#     'javlon':['python', 'django', 'sql', 'c++'],
#     'otaw' : ['assembly', 'js', 'html', 'css', 'bootstrap'],
#     'ismoy' : ['python', 'pandas', 'matplotlib'],
#     'abdukarim' : ['python', 'matplotlib', 'pandas', 'numpy', 'algoritm']
#     }
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} ushbu dasturlash tillarni biladi.")
#     for til in tillar:
#         print(f"{til.upper()}")

### LUG'AT ni ichiga LUG'AT ni joylash

# hamkasblar = {
#     'ali':{'familiya':'valiyev',
#            'tyil':1995,
#            'malumot':'oliy',
#            'tillar':['python','c++']
#            },
#     'vali':{'familiya':'aliyev',
#             'tyil':2001,
#             'malumot':"o'rta-maxsus",
#             'tillar':['html', 'css', 'js']},
#     'hasan':{'familiya':'husanov',
#              'tyil':1999,
#              'malumot':'maxsus',
#              'tillar':['python','php']}
#     }

# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()}, "
#           f"{info['tyil']}-yilda tug'ilgan. "
#           f"Ma'lumoti: {info['malumot']}. \n"
#           "Quyidagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print(til.upper())


""" INPUT() va WHILE() """

# ism = input("Ismingizni kiriting: ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
# yosh = input(savol)
# yosh = int(yosh)
# height = input("Bo'yingiz necha metr? ")
# height = float(height)

# son = 1
# while son<=5:
#     print(son, end=' ')
#     son +=1
# print("Dastur tugadi!")

# print("Kiritilgan sonning kvadratini hisoblo'vchi dastur!")
# savol = ("Istalgan son kiriting ")
# savol += ("(dasturni to'xtatish uchun 'stop' deb yozing) : ")
# qiymat = ''
# while qiymat != 'stop':
#     qiymat = input(savol)
#     if qiymat != 'stop':
#         print(float(qiymat)**2)
# print("Dastur tugadi!")


### ishora: True False

# print("Kiritilgan sonning kvadratini hisoblo'vchi dastur!")
# savol = ("Istalgan son kiriting ")
# savol += ("(dasturni to'xtatish uchun 'stop' deb yozing) : ")
# qiymat = ''
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'stop':
#         ishora = False
#     else:
#         print(float(qiymat)**2)
# print("Dastur tugadi!")


### Break

# print("Kiritilgan sonning kvadratini hisoblo'vchi dastur!")
# savol = ("Istalgan son kiriting ")
# savol += ("(dasturni to'xtatish uchun 'stop' deb yozing) : ")
# while True:
#     qiymat = input(savol)
#     if qiymat == 'stop':
#         break
#     else:
#         print(float(qiymat)**2)
# print("Dastur tugadi!")

# sonlar = list(range(1,11))
# for son in sonlar: 
#     if son == 5: # son 5 ga teng bo'lsa kod to'xtaydi
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")


### CONTINUE OPERATORI

# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5: # son 5 ga teng bo'lsa tiskl boshiga qaytadi
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng")

# son = 0
# while son<10:
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)


### ABADIY TSIKL TUZOG'I

## infinite loop
# son = 0
# while son<10:
#     if son%2!=0:
#         continue
#     else:
#         print(son)

# son = 1
# while son>0: 
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)

### Amaliyot

# savol = "yaxshi ko'rgan kitobingizni kiriting "
# savol += "(dasturni to'xtatish uchun 'stop' ni kiriting): "
# kitob = ''
# while kitob != 'stop':
#     kitob = input(savol)
#     if kitob != 'stop':
#         print(float(kitob)**2)
# print("Dastur tugadi!")

# print("Muzeyga xush kelibsiz!")
# savol =  "Yoshingizni kiriting (to'xtatish uchun 'stop') : "
# yosh = ''
# while yosh != 'stop':
#     yosh = input(savol)
#     if yosh != 'stop':
#         yosh = int(yosh)
#         if yosh <= 7:
#             print("Sizga kirish 2000 so'm")
#         elif 7 < yosh <= 18:
#             print("Sizga kirish 3000 so'm")
#         elif 18 < yosh <= 65:
#             print("Sizga kirish 10000 so'm")
#         else:
#             print("Sizga kirish bepul")
#     elif yosh == 'stop':
#         break
# print("Tashrifingiz uchun raxmat! ")

# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# while True:
#     qiymat = input(savol)
#     if qiymat=='exit':
#         break
#     elif float(qiymat)<0:
#         continue # agar foydalanuvchi manfiy son kiritsa tsiklni takrorlaymiz
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")
    

## WHILE YORDAMIDA RO'YXATNI TO'LDIRISH

# print("Do'stlani ro'yxati.")
# ismlar = []
# n = 1
# while True:
#     savol = f"{n}-do'stingizni ismi: "
#     ism = input(savol)
#     ismlar.append(ism)
#     savol2 = input("Yana ism kiritasizmi ('ha' yoki 'yo'q')")
#     if savol2 == 'ha':
#         n+=1
#         continue
#     else:
#         break
# print("Do'stlaringizni ro'yxati.")
# for ism in ismlar:
#     print(ism.title())
    

## WHILE YORDAMIDA LUG'ATNI TO'LDIRISH

# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh) # ism kalit, yosh qiymat
#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#     if javob == "yo'q":
#         ishora = False
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")      

## RO'YXAT ELEMENTLARINI O'CHIRISH

# cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
# while 'nexia' in cars: # toki nexia cars ro'yxati ichida ekan...
#     cars.remove('nexia') # nexia ni ro'yxatdan olib tashla
# print(cars)

## RO'YXATDAN RO'YXATGA ELEMENT KO'CHIRISH

# talabalar = ['hasan', 'husan', 'olim', 'botir']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = baho


### AMALIYOT ###

# print("Buyurtma qabul qiluvchi dasturimizga xush kelibsiz!")
# buyurtmalar = []
# while True:
#     buyurtma = input("Buyurtmani kiriting: ")
#     buyurtmalar.append(buyurtma)
#     savol = input("\nYana buyurtma berasizmi? (ha/yo'q) ")
#     if savol == 'ha':
#         continue
#     else:
#         break
# savol1 = "\nBuyurtmalar qabul qilindi!\nKo'rishni hohlaysizmi? (ha/yo'q) "
# javob = input(savol1)
# if javob == 'ha':
#     print("\nBuyurtmalar ro'yxati.")
#     for buyurtma in buyurtmalar:
#         print(f"{buyurtma.title()}")
# else:
#     print("\nRaxmat sog' bo'ling! ")


# print("e-Bozor mahsulotlar do'koniga xush kelibsiz!")
# bozor = {}
# ishora = True
# while ishora:
#     mahsulot = input("\nMahsulot nomini kiriting: ")
#     narh = int(input(f"{mahsulot.title()}ning narhini kiriting: "))
#     bozor[mahsulot] = narh
#     savol = input(f"\nYana e-Bozor dasturidan foydalanasizmi? (ha/yo'q) ")
#     if savol == 'ha':
#         continue
#     else:
#         ishora = False
# javob = input(f"\nMahsulotlar va narhlari qabul qilindi!\nKo'rishni hohlaysizmi? (ha/yo'q)")
# if javob == 'ha':
#     for m, n in bozor.items():
#         print(f"{m.title()}ning narhi {n} so'm")
# else:
#     print("e-Bozor dasturimizdan foydalanganingiz uchun raxmat :)\nDatur to'xtatildi!")


# bozor = {'uzum': 20000, 'olma': 13000, 'pamidor': 19000, 'anor': 23000}
# buyurtmalar = ['olma', 'uzum', 'anor']
# for buyurtma in bozor.keys():
#     if buyurtma in buyurtmalar:
#         print(f"{buyurtma.title()}ning narhi {bozor[buyurtma]}")
#     else:
#         print(f"{buyurtma.title()} mahsulotining narhi ko'rsatilmagan.")
    
# buyurtmalar = ['olma','anjir','uzum','qovun']
# mahsulotlar = {'olma':20000,
#                'shaftoli':25000,
#                'tarvuz':18000,
#                'uzum':22000}

# while buyurtmalar:
#     buyurtma = buyurtmalar.pop()
#     if buyurtma in mahsulotlar.keys():
#         narh = mahsulotlar[buyurtma]
#         print(f"{buyurtma.title()} - {narh} so'm")
#     else:
#         print(f"Bizda {buyurtma} yo'q")


