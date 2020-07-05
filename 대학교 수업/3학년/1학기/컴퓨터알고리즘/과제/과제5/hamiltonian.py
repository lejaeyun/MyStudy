# 간선에 대한 Weight
W = [ [0,1,0,2,0,0] ,
      [3,0,4,0,5,0] ,
      [0,6,0,0,0,7] ,
      [8,0,0,0,9,0] ,
      [0,10,0,11,0,12] ,
      [0,0,13,0,14,0] ]

# 연결된 Vertex 배열
vindex = [0 for _ in range(len(W))]
# 최대값을 저장할 글로벌 변수
maximum = 0

def hamiltonian(i) :
        global maximum
        if (promising(i)) :
                if (i == len(W)-1) :
                        visitmax = 0
                        # 간선의 총합을 구함
                        for i in range(1, len(W)) :
                                start = vindex.index(i-1)
                                end = vindex.index(i)
                                visitmax += W[start][end]
                        print(vindex)
                        # max값을 maximum에 대입
                        maximum = max(maximum, visitmax)
                else :
                        # 모든 변수 Visit
                        for j in range(0,len(W)) :
                                vindex[i+1] = j
                                hamiltonian(i+1)

# Visit 했던 Vertex가 있는지 체크
# 간선이 연결되어있는지 체크
def promising(i) :
        j = 0
        switching = True
        if i != 0 and W[vindex[i-1]][vindex[i]] == 0 :
                switching = False
        if vindex[i] in vindex[:i] :
                switching = False
        return switching

result = list()
# 시작점을 다르게하여 출발
for j in range(len(W)) :
        vindex = [0 for _ in range(len(W))]
        vindex[0] = j
        hamiltonian(0)
        
print(maximum)
