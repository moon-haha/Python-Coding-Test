# data = dict()
# data['사과'] = 'Apple'
# data['바나나'] = 'Banana'
# data['코코넛'] = 'Coconut'
# # key (hash table)
# # 옳바른 상황에 맞게 사용
# print(data)


# if '사과' in data:
#     print("'사과'를 키로 가지는 데이터가 존재합니다.")

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

# 키 데이터 리스트
key_list = data.keys()
# 값 데이터 리스트
value_list = data.values()
print(key_list)
print(value_list)

# 키에 따른 값 하나씩 출력
for key in key_list:
    print(data[key])

b = {
    '홍길동': 97,
    '이순신': 98
}

print(b)
key_list = b.keys()  # 사전 키 객체
print(key_list)
key_list = list(b.keys())  # 리스트 형식
print(key_list)
print(b['이순신'])
