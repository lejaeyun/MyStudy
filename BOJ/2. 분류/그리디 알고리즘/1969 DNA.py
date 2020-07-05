import sys
input = sys.stdin.readline

n, length = map(int, input().split())
dna = list()

for _ in range(n) :
    dna.append(input().rstrip())

result = ""
result_distance = 0
for i in range(length) :
    dna_lst = [ [0,'A'], [0,'C'], [0, 'G'], [0, 'T'] ]
    for j in range(n) :
        for k in range( 4 ) :
            if dna[j][i] == dna_lst[k][1] :
                dna_lst[k][0] += 1
                
    dna_lst.sort()
    m = dna_lst[-1][0]
    tmplst = list()
    for k in range( 4 ) :
        if dna_lst[k][0] == m :
            tmplst.append(dna_lst[k][1])
    tmplst.sort()
    result_distance += n - m
    result += tmplst[0]
    

print(result)
print(result_distance)
        
