#[부분 문자열 팰린드롬 확인 알고리즘]
#String이 주어질 때 Substring이 Palindrome(회문)인지 알아보는 알고리즘
#팰린드롬 == 문자열을 앞에서 읽으나 뒤에서 읽으나 동일한 문자가 나오는 문자열을 의미함.

def is_palindrome(s):
    # 문자열을 양쪽에서 비교하기 위해 앞뒤를 대칭적으로 잘라서 확인함
    left, right = 0, len(s) - 1
    
    # 앞뒤에서 한 문자씩 비교하며, 중앙에 도달할 때까지 확인
    while left < right:
        if s[left] != s[right]:
            return False  # 문자가 일치하지 않으면 팰린드롬이 아님
        left += 1
        right -= 1

    return True  # 모든 문자가 일치하면 팰린드롬임

# 테스트
print(is_palindrome("level"))  # True
print(is_palindrome("hello"))  # False

#[홀수, 짝수 구분하기]
number = input("정수 입력 >> ") #입력 받기
number = int(number)

if number % 2 == 0:
    print("짝수")

if number % 2 == 1:
    print("홀수")