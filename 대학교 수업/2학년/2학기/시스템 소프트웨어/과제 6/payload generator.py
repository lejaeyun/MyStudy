
def generator(n, address) :
    result = ""

    for _ in range(n) :
        result += "00 "

    if len(address) < 16 :
        address = address + "0" * (16-len(address))
    
    temp = ""
    little_endian_address = ""
    for i in range(len(address)) :
        temp = temp + address[i] 
        if len(temp) == 2 :
            if temp == "00" :
                little_endian_address = little_endian_address + temp + " "
            else :
                little_endian_address = temp + " " + little_endian_address 
            temp = ""
            
    result = result + little_endian_address
    return result[0:-1]

def main() :
    num = 0x28
    address = "401adb"
    result = generator(num, address)
    print(result)
        
main()
