def update_values(ranges, values):
    result = []
    for value in values:
        result.append(value)
        for cenas in ranges:
            if value in range(cenas[1], cenas[1]+cenas[2]+1):
                result.pop()
                result.append(cenas[0]+value-cenas[1])
                break
    return result

ranges = []
with open('Day5/input.txt') as file:
    for line in file:
        line = line.strip()
        if line=='':
            if ranges != []:
                values = update_values(ranges, values)
                ranges.clear()
        elif line[0].isdigit():
            ranges.append([int(i) for i in line.split(' ')])
        elif line[:6]=='seeds:':
            values = line.split(':')[1].split(' ')[1:]
            values = [int(i) for i in values]

    values = update_values(ranges, values)
    ranges.clear()

print(min(values))
