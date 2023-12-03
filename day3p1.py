import re
import numpy as np

f = open('day3_data.txt', 'r')
data = f.read()
data = data.split('\n')
import copy

data_copy = copy.deepcopy(data)
for i in range(len(data)):
    data[i] = [x for x in data[i]]
# strategy:
# find (i,j) indices for every symbol (define symbol as everything which is not ".", or a digit)
# find (k,l) indices for every number (collection of digits) - use regex?
# for each number check if there is a symbol around -> it if yes add to sum


# find (i,j) indices for every symbol (define symbol as everything which is not ".", or a digit)
symbol_map = np.zeros((len(data) + 4, len(data[0]) + 4))
gear_map = np.zeros((len(data) + 4, len(data[0]) + 4))
num_map = np.zeros((len(data) + 4, len(data[0]) + 4))
for i in range(len(data)):
    for j in range(len(data[0])):
        symbol_map[i + 1, j + 1] = 1 * (not (data[i][j] == '.' or data[i][j].isdigit()))
        gear_map[i + 1, j + 1] = 1 * (data[i][j] == '*')
        # num_map[i+1] = 1*data[i][j].isdigit()
sum1 = 0
sum2 = 0
gear_map_new = copy.deepcopy(gear_map)
for i in range(len(data_copy)):
    no_numbers = False
    while (not no_numbers):
        r = re.compile("\d+")
        m = r.search(data_copy[i])
        if m is None:
            no_numbers = True
            continue
        start_idx = m.regs[0][0]
        end_idx = m.regs[0][1]
        if np.sum(symbol_map[i][(start_idx + 1):(end_idx + 1)]) > 0 or np.sum(symbol_map[i + 2][(start_idx + 1):(end_idx + 1)]) > 0 or np.sum(symbol_map[i:i + 3, start_idx]) > 0 or np.sum(symbol_map[i:i + 3, end_idx + 1]) > 0:
            sum1 += int(data_copy[i][start_idx:end_idx])
        if np.sum(gear_map[i][(start_idx + 1):(end_idx + 1)]) > 0 or np.sum(gear_map[i + 2][(start_idx + 1):(end_idx + 1)]) > 0 or np.sum(gear_map[i:i + 3, start_idx]) > 0 or np.sum(gear_map[i:i + 3, end_idx + 1]) > 0:
            gear_map[i][(start_idx + 1):(end_idx + 1)] *= int(data_copy[i][start_idx:end_idx])
            gear_map[i + 2][(start_idx + 1):(end_idx + 1)] *= int(data_copy[i][start_idx:end_idx])
            gear_map[i:i + 3, start_idx] *= int(data_copy[i][start_idx:end_idx])
            gear_map[i:i + 3, end_idx + 1] *= int(data_copy[i][start_idx:end_idx])
            gear_map_new[i][(start_idx + 1):(end_idx + 1)] *= 2
            gear_map_new[i + 2][(start_idx + 1):(end_idx + 1)] *= 2
            gear_map_new[i:i + 3, start_idx] *= 2
            gear_map_new[i:i + 3, end_idx + 1] *= 2
        data_copy[i] = str(data_copy[i][:start_idx] + '.' * (end_idx - start_idx) + data_copy[i][end_idx:])
    hahah = 0
print(sum1)
gear_map_final = np.where(gear_map_new==4, gear_map, 0)
print(np.sum(gear_map_final))
print(sum2)
# print(considered_numbers)
            # for i in range(len(data)):
            #     for j in range(len(data[0])):
            #         if data[i][j].isdigit():
            # check
