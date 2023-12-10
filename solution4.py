import os
import time

# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000

def solution(r1, r2):
    answer = 0
    def count_points_in_circle(r):
        count = 0
        for x in range(-r, r+1):
            for y in range(-r, r+1):
                if x**2 + y**2 <= r**2:
                    count += 1
        return count
    answer = count_points_in_circle(r2) - count_points_in_circle(r1)

    return answer

answer = solution(5, 10)
print(f'answer is {answer}')