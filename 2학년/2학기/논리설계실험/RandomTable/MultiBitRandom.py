import itertools
import random

Random_Num = 20 # Num of make random num
arr = ["A", "B", "C", "D"]
arrn = ["9", "9", "0", "12"]
result_arr = list()
result_arrn = list()

#file clearing
for filename in arr :
    f = open("txt\\"+ filename +".txt","w")

#multibit str
for j in arrn :
    s = ""
    for _ in range( int(j) + 1 ) :
        s += "0"
    result_arrn.append(s)
    
#file initialize
for i in arr :
    f = open("txt\\"+ i +".txt","a")
    f.write("  initial\n")
    f.write("  begin\n")
    f.write("    "+ i +" = " + str(int(arrn[arr.index(i)]) + 1) + "'b" \
            + (result_arrn[arr.index(i)]) +";\n")
    f.close()
    
#random comb
for _ in range(Random_Num) :
    for j in arr :
        f = open("txt\\"+ j +".txt","a")
        s = result_arrn[arr.index(j)]
        s = str(bin(int(s) | random.randrange(0, 2**(int(arrn[arr.index(j)]) + 1))))[1:]
        for i in range(int(arrn[arr.index(j)]) - (len(s) - 1) + 1) :
            s = s[0] + "0" + s[1:]
        f.write("    #100 "+ j +" = " + str(int(arrn[arr.index(j)]) + 1)\
                + "'" + s +";\n")
        f.write("    #100 "+ j +" = " + str(int(arrn[arr.index(j)]) + 1)\
                + "'b" + (result_arrn[arr.index(j)]) +";\n")
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

