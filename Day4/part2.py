with open('Day4/input.txt') as file:
    i = 0
    copies= {}
    sum=0
    for line in file:
        i+=1
        copies[i] = copies.get(i, 0) + 1
        line = line.strip()
        line = line.split('|')
        mynums = [item for item in line[0].split(':')[1].split(' ') if item != '']
        count = len([item for item in line[1].split(' ') if item != '' and item in mynums])
        while copies[i] > 0:
            for x in range(i+1, i+count+1):
                copies[x] = copies.get(x, 0) + 1
            sum +=1
            copies[i] -= 1
        del copies[i]
print(sum)
