# #Task1
# def sum_of_digits(num):
#     sum = 0
#     while num != 0:
#         sum += num % 10
#         num //= 10
#     return sum
# def digit_sum(n):
#     n = n.split(".")
#     if len(n) > 1:
#         return sum_of_digits(int(n[0])) + sum_of_digits(int(n[1]))
#     else:
#         return sum_of_digits(int(n[0]))

# n = (input("Введите число типа int или float: "))
# print(digit_sum(n))

# #Task2
# def mult_result(n):
#     result = []
#     for i in range(1, n + 1):
#         mult = 1
#         for j in range(1, i + 1):
#             mult *= j
#         result.append(mult)
#     return result
# print(mult_result(4))

#Task3
# def substring_count(s, sub):
#     count = 0
#     while sub in s:
#         count += 1
#         s = s.replace(sub, "", 1)
#     return count
# print(substring_count("helloworld", "l"))

#Task4
# from math import *
# def points_distance(n, point1, point2):
#     quadratic_sum = 0
#     for i in range(n):
#         quadratic_sum += (int(point1[i]) - int(point2[i])) ** 2
#     return(sqrt(quadratic_sum))
# n = int(input("Введите размерность пространства "))
# point1, point2 = (input("Введите координаты точки ").split() for _ in range(2))
# print(points_distance(n, point1, point2))

import time
import random
def logic():
    start_time = time.time()
    for _ in range(100):
        predicate_number = random.randint(5, 25)
        predicates = [bool(random.randint(0, 1)) for _ in range(predicate_number)]
        print(not (any(predicates)) == all([not x for x in predicates]))
    print("--- %s seconds ---" % (time.time() - start_time))    
print(logic())