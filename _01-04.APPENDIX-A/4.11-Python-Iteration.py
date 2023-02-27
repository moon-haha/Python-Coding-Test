# # 1~9 sum while

# i = 1
# result = 0

# while i <= 9:
#     result += i
#     i += 1

# print(result)

# # 1~9 sum odd numger
# i = 1
# result = 0

# while i <= 9:
#     if i % 2 == 1:
#         result += i
#     i += 1

# print(result)


# #for
# array = [9, 8, 7, 6, 5]

# for x in array:
#     print(x)

# # for range
# result = 0
# for i in range(1, 10):
#     result += i

# print(result)

# # 1 ~ 30 int sum

# result = 0
# for i in range(1, 31):
#     result += i
# print(result)

# # for continue
# result = 0
# for i in range(1, 10):
#     if i % 2 == 0:
#         continue #짝수면 더하지 않음
#     result += i
# print(result)

# # for break

# i = 1
# while True:
#     print("i:", i)
#     if i == 5:
#         break ## 5가 되면 탈출
#     i += 1

# # 합격 여부 판단 예제
# scores = [90, 95, 77, 65, 97]

# for i in range(5):
#     if scores[i] >= 80:
#         print(i+1, "번 학생 합격")

# # 특정 번호 학생 제외
# scores = [90, 95, 77, 65, 97]
# cheating = {2, 4}

# for i in range(5):
#     if i + 1 in cheating:
#         continue
#     if scores[i] >= 80:
#         print(i+1, "번 학생 합격")

# 구구단, 중첩된 반복문(이중 for 문)

for i in range(2, 10):  # 2~9단까지
    for j in range(1, 10):  # 1~9 곱해준다
        print(i, 'X', j, '=', i*j)
    print()
