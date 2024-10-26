#[기초공부]
#1. 변수 & 기본연산
a = 3
b = 2
c = a + b
d = a / b
e = a * b
f = a - b
a = a + 1 # a + 1 을 다시 a애 넣음 >> print 하면 3이 나왔지만 a = a + 1 하면 4로 결과값이 나온다.

print(a, b, c, d, e, f)

# 2. 자료형
#  1) 숫자, 문자형 
name = "bob"
age = 14

isAdult = age > 19 # >> isAdult = 14 > 19 즉, 14가 19보다 큰지, 작은지를 나타내기 때문에 True / Fals 로 결과값이 나옴

is_name = True # True 또는 False -> "Boolean"형이 들어갈 수도 있음

print(isAdult) # Fals

# 2) 리스트 형(Javascript의 배열형과 동일)
# >> 여러가지 자료형이 묶여서 순서에 따라서 저장되는 형태

shop = ["체리", "사과", "홍시"] # >> 0,1,2 ... 순서 / 0번 체리, 1번 사과, 2번 홍시

#print(shop) #['체리', '사과', '홍시']
print(shop[0]) #['체리']
print(shop[1]) #['사과']
print(shop[2]) #['홍시']
# print(shop[3]) # IndexError: list index out of range >> 범위를 벗어났음을 알려줌
print(shop[-1]) #>> 홍시 출력 (-넣으면 뒤에서 앞으로 출렫된다 '-2 사과' '-3 체리')