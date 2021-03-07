# https://www.acmicpc.net/problem/14503

import sys
input = sys.stdin.readline

def findClearBox(matrix, head, pos):
    clear_cnt = 0
    change_cnt = 0
    while True:
        current_x, current_y, current_h = pos
        if matrix[current_y][current_x] == 0:
            matrix[current_y][current_x] = 2
            clear_cnt = clear_cnt + 1
            change_cnt = 0
        elif change_cnt == len(head):
            is_behind_wall, tmp_pos = cant_go_behind(matrix, pos)
            if is_behind_wall == False:
                pos = tmp_pos
                change_cnt = 0
            if is_behind_wall:
                break
        else:
            change_cnt = change_cnt + 1
            pos = is_sweep(matrix, head, pos)
    return clear_cnt
    
def is_sweep(matrix, head, pos):
    current_x, current_y, current_h = pos
    if current_h == 'N':
        target_x, target_y = current_x-1, current_y
    elif current_h == 'W':
        target_x, target_y = current_x, current_y+1
    elif current_h == 'S':
        target_x, target_y = current_x+1, current_y
    elif current_h == 'E':
        target_x, target_y = current_x, current_y-1

    if head.index(current_h)+1 == len(head):
        target_h = head[0]
    else:
        target_h = head[head.index(current_h)+1]

    ret = True if matrix[target_y][target_x] == 0 else False
    if ret:
        ret_pos = [target_x, target_y, target_h]
    else:
        ret_pos = [current_x, current_y, target_h]
    return ret_pos

def cant_go_behind(matrix, pos):
    current_x, current_y, current_h = pos
    if current_h == 'N':
        target_x, target_y = current_x, current_y+1
    elif current_h == 'W':
        target_x, target_y = current_x+1, current_y
    elif current_h == 'S':
        target_x, target_y = current_x, current_y-1
    elif current_h == 'E':
        target_x, target_y = current_x-1, current_y

    ret = True if matrix[target_y][target_x] == 1 else False
    ret_pos = [target_x, target_y, current_h]
    return ret, ret_pos
    

def main():
    head = ['N', 'W', 'S', 'E']
    matrix = list()
    N, M = list(map(int, input().split()))
    y, x, h = map(int, input().split())
    h = head[-h]

    for _ in range(N):
        matrix.append(list(map(int, input().split())))
    pos = [x, y, h]
    clear_cnt = findClearBox(matrix, head, pos)
    print(clear_cnt)

main()
