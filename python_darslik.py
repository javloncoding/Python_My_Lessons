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

























