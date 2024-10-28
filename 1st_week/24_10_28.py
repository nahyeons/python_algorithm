#시공간 복잡도

#시간복잡도 : 입력값과 문제를 해결하는 데 걸리는 시간과의 상관관계, 입력값이 2배로 늘어났을 때 문제를 해결하는데 걸리는 시간은 몇 배로 늘어났는지 보는것
#공간복잡도 : 입력값과 문제를 해결하는데 걸리는 공간과의 상관관계, 입력값이 2배로 늘어났을 때 문제를 해결하는데 걸리는 공간은 몇 배로 늘어났는지 보는것

#Q. a 부터 z 까지, 주어진 문자열에서 알파벳이 포함되어 있을 경우 처음 등장하는 인덱스를 반환하는 프로그램을 작성하세요. 포함되어있지 않을 경우 -1을 반환하시면 됩니다.

# 예를 들어 ‘sparta’가 주어질 경우 아래 배열을 반환합니다.
# [2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, 3, 0, 4, -1, -1, -1, -1, -1, -1]

import string

# 아스키 코드
# 1. 알파벳을 바로 꺼내오는 방법
print(string.ascii_lowercase)

# 2. ord 연산
print(ord('a'), ord('A'), ord('@'))  # 97 65 64

# 3. range
for i in range(10):
    print(i)

#시간복잡도
def get_idx_naive(word):
		# O(N^2) >> for 문이 2개라 최악의 경우 n^2 -->시간복잡도의 안좋은 방법
    result = [-1] * len(string.ascii_lowercase)
    for i in range(len(word)):
        char = word[i]
        for j in range(len(string.ascii_lowercase)):
            lo = string.ascii_lowercase[j]
            if result[j] == -1 and char == lo:
                result[j] = i
    return result


def get_idx(word): #for 문 1번 돌기때문에 시간이 단축
    # O(N)
    result = [-1]*len(string.ascii_lowercase)
    for i in range(len(word)):
        idx = ord(word[i]) - 97
        if result[idx] == -1:
            result[idx] = i
    return result


print(get_idx_naive('sparta'))
print(get_idx('sparta'))