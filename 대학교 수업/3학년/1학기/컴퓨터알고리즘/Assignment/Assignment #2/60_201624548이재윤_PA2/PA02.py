# Dynamic Programming
# 201624548 이재윤

# mymatrix에서 반환한 maxTuple과 H를 이용하여 염기 서열을 되추적하는 함수
# direction을 이용하여 추적함.
# queue를 사용하여 구현
# 5개의 값만 구하도록 구현.
# First in First Out
# 속도를 빠르게 하기 위하여 덱(deque)을 사용
from collections import deque
def mytrace_back(startTuple, H, a, b) :
    queue = deque()
    result = list()
    i,j = startTuple[0], startTuple[1]
    
    # 0 = 원래 Sequence
    # 1 = 비교 Sequence
    # 2 = 현재 index (이를 통해 Direction과 Sequence를 추가한다)
    queue.append(["","",startTuple])
    
    while queue and len(result) < 5 :
        nxt = queue.popleft()
        buf_a_word, buf_b_word,nxtTuple = nxt[0], nxt[1], nxt[2]
        i,j = nxtTuple[0], nxtTuple[1]
        nextdirection = H[i][j][1]
        # 가능한 모든 방향에 대해 되추적
        for d in nextdirection :
            # word 원복
            a_word, b_word = buf_a_word, buf_b_word
            # 두 sequence가 같은경우
            if d == 0 :
                a_word = a[i-1] + a_word
                b_word = b[j-1] + b_word
                queue.appendleft([a_word, b_word, [i-1, j-1]])
            # 비교하는 Sequence에 Gap이 필요한 경우
            elif d == 1 :
                a_word = a[j-1] + a_word
                b_word = '-' + b_word
                queue.appendleft([a_word, b_word, [i-1, j]])
            # 비교당하는 Sequence에 Gap이 필요한 경우
            elif d == 2 :
                a_word = '-' + a_word
                b_word = b[i-1] + b_word
                queue.appendleft([a_word, b_word, [i, j-1]])
            # 진행 방향이 없다면 (0을 만난다면)
            # result 값에 추가한다
            elif d == -1 :
                result.append(a_word + ',' + b_word)
        
    return result

# dp를 이용하여 두 sequence를 scoring 하는 함수
# dp 배열을 바로 만들 시 Memory 초과 우려가 있어 dp 배열을 한줄씩 늘려나가도록 구성
def mymatrix(a, b):
    # 길이 선언
    length_a, length_b = len(a)+1, len(b)+1
    # DP 결과값을 저장할 리스트
    H = [[[0,[-1]] for _ in range(length_b)] ]
    # -가 들어갈 경우 Cost
    gap_cost = (5,2)

    # a의 길이동안 반복할 인덱스
    i = 1
    # 5번 이상 감소하면 (불일치 혹은 gap) 루프를 탈출하기 위한 cnt 선언
    cnt = 0
    # 최대값의 위치를 저장하기위한 tuple
    maxtuple = (0,0)
    # 최대값 체크를 위한 변수
    maximum, befmax, aftmax = 0,0,0
    
    # 끝날 때 까지 반복하거나,
    # 최고점수를 지나고 연속해서 5개가 불일치 혹은 gap이 나오는지 확인.
    while i < length_a and cnt <= 5 :
        H.append([[0,[-1]]])
        aftmax = 0
        for j in range(1,length_b) :
            # 방향을 결정, -1 = 방향없음, 0 대각선, 1 위, 2 왼쪽
            # 동일 값이 여러개일 때를 대비하여 List로 구현
            direction = []
            # 일치 +3 불일치 -2
            match = H[i - 1][j - 1][0] + (3 if a[i-1] == b[j-1] else - 2)
            # Gap penalty -5, -2 위쪽 방향
            # 연속되는 경우 (바로 이전의 direction에 1이 존재하는경우) 
            delete = H[i - 1][j][0] - (gap_cost[1] if 1 in H[i - 1][j][1] else gap_cost[0])
            # Gap penalty -5, -2 왼쪽 방향
            # 연속되는 경우 (바로 이전의 direction에 2가 존재하는경우)
            insert = H[i][j - 1][0] - (gap_cost[1] if 2 in H[i][j-1][1] else gap_cost[0])
            tmpmax = max(match, delete, insert, 0)
            # 가능한 모든 방향 추가
            if tmpmax == 0 : direction.append(-1)
            if tmpmax == match : direction.append(0)
            if tmpmax == delete : direction.append(1)
            if tmpmax == insert : direction.append(2)

            # 최대값 갱신
            if tmpmax > aftmax :
                aftmax = tmpmax
                tmptuple = (i,j)
            # 리스트에 추가
            H[i].append( [tmpmax, direction] )

        # 최대값과 최대값이 존재하는 위치 tuple을 갱신
        if maximum < aftmax :
            maximum = aftmax
            maxtuple = tmptuple
            cnt = 0
            
        # 불일치, Gap이 생길 경우 max 값이 내려가기 때문에 이를 이용하여 카운팅
        if befmax > aftmax :
            befmax = aftmax
            cnt += 1
        else :
            befmax = aftmax
            
        i += 1
        
    return maxtuple, H

