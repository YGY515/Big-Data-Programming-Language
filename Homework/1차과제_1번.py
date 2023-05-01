# -*- coding: utf-8 -*-
"""
1차과제 1번문제
<순서도를 조건문으로 코딩하기>
정보융합학부 2020204097 윤가영
"""

def homework1():
    
    print("고민 시작")
    Answer_1 = input("과제를 내 손으로 끝마친다 (Yes/No): ")

    if (Answer_1 == "Yes"):
        Answer_2 = input("야식을 먹을까? (Yes/No): ")
    
        if (Answer_2 == "Yes"):
            print("배부르게 불태운다")
    
        elif (Answer_2 == "No"):
            print("굶주리며 불태운다")

    else: 
        Answer_3 = input("과톱의 도움을 받는다 (Yes/No): ")
        if (Answer_3 == "No"):
            print("내일 배 끼고, 지금은 잔다")
        
        else: 
            Answer_2 = input("야식을 먹을까? (Yes/No): ")
        
            if (Answer_2 == "Yes"):
                print("배부르게 불태운다")
        
            elif (Answer_2 == "No"):
                print("굶주리며 불태운다")
        
    print("고민해결")

homework1()    # 순서도 함수 호출