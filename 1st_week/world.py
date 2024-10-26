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

