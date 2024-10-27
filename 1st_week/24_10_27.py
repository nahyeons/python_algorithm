#requests 라이브러리 사용하기 +list/dictionary/함수/if/for문 연습

#서울시 대기 OpenAPI에서, 중구의 미세먼지 값 가져오기
from pprint import pprint
import requests

r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
rjson = r.json()

# pprint(rjson) # 보기쉽게 예쁘게 프린트됨

gus = rjson['RealtimeCityAir']['row'] #모든 구의 IDEX_MVL 값 찍기
# pprint(gus)

for gu in gus:
	# print(gu['MSRSTE_NM'], gu['IDEX_MVL'])

#>> 이렇게 print 할 수 있지만 name으로 작성해서 프린트 할 수 도 있음

    gu_name = gu['MSRSTE_NM']
    gu_mise = gu['IDEX_MVL']
    # print(gu_name, gu_mise)
    if gu_mise < 60: # 조건 : IDEX_MVL 값이 60 미만인 구만 출력
        print(gu_name, gu_mise)


# 함수로 사용해보기
def get_gu_mise(name):
    r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
    rjson = r.json()

    gus = rjson['RealtimeCityAir']['row']
    for gu in gus:
        gu_name = gu['MSRSTE_NM']
        gu_mise = gu['IDEX_MVL']
        if gu_name == name:
            return gu_mise

    return "미세먼지가 없습니다"

print(get_gu_mise("중구"))
print(get_gu_mise("종로구"))
print(get_gu_mise("송파구"))
print(get_gu_mise("관악구"))