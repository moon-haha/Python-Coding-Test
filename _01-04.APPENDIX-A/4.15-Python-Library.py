# # 내장 함수
# # sum()
# result = sum([1, 2, 3, 4, 5])
# print(result)

# # min() , max()
# min_result = min(7, 3, 5, 2)
# max_result = max(7, 3, 5, 2)
# print(min_result, max_result)

# # eval() #수식 계산 반환
# result = eval("(3+5)*7")
# print(result)

# # sorted()
# result = sorted([9, 1, 8, 5, 4])
# reverse_result = sorted([9, 1, 8, 5, 4], reverse=True)
# print(result)
# print(reverse_result)

# # sorted() with key
# array = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
# result = sorted(array, key=lambda x: x[1], reverse=True)
# print(result)

# 순열과 조합
# # 패키지 가져오기
# from itertools import combinations
# from itertools import permutations

# data = ['A', 'B', 'C']  # 데이터 준비

# # 모든 순열 구하기
# result = list(permutations(data, 3))
# print(result)

# # 패키지 가져오기


# data = ['A', 'B', 'C']

# # 2개 뽑는 조합
# result = list(combinations(data, 2))
# print(result)

# # 중복 순열과 중복 조합

# # 패키지 - itertools
# from itertools import combinations_with_replacement
# from itertools import product

# data = ['A', 'B', 'C']

# # 중복을 허용하는 순열
# result = list(product(data, repeat=2))
# print(result)

# # 패키지 - itertools

# data = ['A', 'B', 'C']  # 데이터 준비

# result = list(combinations_with_replacement(data, 2))
# print(result)

# # Counter
# from collections import Counter

# # 반복 가능한 객체
# counter = Counter(['red', 'blue', 'red', 'red', 'green', 'blue', 'blue'])

# print(counter['blue'])  # blue 등장 횟수
# print(counter['green'])  # green 등장 횟수
# print(dict(counter))  # key-value 등장횟수 사전 자료형으로

# # 최대 공약수, 최소 공배수

# import math

# # LCM

# # 최소공배수 a*b / a,b의 최대공약수(머릿속으로 계산해보면 아하 됨)


# def lcm(a, b):
#     return a * b // math.gcd(a, b)


# print(lcm(21, 14))

# # GCD
# a = 21
# b = 14
# print(math.gcd(a, b))

# # 그외 팩토리얼, 원주율 등 포함한다.
