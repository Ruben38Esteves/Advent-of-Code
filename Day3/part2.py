matrix = []

with open("Day3/input.txt",'r') as file:
    for line in file:
        line = line.strip()
        matrix.append(line)



def checkSymbol(i,j):
    if i>=0 and j>=0 and i<len(matrix) and j<len(matrix):
        if matrix[i][j].isdigit():
            return True
        else:
            return False


def getNums(i,j,n):
    j1 = j-3
    if j1 < 0:
        j1 = 0
    j2 = j+3
    if j2 >= len(matrix[i]):
        j2 = len(matrix[i]) - 1
    line = matrix[i][j1:j2+1]
    

def checkAdj(i,j):
    nums = 0
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
            
    else:
        return False

i=0
j=0
sum=0
while i < len(matrix):
    while j < len(matrix[i]):
        if matrix[i][j]=='*':
            if checkAdj(i,j):
                sum+=1
                print(i,j)
        j+=1
    i+=1
    j=0
print(sum)