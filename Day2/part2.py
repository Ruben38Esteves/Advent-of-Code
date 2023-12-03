colorBalls= {
    'red': 0,
    'green': 0,
    'blue': 0
}

def resetamounts(): 
    colorBalls['red'] = 0
    colorBalls['green'] = 0
    colorBalls['blue'] = 0


with open("Day2/part1.txt",'r') as file:
    sum=0
    for line in file:
        line = line.strip()
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
                    colorBalls[color] = amount
        power = colorBalls['red'] * colorBalls['green'] * colorBalls['blue']
        sum += power
        resetamounts()
print('Sum of possible games is: ' + str(sum))
