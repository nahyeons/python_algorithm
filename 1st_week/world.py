# 조건문
#  if/else

def is_adult(age):
    if age > 20:
        print("성인입니다.")
    else:
        print("청소년이에요")

is_adult(30)

# 반복문(for문)
#  무조건 리스트와 함께 쓰임!

fruits = ["포도", "귤", "키위", "딸기", "블루베리", "딸기", "참외", "홍시", "메론"]

for fruit in fruits:
    print(fruit) # "포도", "귤", "키위", "딸기", "블루베리", "수박", "참외", "홍시", "메론"

count = 0
for f in fruits:
    if f == "감": #감의 갯수
        count += 1 #count = count + 1 (반복문 돌다가 사과가 있으면 1을 더하고 저장)

print(count) #0

#딸기, 홍시 갯수
def count_fruit(target):
    count = 0
    for fruit in fruits:
        if fruit == target:
            count += 1
    return count

strawberry_count = count_fruit("딸기") #딸기 갯수
print(strawberry_count) #2

soft_persimmon_count = count_fruit("홍시") #홍시 갯수
print(soft_persimmon_count) #1

#반복문 응용

def count_fruit(fruit_name):
    fruits = ["포도", "귤", "키위", "딸기", "블루베리", "수박", "참외", "홍시", "메론", "포도", "귤"]
    count = 0

    for f in fruits:
        if f == fruit_name:
            count += 1

    return count

print(count_fruit("사과")) #0
print(count_fruit("귤")) #2
print(count_fruit("딸기")) #1
print(count_fruit("메론")) #1
print(count_fruit("키위")) #1


#조건문, 반복문 응용

people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27}
]

#모든 사람의 이름, 나이 출력
for person in people:
    print(person['name'], person['age'])

#이름을 받으면 나이를 리턴해주는 함수
def get_age(myname):
    for person in people:
        if person['name'] == myname:
            return person['age']
    return '해당하는 이름이 없습니다.'

print(get_age('carry')) #38
print(get_age('kay')) #해당하는 이름이 없습니다.