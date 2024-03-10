
# try:
#     a = int(input())
#     b = int(input())
#     result = a/b
#     # print(result)
# # except ZeroDivisionError:
# #     print('Error')
# # # except ValueError:
# # #     print('Error2')
# # else:
# #     print(result)
# except Exception:
#     print('Error3')
# else:
#     print(result)
#
# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# l2 = []
# for i in l1:
#     l2.append(i**2)
# print(l2)
# l3 = [i**2 for i in l1]
# print(l3)
# l4 = [3**y for y in range(1, 6)]
# print(l4)
# l5 = [x for x in l1 if x % 2 == 1]
# print(l5)
# l6 = [(x, y) for x in l1 for y in l2]
# print(l6)
#
# l7 = []
# for x in l1:
#     for y in l2:
#         l7.append((x, y))
# print(l7)

#
# s1 = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6}
# s2 = {}
# print(s1)
# for key, value in s1.items():
#     s2[value] = key
# print(s2)
# s3 = {v: k for k, v in s1.items()}
# print(s3)
#
# from math import *
#
# def rownanie_kwadratowe(a, b, c):
#     delta = b**2-4*a*c
#     if delta < 0:
#         print('brak pierwiastkow')
#         return 0
#     elif delta == 0:
#         print('Jeden pierwiastek')
#         x = (-b) / (2 * a)
#         return x
#     elif delta > 0:
#         print('Dwa pierwiastki')
#         x1 = (-b + sqrt(delta)) / (2 * a)
#         x2 = (-b - sqrt(delta)) / (2 * a)
#         return x1, x2
# print(rownanie_kwadratowe(6, 3, 1))
# print(rownanie_kwadratowe(1, 2, 1))
# print(rownanie_kwadratowe(2, 6, 1))
#
# def dlugosc_odcinka(x1=1, x2=2, y1=3 ,y2=4):
#     return sqrt(((x1-x2)**2) + (y1-y2)**2)
# print(dlugosc_odcinka())
# print(dlugosc_odcinka(3, 5, 1, 6))
# # print(dlugosc_odcinka(y1=5, x1=3, y2=6, x2=8))
# # print(dlugosc_odcinka(1, 5, y2=8, y1=3))
# #
#
# plik = open('tekst (1).txt', 'r', encoding='utf-8') # C:\\Users\\local\\Downloads
# znak  = plik.read(10)
# linia = plik.readline()
# linie = plik.readlines()
# plik.close()
# print(znak)
# print(linia)
# print(linie)
#
# plik = open('tekst (1).txt', 'a+')
# plik.write('aaaaa')
# plik.seek(105)
# znaki = plik.read(10)
# plik.close()
# print(znaki)
#
# with open('tekst (1).txt', 'r') as plik:
#     znaki = plik.read(10)
#
# print(znaki)