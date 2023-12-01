import numpy as np
import sys

f = open('day1_data.txt', 'r')
data = f.read()
data = data.split('\n')

sum = 0

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
           'nine']
for line in data:
    min_idx = -1
    options_idx = [-1] * 18
    options_lidx = [-1] * 18
    for i, option in enumerate(options):
        options_idx[i] = line.find(option)
        options_lidx[i] = line.rfind(option)

    options_idx_pos = options_idx
    for j in range(len(options_idx)):
        if options_idx[j] < 0:
            options_idx_pos[j] = sys.maxsize

    first_dig = options[np.argmin(options_idx_pos)]
    last_dig = options[np.argmax(options_lidx)]
    if first_dig == '1' or first_dig == 'one':
        sum += 10 * 1
    elif first_dig == '2' or first_dig == 'two':
        sum += 10 * 2
    elif first_dig == '3' or first_dig == 'three':
        sum += 10 * 3
    elif first_dig == '4' or first_dig == 'four':
        sum += 10 * 4
    elif first_dig == '5' or first_dig == 'five':
        sum += 10 * 5
    elif first_dig == '6' or first_dig == 'six':
        sum += 10 * 6
    elif first_dig == '7' or first_dig == 'seven':
        sum += 10 * 7
    elif first_dig == '8' or first_dig == 'eight':
        sum += 10 * 8
    elif first_dig == '9' or first_dig == 'nine':
        sum += 10 * 9

    if last_dig == '1' or last_dig == 'one':
        sum += 1
    elif last_dig == '2' or last_dig == 'two':
        sum += 2
    elif last_dig == '3' or last_dig == 'three':
        sum += 3
    elif last_dig == '4' or last_dig == 'four':
        sum += 4
    elif last_dig == '5' or last_dig == 'five':
        sum += 5
    elif last_dig == '6' or last_dig == 'six':
        sum += 6
    elif last_dig == '7' or last_dig == 'seven':
        sum += 7
    elif last_dig == '8' or last_dig == 'eight':
        sum += 8
    elif last_dig == '9' or last_dig == 'nine':
        sum += 9

print(sum)