# 두 시퀀스를 비교하는 함수.
# 결과 리스트와, 최대값이 존재하는 위치, 분석 매트릭스를 반환
def smith_waterman(a, b):
    a, b = a.upper(), b.upper()
    maxtuple, H = mymatrix(a, b)
    result = mytrace_back(maxtuple, H, a, b)
    return result, maxtuple, H

# Main
import sys
def main() :
    
    if len(sys.argv) != 3 :
        print("Usage : PA02.py [INPUT FILE] [INPUT FILE]")
        return
        
    inputFilenameList = [sys.argv[1], sys.argv[2]]

    # 파일을 읽어 배열에 저장
    String = list()
    for inputFilename in inputFilenameList :
        with open(inputFilename, "r") as f :
            tmpString = ""
            tmpList = f.readlines()
            for b in tmpList :
                tmpSegment = b.rstrip()
                if len(tmpSegment.split()) == 1 :
                    tmpString += tmpSegment
        String.append(tmpString)
    # 자기 자신의 SubSequence일 경우
    if String[1] in String[0] :
        print("Sub Sequence")
        with open('output_'+ inputFilenameList[0].split('.')[0] + '_' + inputFilenameList[1].split('.')[0] + '.algin', "w") as f :
            f.write(" -  서열1 : " + inputFilenameList[0] + ", " + str(len(String[0])) + '\n')
            f.write(" -  서열2 : " + inputFilenameList[1] + ', ' + str(len(String[1])) + '\n')
            f.write(" -  부분서열 : " + str(len(String[1]))  + '\n\n')
            
            print(" -  서열1 : " + inputFilenameList[0] + ", " + str(len(String[0])))
            print(" -  서열2 : " + inputFilenameList[1] + ', ' + str(len(String[1])))
            print(" -  부분서열 : " + str(len(String[1])) + '\n')
        return
            
        
    result,maxTuple, H = smith_waterman(String[0], String[1])
    cnt = 0

    # 결과값을 토대로 파일, 화면에 출력
    with open('output_'+ inputFilenameList[0].split('.')[0] + '_' + inputFilenameList[1].split('.')[0] + '.algin', "w") as f :
        f.write(" -  서열1 : " + inputFilenameList[0] + ", " + str(len(String[0])) + '\n')
        f.write(" -  서열2 : " + inputFilenameList[1] + ', ' + str(len(String[1])) + '\n')
        f.write(" -  부분서열 : " + str(H[maxTuple[0]][maxTuple[1]][0])  + '\n\n')
        
        print(" -  서열1 : " + inputFilenameList[0] + ", " + str(len(String[0])))
        print(" -  서열2 : " + inputFilenameList[1] + ', ' + str(len(String[1])))
        print(" -  부분서열 : " + str(H[maxTuple[0]][maxTuple[1]][0]) + '\n')
        
        for r in result :
            if cnt < 5 :
                tmplist = r.split(',')
                f.write("\t #" + str(cnt+1) + '\n')
                f.write("\t seq1 .." + tmplist[0]  + '..\n')
                f.write("\t seq2 .." + tmplist[1]  + '..\n')
                f.write("\n")
                print("\t #" + str(cnt+1))
                print("\t seq1 .." + tmplist[0]  + '..')
                print("\t seq2 .." + tmplist[1]  + '..\n')
            cnt += 1
    
main()




