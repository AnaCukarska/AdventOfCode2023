import re

f = open('day4_data.txt', 'r')
data = f.read()
data = data.split('\n')
def process_card(i, total):
    line = data[i]
    r = re.compile("\d+")
    m = r.findall(line)
    m = m[1:]
    winning_nums = m[0:10]
    my_nums = m[10:]
    nums_of_interest = sum(my_nums[j] in winning_nums for j in range(len(my_nums)))
    # print(nums_of_interest)
    for j in range(i+1, i+1+nums_of_interest):
        total = process_card(j, total)
    # print(total)
    return total + 1


total = 0
for k in range(len(data)):
    total = process_card(k, total)
    print(str(k) + " " + str(total))
print(total)

