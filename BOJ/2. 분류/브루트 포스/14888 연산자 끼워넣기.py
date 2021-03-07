# https://www.acmicpc.net/problem/14888

import sys
input = sys.stdin.readline
from itertools import permutations

def getCalculateResult(numbers, op_list):
    calculated_list = list()
    for ops in op_list:
        res_cal = numbers[0]
        for i in range(1, len(numbers)):
            cur_op = ops[i-1]
            num = numbers[i]
            res_cal = calOperator(res_cal, cur_op, num)
        calculated_list.append(res_cal)
    return calculated_list

def calOperator(left, operator, right):
    rtn = None
    if operator == '+':
        rtn = left + right
    elif operator == '-':
        rtn = left - right
    elif operator == '*':
        rtn = left * right
    elif operator == '%':
        rtn = abs(left) // abs(right)
        if left < 0:
            rtn = rtn * (-1)
    return rtn

def makeOperatorList(op_cnt):
    op_classes = ['+', '-', '*', '%']
    op_list = list()
    for op_index in range(len(op_classes)):
        cnt = op_cnt[op_index]
        op = op_classes[op_index]
        op_list.extend([op for _ in range(cnt)])
    op_list = list(permutations(op_list, len(op_list)))
    op_list = list(set(op_list))
    return op_list

def main():
    _ = int(input())
    numbers = list(map(int, input().split()))
    op_cnt = list(map(int, input().split()))
    op_list = makeOperatorList(op_cnt)
    result = getCalculateResult(numbers, op_list)
    print(max(result))
    print(min(result))

main()
