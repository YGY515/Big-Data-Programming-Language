# -*- coding: utf-8 -*-
"""
1차과제 3번문제
<사용자로부터 5개의 실수를 입력 받아 실수들의 통계량을 산출하기>
정보융합학부 2020204097 윤가영
"""

import numpy
from scipy import stats


def homework3():
    numbers = []    # 숫자를 입력 받을 리스트
    count = 0
    
    for i in range (1, 6):    # 총 5개를 입력받기
        print("실수 5개를 입력하세요.(",i,"/5)")
        num = float(input())
        # input 함수는 입력받은 것을 문자열로 저장 때문에 실수 변환이 필요함
    
        numbers.append(num)
        count = count + 1
    
    
    f = 1    # 모두를 곱하는 값인 f 구하기
    for n in numbers:
        f = f*n    # n변수로 numbers 리스트를 돌며 요소 다 곱하기

    a = sum(numbers)    #전체합
    b = a / count       #평균
    c = numpy.median(numbers)    #중앙값
    d = stats.mode(numbers, keepdims = True)[0]    #최빈값
    e = numpy.std(numbers)       #표준편차

    print("\n전체 개수는",count,"개 합은",a,"평균은",b,"중앙값과 최빈값은 각각",c,d,
          "\n그리고 표준편차는",e,"이며 모두를 곱한 값은",f,"이에요.")
    
    
homework3()  # 실수들의 통계량 산출하는 함수 호출