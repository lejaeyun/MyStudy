import matplotlib.pyplot as plt
import sys

def main() :
    inputFilename = "PA01-1_input.txt"
    
    line_segments = list()
    fig, ax = plt.subplots()
    
    with open(inputFilename, "r") as f :
        tmpList = f.readlines()
        for b in tmpList :
            tmpSegment = list(map(int, b.rstrip().split()))
            if tmpSegment[0] == -1 :
                break
            if len(tmpSegment) != 1 : # 처음 개수, -1 제외
                point1 = (tmpSegment[0], tmpSegment[1])
                point2 = (tmpSegment[2], tmpSegment[3])
                ax.plot([tmpSegment[0], tmpSegment[2]], [tmpSegment[1], tmpSegment[3]], 'x-')
              
    plt.show()

    
    print("Success!!")

main()

