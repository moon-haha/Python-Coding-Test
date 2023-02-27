# # 데이터의 갯수 입력
# n = int(input())

# data = list(map(int, input().split()))
# # input()
# # input().split()
# # map(int,input().split())
# # 패턴
# # n = int(input())
# # list(map(int,input().split()))

# # 내림차순 후 출력
# data.sort(reverse=True)
# print(data)

# # 패킹, 3개만 딱 데이터 받기
# a, b, c = list(map(int, input().split()))

# # 빠르게 입력 받기
# import sys
# # 문자열 입력 받기
# data = sys.stdin.readline().rstrip()
# print(data)

# 출력을 위한 전형적인 소스코드
a = 1
b = 2
print(a, b)  # 줄바꿈 실행됨
print(7, end="")  # 띄어쓰기 실행됨
print(8, end="")  # 띄어쓰기 실행됨

answer = 7
print(' 정답은' + str(answer) + ' 입니다.')
