import re

f = open('day2_data.txt', 'r')
data = f.read()
data = data.split('\n')
sum = 0
for i in range(len(data)):
    r = re.compile("\ \w+")
    m = r.findall(data[i])
    game_id = int(m[0])
    indicator = 1
    for j in range(2, len(m), 2):
        if ('blue' in m[j]):
            if int(m[j - 1]) > 14:
                indicator = 0
        elif ('red' in m[j]):
            if int(m[j - 1]) > 12:
                indicator = 0
        elif ('green' in m[j]):
            if int(m[j - 1]) > 13:
                indicator = 0
    sum += game_id * indicator
print(sum)
