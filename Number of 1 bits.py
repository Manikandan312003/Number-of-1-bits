def findOneBit(number):
    count=0
    while(number):
        count+=number&1
        number=number>>1
    return count

print(findOneBit(int(input())))