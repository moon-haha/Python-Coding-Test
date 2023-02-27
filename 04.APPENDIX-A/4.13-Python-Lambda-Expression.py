# # 람다 표현식

# def add(a, b):
#     return a+b


# # 일반적 사용
# print(add(3, 7))

# # 람다 표현식
# print((lambda a, b: a+b)(3, 7))
# # a, b 매개변수, 식, 값

# # 람다 표현식 예시:

# array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]


# def my_key(x):
#     return x[1]


# print(sorted(array, key=my_key))
# # 내장 함수에서 자주 사용되는 람다함수
# print(sorted(array, key=lambda x: x[1]))
# # 리스트(튜플)을 sorted로 정렬하는데, 두번째 원소[1]를 기준으로 정렬한다.

# 람다 표현식 예시 : 여러 개 리스트
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
result = map(lambda a, b: a+b, list1, list2)
#list 1, list 2의 매 원소 하나씩 받아서 a+b 해서 result에 넣는다.
print(list(result))
