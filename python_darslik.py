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


# son = int(input("juft son kiriting: "))
# if son % 2:
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


# ishora: True False

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


# Break

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


# CONTINUE OPERATORI

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


# ABADIY TSIKL TUZOG'I

# infinite loop

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

# Amaliyot

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


# WHILE YORDAMIDA RO'YXATNI TO'LDIRISH

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

# RO'YXAT ELEMENTLARINI O'CHIRISH

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

""" FUNKSIYALAR """

# def ism_yosh(ism, yosh, yil=2023):
#     print(f"Salom, {ism.title()}. Siz {yil - yosh} yilda tug'ilgansiz.  ")
#
# ism_1 = input("Ismingizni kiriting: ")
# yosh_1 = int(input("Yoshingizni kiriting: "))
# ism_yosh(ism_1, yosh_1)

# def son_1(son):
#     kv = son**2
#     kub = son**3
#     print(f"sonning kvadrati {kv} ga teng, kubi esa {kub} ga teng.")
#
# raqam = int(input(f"Raqam kiriting: "))
# son_1(raqam)

# def juft_toq(son):
#     if son%2:
#         print(f"Kiritilgan son toq, {son}")
#     else:
#         print(f"Kiritilgan son juft, {son}")
# s = int(input(f"Son kiriting: "))
# juft_toq(s)

# def tekshiruv(son):
#     for n in range(2,11):
#         if not son%n:
#             print(f"{son} {n} ga qoldiqisiz bo'linadi.")
# s = int(input(f"son kiriting: "))
# tekshiruv(s)

""" RANGE yoyilmasi """


# def oraliq(min,max,qadam=None):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min +=n
#     return sonlar
# mi = int(input(f"minimum sonni kiritng: "))
# ma = int(input(f"maximum sonni kiritng: "))
# n = int(input(f"qadamni kiritng: "))
# print(oraliq(mi,ma,n))

# def mijoz_info(ism, familiya, tyil, tjoy, tel=None):
#     """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     mijoz = {'ism':ism,
#              'familiya':familiya,
#              'tyil':tyil,
#              'yoshi':2023-tyil,
#              'tjoy':tjoy,
#              'telefon':tel}
#     return mijoz
# print("Mijoz haqida ma'lumotlarni kiriting.")
# mijozlar =[]
# while True:
#     ism = input("Ismi: ")
#     familiya = input("Familiyasi: ")
#     tyil = int(input("Tug'ilgan yili: "))
#     tjoy = input("Tug'ilgan joyi: ")
#     telefon = input("Telefon raqami: ")
#     mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, telefon))
#     javob = input("Davom etasizmi? (ha/yo'q)")
#     if javob!='ha':
#         break
# print("Mijozlar:")
# for mijoz in mijozlar:
#     print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()},"
#           f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['telefon']}")
#
# def fibonacci(n):
#     sonlar = []
#     for x in range(n):
#         if x==0 or x==1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[x-1]+sonlar[x-2])
#     return sonlar
#
# print(fibonacci(10))

# def tub_sonlar_top(min, max):
#     tub_sonlar = []
#     for n in range(min, max + 1):
#         tub = True
#         if (n == 1):
#             tub = False
#         elif (n == 2):
#             tub = True
#         else:
#             for x in range(2, n):
#                 if (n % x == 0):
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
#     return tub_sonlar
# tub_sonlar_top(1, 20)


# def katta_harf(matnlar):
#     for i in range(len(matnlar)):
#         matnlar[i]=matnlar[i].title()
#
# ismlar = ['ali', 'vali', 'hasan', 'husan']
# katta_harf(ismlar)
# print(ismlar)
#
# def katta_harf(matnlar):
#     matnlar = matnlar[:]
#     for i in range(len(matnlar)):
#         matnlar[i]=matnlar[i].title()
#     return matnlar
#
# ismlar = ['ali', 'vali', 'hasan', 'husan']
# yangi_ismlar = katta_harf(ismlar)
# print(ismlar)
# print(yangi_ismlar)

# talabalar = ['ali', 'vali', 'hasan', 'husan']
#

# def bahola(ismlar):
#     baholar = {}
#     for ism in ismlar:
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism] = baho
#     return baholar
#
#
# baholar = bahola(talabalar)
# print(baholar)
# print(talabalar)

# s = [2 ,3, 3,4,5,6,5]
# def sd(*d):
#     n = 0
#     for m in s:
#         n += m
#     return n
# d = sd(s)
# print(d)

# def my_func(*son):
#     kopaytma = 1
#     for kopayuvchi in sonlar:
#         kopaytma *= kopayuvchi
#     return kopaytma
# sonlar = [2,5]
# natija = my_func(sonlar)
# print(natija)

# def talaba_info(ism, familiya, **kwargs):
#     kwargs['ism']=ism
#     kwargs['familiya']=familiya
#     return kwargs
#
# talaba = talaba_info('olim','olimov',tyil=1995,fakultet='IT',yonalish='AT')
# print(talaba)

