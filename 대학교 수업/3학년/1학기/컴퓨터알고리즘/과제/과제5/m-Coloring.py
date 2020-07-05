# 간선에 대한 연결 확인
W = [ [0,1,0,1,0,0] ,
      [1,0,1,0,1,0] ,
      [0,1,0,0,0,1] ,
      [1,0,0,0,1,0] ,
      [0,1,0,1,0,1] ,
      [0,0,1,0,1,0] ]
# 컬러 개수
color = ['Red' , 'White', 'Green']
# 색칠한 Vertex 배열
vcolor = [0 for _ in range(len(W))]
count = 1
def coloring(i) :
        global count
        if (promising(i)) :
                # 0은 이미 색칠해서 들어오므로 -1과 비교
                if (i == len(W)-1) :
                        print(count, end = " ")
                        count += 1
                        for n in vcolor :
                                print(n, end= " ")
                        print()
                else :
                        for j in range(0,len(color)) :
                                vcolor[i+1] = color[j]
                                coloring(i+1)

# 연결된 Vertex와 같은 색이 존재하는지 체크
# 같은 색이 아니라면 True를 리턴 같은 색이 존재한다면 False를 리턴
def promising(i) :
        j = 0
        switching = True
        while (j<i and switching) :
                if (W[i][j] == 1 and vcolor[i] == vcolor[j]) :
                        switching = False
                j += 1
        return switching
# 3가지 색에 대한 결과값
for j in range(0,len(color)) :
        vcolor[0] = color[j]
        coloring(0)
