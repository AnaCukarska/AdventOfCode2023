import re
import numpy as np
f = open('day6_data.txt', 'r')
data = f.read()
data = data.split('\n')

r = re.compile("\d+")

m_time = r.findall(data[0])
m_dist = r.findall(data[1])
prod = 1
for i in range(len(m_time)):
    max_dist = int(m_dist[i])
    tot_time = int(m_time[i])
    possible_dist = np.zeros([tot_time+1, 1])
    for j in range(tot_time+1):
        possible_dist[j] = j * (tot_time - j)
    wins = np.sum(possible_dist > max_dist)
    # print(wins)
    prod *=wins

print(prod)