"""MODULLAR"""

# import math
#
# x=400
# print(math.sqrt(x))
# print(pow(5,5))
#
# from math import pi
# print(pi)
# print(math.log2(8))
# print(math.log10(100))
#
# import random as r # random modulini r deb chaqirayapmiz
#
# son = r.randint(0,100) # 0 va 100 oralig'ida tasodifiy son
# print(son)
#
# ismlar = ['olim','anvar','hasan','husan']
# ism = r.choice(ismlar) # ismlar dan tasodifiy ism tanlaymiz
# print(ism)
# print(r.choice(ism)) # ismdan tasodifiy harf tanlaymiz
#
# x = list(range(0,51,5))
# print(x)
# print(r.choice(x))
#
# x = list(range(11))
# print(x)
# r.shuffle(x)
# print(x)

"""LAMBDA"""
# lambda argument:ifoda

# import math
# uzunlik = lambda pi, r : 2*pi*r
# print(uzunlik(math.pi,10))
#
# product = lambda x, y : x ** y
# print(product(3, 2))
#
# def daraja(n):
#     return lambda x : x**n
#
# kvadrat = daraja(2)
# kub = daraja(3)
# print(f"3-ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng")
#
# from math import sqrt
#
# sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati
# ildizlar = list(map(sqrt,sonlar))
# sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati
#
# def daraja2(x):
#     """Berilgan sonning kvadratini qaytaruvchi funksiya"""
#     return x*x
#
# print(list(map(daraja2,sonlar))) # sonlar ning kvadratini hisoblaymiz
#
# kvadratlar = list(map(lambda x:x*x,sonlar))
# print(kvadratlar)
#
# kvadratlar = []
# for son in sonlar:
#     kvadratlar.append(son*son)
#
# a = [4, 5, 6]
# b = [7, 8, 9]
# a_plus_b = list(map(lambda x, y: x + y, a, b))
# print(a_plus_b)
#
# ismlar = ['hasan','husan','olim','umid']
# print(list(map(lambda matn:matn.upper(),ismlar)))
#
# import random as r
#
# sonlar = r.sample(range(100),10) # 0-99 oralig'ida 10 ta tasodifiy sonlar
#
# def juftmi(x):
#     """x juft bo'lsa True, aks holda False qaytaruvchu funksiya"""
#     return x%2==0
#
# juft_sonlar = list(filter(juftmi,sonlar))
# print(sonlar)
# print(juft_sonlar)
#
# import random as r
#
# sonlar = r.sample(range(100),10) # 0-99 oralig'ida 10 ta tasodifiy sonlar
# juft_sonlar = list(filter(lambda son: son%2==0,sonlar))
#
# print(sonlar)
# print(juft_sonlar)
#
# mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]
#
# mevalar_b = list(filter(lambda meva:meva.startswith('b'),mevalar))
# print(mevalar_b)
#
# mevalar2 = list(filter(lambda meva:len(meva)<=5, mevalar))
# print(mevalar2)
#
# list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar))



# """ SON TOPISH O'YINI """
#
# import random as r
#
# print("Salom son topish o'yinini o'ynimiz. ")
# def sontop(x=10):
#     print("Men 1 dan 10 gacha son o'yladim topib ko'ringchi!")
#     taxmin_son = r.randint(1, x)
#     taxminlar = 0
#     while True:
#         taxminlar += 1
#         savol = int(input(">>> "))
#         if savol < taxmin_son:
#             print("Men o'ylagan son bundan kattaroq.")
#         elif savol > taxmin_son:
#             print("Men o'ylagan son bundan kichikroq.")
#         else:
#             break
#     print(f"Siz {taxminlar} ta taxmin bilan topdingiz :)\n")
#     return taxminlar
# def sontop_pc(x=10):
#     input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.\n>>>")
#     quyi = 1
#     yuqori = x
#     taxminlar = 0
#     while True:
#         taxminlar += 1
#         if quyi != yuqori:
#             taxmin = r.randint(quyi, yuqori)
#         else:
#             taxmin = quyi
#         javob = input(
#             f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
#             f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower()
#         )
#         if javob == "-":
#             yuqori = taxmin - 1
#         elif javob == "+":
#             quyi = taxmin + 1
#         else:
#             break
#     print(f"Men {taxminlar} ta taxmin bilan topdim!")
#     return taxminlar
# def play(x=10):
#     yana = True
#     while yana:
#         taxminlar_pc = sontop_pc(x)
#         taxminlar_user = sontop(x)
#
#         if taxminlar_user > taxminlar_pc:
#             print(f"Men {taxminlar_pc} taxmin bilan topdim va  yutdim!")
#         elif taxminlar_user < taxminlar_pc:
#             print(f"Siz {taxminlar_user} taxmin bilan topdingiz va yutdingiz!")
#         else:
#             print("Durrang!")
#         yana = int(input("Yana o'ynaymizmi? Ha(1)/Yo'q(0):"))
# play()





