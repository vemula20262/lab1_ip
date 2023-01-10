# set1 = set()
# set2 = set()
# n = int(input("enter the number "))
# for i in range(n + 1):
#     if (i % 3 == 0):
#         set1.add(i)
#     if (i % 5 == 0):
#         set2.add(i)
#
#
# print(set1.intersection(set2))

# how to remove the elemnet from a tupple
# def remove(tup, n):
#     return tup[:n] + tup[n + 1:]
# tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(remove(tup, 5))


#question3

# n = int(input("enter the number "))
# tupel = ()
# for i in range(n):
#     k = int(input("enter the number "))
#     tupel = tupel + (k,)
# print(tupel[:4] + tupel[5:]+(5,))

#question4

# n = input("enter the string")
# dict = {}
# flag = 0
# for i in n:
#     if i in dict:
#         dict[i] += 1
#         flag = 1
#
#     else:
#         dict[i] = 1
# if flag == 1:
#     print("not a heterogram")
# else:
#     print("heterogram")
# for i in dict:
#     print(i, dict[i])

#question5
# k = dict(input("enter the key value pair"))
# k = {'Ram': 20, 'Shyam': 80, 'Mohan': 45, 'Rahul': 16, 'Heena': 17, 'Neha': 15, 'Salman': 18}
# l = {}
# for i in k:
#     if k[i]>=18:
#         l[i] = k[i]
# print(l)

#question6
