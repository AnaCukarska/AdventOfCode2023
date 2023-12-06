import re
import numpy as np
f = open('day6_data.txt', 'r')
data = f.read()
data = data.split('\n')

r = re.compile("\d+")

m_time = r.findall(data[0])
m_dist = r.findall(data[1])
prod = 1
max_dist_str = ""
tot_time_str = ""
for i in range(len(m_time)):
    max_dist_str += (m_dist[i])
    tot_time_str += (m_time[i])

max_dist = int(max_dist_str)
tot_time = int(tot_time_str)
possible_dist = np.zeros([tot_time+1, 1])
for j in range(tot_time+1):
    possible_dist[j] = j * (tot_time - j)
    if (j % 1000000 == 0):
        print(str(j//1000000)+" mil")
wins = np.sum(possible_dist > max_dist)
print(wins)

# print(prod)