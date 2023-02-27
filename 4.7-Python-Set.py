# # 초기화 방법 1
# data = set([1, 1, 2, 3, 4, 5])
# print(data)

# # 초기화 방법 2
# data = {1, 1, 2, 3, 4, 5, 5}
# print(data)

# # 연산

# a = set([1, 2, 3, 4, 5])
# b = set([3, 4, 5, 6, 7])

# print(a | b)
# print(a & b)
# print(a - b)

# 관련 함수
data = set([1, 2, 3])
print(data)

data.add(4)
print(data)

data.update([5, 6])
print(data)

data.remove(3)
print(data)
