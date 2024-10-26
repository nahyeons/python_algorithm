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

fruits = ["포도", "귤", "키위", "딸기", "블루베리", "수박", "참외", "홍시", "메론"]

for fruit in fruits:
    print(fruit) # "포도", "귤", "키위", "딸기", "블루베리", "수박", "참외", "홍시", "메론"

count = 0
for f in fruits:
    if f == "감":
        count += 1 #count = count + 1 (반복문 돌다가 사과가 있으면 1을 더하고 저장)

print(count) #0

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