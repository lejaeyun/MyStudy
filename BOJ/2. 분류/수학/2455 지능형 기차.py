# https://www.acmicpc.net/problem/14888

import sys
input = sys.stdin.readline

def getMaxNumInSubway(subway_inout_list):
    max_num = 0
    current_num = 0
    for inout_list in subway_inout_list:
        out, enter = inout_list
        current_num = current_num - out + enter
        max_num = max(max_num,  current_num)
    return max_num

def main():
    subway_inout_list = list()
    for _ in range(4):
        subway_inout_list.append(list(map(int, input().split())))
    print(getMaxNumInSubway(subway_inout_list))

main()
