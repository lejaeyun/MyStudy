# -*- coding: utf-8 -*-
"""
Created on Sun May 31 15:15:34 2020

@author: 재윤
"""
# priority queue
import heapq
import sys
import os

# Huffman Code Node Define
class Node :
    def __init__(self, symbol, frequency) :
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None
        
    def setleft(self, left) :
        self.left = left
        
    def setright(self, right) :
        self.right = right
    
    def setleftright(self,left , right) :
        self.setleft(left)
        self.setright(right)

# binary code To original code
def decoding(code, data) :
    decoding = ""
    word = ""
    key = code.keys()
    for c in data :
        # if binary code exist
        # plus original code
        if word in key :
            decoding += code[word]
            word = ""
        word += c    
    # last word
    decoding += code[word]
    return decoding

def encoding(huffmanTree, data) :
    code = mk_Code(huffmanTree, 0)
    encoding = ""
    # if word exist
    # plus binary code 
    for c in data :
        encoding += code[c]
    return encoding

# huffmantree To Code
# type 0 ('q' : 111)
# For encoding
# type 1 (111 : 'q')
# For decoding
def mk_Code(huffmanTree,mktype) :
    code = dict()
    tmpcode = list()
    tmpcode.append([huffmanTree,""])
    
    while tmpcode :        
        nxtnode, nxtcode = tuple(tmpcode.pop())
        # if leftnode exist
        if nxtnode.left != None :
            tmpcode.append([nxtnode.left,nxtcode+'0'])
        # if rightnode exist    
        if nxtnode.right != None :
            tmpcode.append([nxtnode.right,nxtcode+'1'])
        # Enter Code
        if nxtnode.left == None and nxtnode.right == None :
            # type 1 (111 : 'q')
            # For decoding
            if mktype == 1 :
                code[nxtcode] = nxtnode.symbol
            # type 0 ('q' : 111)
            # For encoding
            if mktype == 0 :
                code[nxtnode.symbol] = nxtcode
    
    return code


# Make huffman Tree
def mk_huffmanTree(data) :
    freq_dict = dict()
    # make symbol and frequency
    for d in data :
        if d not in freq_dict.keys() :
            freq_dict[d] = 1
        else :
            freq_dict[d] = freq_dict[d] + 1
    
    # List (freq, symbol)
    freq_symbol = list()
    for sym,freq in list(freq_dict.items()) :
        freq_symbol.append([freq, sym, Node(sym, freq)])
    
    # Make Priority Queue
    heapq.heapify(freq_symbol)
    
    for i in range(len(freq_symbol)-1) :
        # pop
        first = heapq.heappop(freq_symbol)
        second = heapq.heappop(freq_symbol)
        # make fre,sym,node
        lfreq, lsym, lnode = tuple(first)
        rfreq, rsym, rnode = tuple(second)
        # make parent_node
        pfreq, psym = lfreq+rfreq, lsym+rsym
        parent_node = Node(psym ,pfreq)
        parent_node.setleftright(lnode, rnode)
        # enqueue
        heapq.heappush(freq_symbol, [pfreq, psym, parent_node])
        
    result_huffmantree = heapq.heappop(freq_symbol)[2]
    
    return result_huffmantree

def main() :
    
    if len(sys.argv) != 3 :
        print('Encoding')
        print("Usage : PA03.py -c [INPUT FILE]")
        print('Decoding')
        print("Usage : PA03.py -d [INPUT FILE]")
        return
    # Encode Type
    code_type = sys.argv[1]
    # Encode
    if code_type == "-c" :
        filename = sys.argv[2].rstrip()
        data = ""
        # delete newline
        with open(filename,'r') as f :
            for l in f.readlines() :
                data += l.replace('\n','')
        huff_tree = mk_huffmanTree(data)
        code = mk_Code(huff_tree,0)
        encode = encoding(huff_tree,data)
        print("- 문자 총 개수 : ", len(code))
        print("- 문자열 빈도수")
        for d in list(code.items()) :
            print(' ' + d[0]," : ",d[1])
        # 바이너리 파일 저장
        with open(filename+'.zip','wb') as f :
            for d in code.items() :
                f.write((d[0] + ',' + str(d[1]) + ' ').encode())
            f.write('\n'.encode())
            f.write(str(int(encode,2)).encode())
        print("- 압축률 : ",round((os.path.getsize(filename+'.zip')/os.path.getsize(filename)) * 100),'%')
    # Decode    
    elif code_type == "-d" :
        filename = sys.argv[2].rstrip()
        data = ""
        with open(filename,'rb') as f :
            for l in f.readlines() :
                data += l.decode()
        ds = data.split()
        tmpcode = ds[:-1]
        data = str(bin(int(ds[-1]))).split('b')[1]
        code = dict()
        for c in tmpcode :
            alpha, alpha_code = tuple(c.split(','))
            code[alpha_code] = alpha
        decode = decoding(code,data)
        print("- 원본 파일 내용")
        print(decode)
        with open(filename.split('.')[0],'w') as f :
            f.write(decode)
    # Else
    else :
        print("Check Your argv plz")

main()
