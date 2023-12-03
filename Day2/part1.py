colorBalls= {
    'red': 12,
    'green': 13,
    'blue': 14
}

with open("Day2/part1.txt",'r') as file:
    sum=0
    for line in file:
        line = line.strip()
        possible = True
        line1 = line.split(':')
        gameN = line1[0][5:]
        tries = line1[1].split(';')
        for play in tries:
            hands = play.split(',')
            for hand in hands:
                parts = hand.split()
                color = parts[1]
                amount = int(parts[0])
                if amount > colorBalls[color]:
                    possible = False
                    print(hand + ' is not possible')
        if possible:
            print(gameN + ' is possible')
            sum+=int(gameN)
print('Sum of possible games is: ' + str(sum))
