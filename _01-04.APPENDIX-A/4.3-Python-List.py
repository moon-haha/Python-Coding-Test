# # 리스트 초기화
# a = [1, 2, 3, 4, 5, 6, 7, 8]
# print(a)

# # 4번째
# print(a[3])

# n = 10
# # 크키가 10이고 모든 값이 0인 1차원 리스트 초기화
# a = [0] * n
# print(a)

# 리스트의 인덱싱과 슬라이싱
# # 인덱싱
# a = [1, 2, 3, 4, 5, 6, 7, 8]
# # 여덟 번째 값
# print(a[7])

# # 뒤에서 첫 번째
# print(a[-1])

# # 뒤에서 세 번째
# print(a[-3])

# a[3] = 7
# print(a)
# # 슬라이싱
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # 네 번째 원소만 출력하기
# print(a[3])

# # 두 번째 원소부터 네 번째 원소까지
# print(a[1:4])

# # 리스트 컴프리헨션
# # array는 0~9까지의 수를 포함하는 리스트
# array = [i for i in range(10)]

# print(array)

# # 조건문 리스트 컴프리헨션
# # 1부터 19까지인데 2로 나눴을때 나머지가 1인 원소(홀수)만 포함
# array = [i for i in range(20) if i % 2 == 1]

# print(array)

# # 1 부터 9까지의 수들의 제곱 값을 포함하는 리스트

# array = [i * i for i in range(1, 10)]
# print(array)

# # 리스트 컴프리헨션과 일반적 코드 비교
# # 리스트 컴프리헨션

# array = [i for i in range(20) if i % 2 == 1]
# print(array)
# # 일반 코드

# array = []
# for i in range(20):
#     if i % 2 == 1:
#         array.append(i)

# print(array)

# # N X M 크기의 2차원 리스트 초기화
# n = 4
# m = 3
# # n번 반복할 때마다 m 길이인 list 초기화
# array = [[0] * m for _ in range(n)]
# print(array)

# # Hello World 5회 (i 필요 없으므로 언더바)
# for _ in range(5):
#     print("hello world")

# # List 관련 기타 메서드
# a = [1, 4, 3]
# print('기본 리스트 : ', a)

# a.append(2)
# print('원소 삽입 : ', a)

# a.sort()
# print("오름차순 정렬 : ", a)

# a.sort(reverse=True)
# print('내림차순 정렬 : ', a)

# a.reverse()
# print("원소 뒤집기 :", a)

# a.insert(2, 6)
# print("인덱스 2에 6 추가 : ", a)

# print("값이 3인 데이터 개수 : ", a.count(3))

# a.remove(6)
# print("6인 데이터 삭제 : ", a)

# # 리스트에서 특정 값 가지는 원소 모두 제거
# a = [1, 2, 3, 4, 5, 5, 5]
# remove_set = {3, 5}  # 집합 자료형

# # remove_list에 포함되지 않은 값을 저장한다
# result = [i for i in a if i not in remove_set]
# # i for i in a a라는 리스트를 i라는 변수로
# # 하나하나마다 remove_set에 포함 됐는지 아닌지 확인하고 남기기
# print(result)
