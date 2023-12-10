import os
import time

# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

def solution(my_string, target):
    answer = 0
    if 1 <= len(my_string) <= 100 and 1 <= len(target) <= 100 :
        if target in my_string:
            answer = 1
            print("target in my_string, answer is ", answer)
        else:
            answer = 0
            print("target not in my_string, answer is ", answer)
    else:
        print("Out of range")
    return answer

my_string = 'open source programing final assignment is python programming'
target = 'python'

answer = solution(my_string, target)
print(f'answer is {answer}')

