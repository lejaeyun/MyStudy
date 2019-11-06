import itertools

arr = ["A", "B"]
result_arr = list()
for txt in arr :
    f = open("txt\\"+txt +".txt","w")
    
for i in range(2, len(arr) + 1) :
    result_arr.extend(list(itertools.combinations(arr,i)))
    

for k in arr :
    for j in arr :
        if k != j :
            f = open("txt\\"+j +".txt","a")
            f.write("    #100 " + j + " = 1'b0;\n")
            f.write("    #100 " + j + " = 1'b0;\n")
            f.close()
        else :
            f = open("txt\\"+ j +".txt","a")
            f.write("    #100 " + j + " = 1'b1;\n")
            f.write("    #100 " + j + " = 1'b0;\n")
            f.close()

for l in result_arr :
    for k in arr :
        if k not in l :
            f = open("txt\\"+ k +".txt","a")
            f.write("    #100 " + k + " = 1'b0;\n")
            f.write("    #100 " + k + " = 1'b0;\n")
            f.close()
        else :
            f = open("txt\\"+ k +".txt","a")
            f.write("    #100 " + k + " = 1'b1;\n")
            f.write("    #100 " + k + " = 1'b0;\n")
            f.close()

