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




























