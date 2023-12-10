sum = 0
with open('Day4/input.txt') as file:
    for line in file:
        line = line.strip()
        line = line.split('|')
        mynums = line[0].split(':')[1].split(' ')
        mynums = [item for item in mynums if item != '']
        gamenums = line[1].split(' ')
        count = len([item for item in gamenums if item != '' and item in mynums])
        if count > 0:
            sum += 2 ** (count-1)

print(sum)
