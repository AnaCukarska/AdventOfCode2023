
import re
import numpy as np

f = open('Untitled2.txt', 'r')
data = f.read()
data = data.split('\n')

print(data[0])
total = 0
for i in range(len(data)):
    product = 0
    line = data[i]
    r = re.compile("\d+")
    m = r.findall(line)
    m = m[1:]
    winning_nums = m[0:10]
    my_nums = m[10:]
    nums_of_interest = sum(my_nums[j] in winning_nums for j in range(len(my_nums)))
    total += (2**(nums_of_interest-1)) * (nums_of_interest!=0)
print(total)

