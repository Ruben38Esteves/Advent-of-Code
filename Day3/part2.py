import math

matrix = []

with open("Day3/input.txt",'r') as file:
    for line in file:
        line = line.strip()
        matrix.append(line)


def checkSymbol(i,j):
    if i>=0 and j>=0 and i<len(matrix) and j<len(matrix[i]):
        if matrix[i][j].isdigit():
            return True
        else:
            return False


def getNums(i,j):
    nums=[]
    if not checkSymbol(i,j):
        if checkSymbol(i,j-1):
            num=""
            it = j-1
            while checkSymbol(i,it):
                num+=matrix[i][it]
                it-=1
            nums.append(int(num[::-1]))
        if checkSymbol(i,j+1):
            num=""
            it = j+1
            while checkSymbol(i,it):
                num+=matrix[i][it]
                it+=1
            nums.append(int(num))
    else:
        if checkSymbol(i,j-1) and checkSymbol(i,j+1):
            num= matrix[i][j-1]+matrix[i][j]+matrix[i][j+1]
            nums.append(int(num))
        elif not checkSymbol(i,j-1):
            num=""
            it = j
            while checkSymbol(i,it):
                num+=matrix[i][it]
                it+=1
            nums.append(int(num))
        elif not checkSymbol(i,j+1):
            num=""
            it = j
            while checkSymbol(i,it):
                num+=matrix[i][it]
                it-=1
            nums.append(int(num[::-1]))
    return nums
    


def checkAdj(i,j):
    nums = 0
    numbers = []
    if checkSymbol(i,j-1):
        nums+=1
    if checkSymbol(i,j+1):
        nums+=1
    line1=""
    if checkSymbol(i-1,j-1):
        line1+="a"
    else:
        line1+=" "
    if checkSymbol(i-1,j):
        line1+="a"
    else:
        line1+=" "
    if checkSymbol(i-1,j+1):
        line1+="a"
    else:
        line1+=" "
    line2=""
    if checkSymbol(i+1,j-1):
        line2+="a"
    else:
        line2+=" "
    if checkSymbol(i+1,j):
        line2+="a"
    else:
        line2+=" "
    if checkSymbol(i+1,j+1):
        line2+="a"
    else:
        line2+=" "
    nums+=len(line1.split())
    nums+=len(line2.split())
    if nums==2:
        if len(line1.split())>0:
            list1 = getNums(i-1,j)
            for item in list1:
                numbers.append([item])
        if len(line2.split())>0:
            list1 = getNums(i+1,j)
            for item in list1:
                numbers.append([item])
        if checkSymbol(i,j-1):
            number = matrix[i][j-3:j]
            number = number.replace(".","")
            numbers.append([int(number)])
        if checkSymbol(i,j+1):
            number = matrix[i][j+1:j+4]
            number = number.replace(".","")
            numbers.append([int(number)])
    return numbers

i=0
j=0
sum=0
while i < len(matrix):
    while j < len(matrix[i]):
        if matrix[i][j]=='*':
            numbers = checkAdj(i,j)
            if len(numbers)==2:
                flat_numbers = [item for sublist in numbers for item in sublist]
                print('found a * with 2 numbers!'+ str(flat_numbers))
                sum+= math.prod(flat_numbers)
                print('product: '+ str(math.prod(flat_numbers))+' and the total is now: '+ str(sum))
        j+=1
    i+=1
    j=0
print(sum)