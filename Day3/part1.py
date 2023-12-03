matrix = []

with open("Day3/input.txt",'r') as file:
    for line in file:
        line = line.strip()
        matrix.append(line)

def checkSymbol(i,j):
    if i>0 and j>0 and i<len(matrix) and j<len(matrix):
        if matrix[i][j]=='.' or matrix[i][j].isdigit():
            return False
        else:
            return True



def checkAdj(i,j):
    if checkSymbol(i,j-1):
        return True
    if checkSymbol(i,j+1):
        return True
    if checkSymbol(i-1,j-1):
        return True
    if checkSymbol(i-1,j):
        return True
    if checkSymbol(i-1,j+1):
        return True
    if checkSymbol(i+1,j-1):
        return True
    if checkSymbol(i+1,j):
        return True
    if checkSymbol(i+1,j+1):
        return True
    return False

i=0
j=0
sum=0
while i < len(matrix):
    while j < len(matrix[i]):
        if matrix[i][j].isdigit():
            foundchar = False
            num = ""
            while j < len(matrix[i]) and matrix[i][j].isdigit():
                num += str(matrix[i][j])
                if not foundchar and checkAdj(i,j):
                    foundchar = True
                j+=1
            if foundchar:
                sum+=int(num)
                print(num)
            j-=1
        j+=1
    i+=1 
    j=0
print(sum)