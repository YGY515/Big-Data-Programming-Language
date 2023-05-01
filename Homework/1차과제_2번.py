# -*- coding: utf-8 -*-
"""
1차과제 2번문제
<자동차의 속도 출력하기>
정보융합학부 2020204097 윤가영
"""

def homework2():
    speed = int(input("자동차의 속도를 입력하세요. (단위: km/h): "))

    if (speed >= 100):
        print("고속")
    
    elif ((100 > speed) and (speed >= 60)):  # 무조건 60보다 넘는다고 하면 고속과 중복될 수 있음
        print("중속")
    
    elif (60 > speed):
        print("저속")
        
homework2()  # 속도 출력하는 함수 호출