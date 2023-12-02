import re

f = open('day2_data.txt', 'r')
data = f.read()
data = data.split('\n')
sum = 0
for i in range(len(data)):
    game_id = str(data[i][4:data[i].index(':')])
    data_set = data[i][data[i].index(':') + 1:].split(';')
    max_blue = 0
    max_red = 0
    max_green = 0
    for k in range(len(data_set)):
        r = re.compile("\ \w+")
        m = r.findall(data_set[k])
        indicator = 1
        for j in range(1, len(m), 2):
            if ('blue' in m[j]):
                if int(m[j - 1]) > max_blue:
                    max_blue = int(m[j - 1])
            elif ('red' in m[j]):
                if int(m[j - 1]) > max_red:
                    max_red = int(m[j - 1])
            elif ('green' in m[j]):
                if int(m[j - 1]) > max_green:
                    max_green = int(m[j - 1])
    sum += max_blue * max_red * max_green
print(sum)
