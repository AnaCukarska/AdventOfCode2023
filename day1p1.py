f = open('day1_data.txt', 'r')
data = f.read()
data = data.split('\n')

sum = 0

for j in range(len(data)):
    i = [x.isdigit() for x in data[j]]
    digit1 = int(data[j][i.index(True)])
    digit2 = int(data[j][-i[::-1].index(True) - 1])
    sum += 10 * digit1 + digit2

# print(sum)