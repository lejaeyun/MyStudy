""" start """

import itertools

arr = ["A", "B", "C", "D", "E"]
result_arr = list()

#file clearing
for filename in arr :
    f = open("txt\\"+ filename +".txt","w")

#make combinations
for i in range(2, len(arr) + 1) :
    result_arr.extend(list(itertools.combinations(arr,i)))
    
#initialize
for i in arr :
    f = open("txt\\"+ i +".txt","a")
    f.write("  initial\n")
    f.write("  begin\n")
    f.write("    "+ i +" = 1'b0;\n")
    f.close()
    
#only one charicter is 1
for k in arr :
    for j in arr :
        if k != j :
            f = open("txt\\"+ j +".txt","a")
            f.write("    #100 " + j + " = 1'b0;\n")
            f.write("    #100 " + j + " = 1'b0;\n")
            f.close()
        else :
            f = open("txt\\"+ j +".txt","a")
            f.write("    #100 " + j + " = 1'b1;\n")
            f.write("    #100 " + j + " = 1'b0;\n")
            f.close()
#comb
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

#endfile
for i in arr :
    f = open("txt\\"+ i +".txt","a")
    f.write("  end\n\n")
    f.close()

#combine files
result = ""
for i in arr :
    f = open("txt\\"+ i +".txt","r")
    result += f.read()
    f.close()
f = open("txt\\result.txt","w")
f.write(result)
f.close()

""" end """
