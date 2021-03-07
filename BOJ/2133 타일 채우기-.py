# https://www.acmicpc.net/problem/14888
'''
3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수를 구해보자.
'''
import sys
input = sys.stdin.readline

def getTileList(N):
    tile_list = [0, 0, 1, 3]
    for i in range(4, 30):
        next_tile_num = tile_list[i-2] + tile_list[i-1]
        tile_list.append(next_tile_num)
    return tile_list[N]


def main():
    N = int(input())
    print(getTileList(N))
    pass

main()
