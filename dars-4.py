# 1-masala
# k = int(input('K sonini kiriting: '))
# n = int(input('N sonini kiriting: '))
# for i in range(n):
#     print(k)



# 2-masala
# s = 0
# for i in range(2, 30):
#     if i % 2 == 1:
#         s += i
# print(s)



# 3-masala
# a = int(input("a ni kiriting: "))
# b = int(input("b ni kiriting: "))
#
# count = 0
# for i in range(a + 1, b):
#     print(i, end=" ")
#     count += 1
#
# print(f"\nChiqarilgan sonlar soni: {count}")



# 4-masala
# konfet = float(input("1 kg konfetning narxini kiriting: "))
# for i in range(1, 11):
#     print(f"{i} kg konfetning narxi: {konfet * i} so'm")



# 5-masala
# konfet_narxi = float(input("Konfetning 1 kilogramm narxini kiriting: "))
# print("0.1 kg konfetning narxi: ", konfet_narxi * 0.1)
# print("0.2 kg konfetning narxi: ", konfet_narxi * 0.2)
# print("0.3 kg konfetning narxi: ", konfet_narxi * 0.3)
# print("0.4 kg konfetning narxi: ", konfet_narxi * 0.4)
# print("0.5 kg konfetning narxi: ", konfet_narxi * 0.5)
# print("0.6 kg konfetning narxi: ", konfet_narxi * 0.6)
# print("0.7 kg konfetning narxi: ", konfet_narxi * 0.7)
# print("0.8 kg konfetning narxi: ", konfet_narxi * 0.8)
# print("0.9 kg konfetning narxi: ", konfet_narxi * 0.9)
# print("1 kg konfetning narxi: ", konfet_narxi * 1)



# 6-masala
# konfet_narxi = float(input("Konfetning 1 kilogramm narxini kiriting: "))
# for i in range(12, 21, 2):
#     print(str(i / 10) + " kg konfetning narxi: ", konfet_narxi * (i / 10))
# print("2 kg konfetning narxi: ", konfet_narxi * 2)



# 7-masala
# a = int(input("a ni kiriting: "))
# b = int(input("b ni kiriting: "))
# summa = 0
# for i in range(a, b+1):
#     summa += i
# print("Butun sonlar yig'indisi: ", summa)



# 8-masala
# a = int(input("a ni kiriting: "))
# b = int(input("b ni kiriting: "))
# ko_paytma = 1
# for i in range(a, b+1):
#     ko_paytma *= i
# print("Butun sonlar ko'paytmasi: ", ko_paytma)



# 9-masala
# a = int(input("a ni kiriting: "))
# b = int(input("b ni kiriting: "))
# summa = 0
# for i in range(a, b+1):
#     summa += i ** 2
# print("Butun sonlar kvadratlarining yig'indisi: ", summa)



# 10-masala
# n = int(input("n butun soni: "))
# s = 0
# for i in range(1, n+1):
#     s += 1/i
# print("Yig'indi: ", s)



# 11-masala
# n = int(input("n butun soni: "))
# s = 0
# for i in range(n+1, 2*n+10):
#     s += i**2
# print("Yig'indi: ", s)



# 12-masala
# n = int(input("n butun soni: "))
# s = 1.1
# for i in range(2, n+1):
#     s *= i/10 + 1
# print("Yig'indi: ", s)



# 13-masala
# n = int(input("n butun soni: "))
# s = 0
# for i in range(1, n+1):
#     s += (-1)**(i+1) * i/10 + (i+1)/10
# print("Yig'indi: ", s)



# 14-masala
# n = int(input("n butun soni: "))
# s = 0
# for i in range(1, 2*n, 2):
#     s += i
#     print(i, "ning kvadrati:", i**2)
# print("Natija:", s)



# 15-masala
# n = int(input("n ni kiriting: "))
# a = int(input("a ni kiriting: "))
# print(f"{a} ning {n}-darajasi {a**n} ga teng")