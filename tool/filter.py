import os, sys


with open('법정동코드 전체자료.txt', 'r') as read_file:
    lines = read_file.readlines()



result = dict()
for line in lines:
    words = line.split()
    result[words[0][0:5]] = 'true'

with open('output.txt', 'w') as w_file:
    for key in result.keys():
        w_file.write(key+'\n')