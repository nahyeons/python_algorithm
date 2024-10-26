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

# 3) 딕셔너리형
bk = {
    "name" : "admin",
    "age" : 20,
    "address" : "서울"
}

print(bk['name']) #admin
print(bk['age']) #20
print(bk['address']) #서울

# >> 딕셔너리형 + 리스트형

people = [
    {
        "name" : "cassiel",
        "age" : "19",
        "address" : "부산"
    },
    {
        "name" : "evren",
        "age" : "29",
        "address" : "서울"
    },
    {
        "name" : "lucius",
        "age" : "34",
        "address" : "군산"
    }
]

print(people[0]['age']) #19
print(people[1]['name']) #evren
print(people[2]['address']) #군산

# 3. 함수
# 함수를 정의하는 이름은 마음대로 정할 수 있음!

#수학문제에서
    # f(x) = 2*x+3
    # y = f(2)
    # y의 값은? 7

# js 에서는?
#function f(x) {
#   return 2*x+3
# }

# 파이썬에서는?
# def f(x):
    # return 2*x+3

# y = f(2)
# y 값은? 7

# 함수 응용
def sum_all(a,b,c):
    return a+b+c

def mul(a,b):
    return a*b

result = sum_all(1,2,3) + mul(10,10)

print(result) #106