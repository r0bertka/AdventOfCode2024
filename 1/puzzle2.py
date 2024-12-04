import csv
import numpy as np


def import_data() -> (np.array, np.array):
    with open(r'C:\Users\robert.karsthof\PycharmProjects\AdventOfCode2024\1\input.txt', 'r') as file:
        content = file.readlines()
        data = np.array([line.split() for line in content])
        column1, column2 = data[:, 0].astype(int), data[:, 1].astype(int)
        return column1, column2

col1, col2 = import_data()
score = 0

for line1 in col1:
    mult = 0
    for line2 in col2:
        if line1 == line2:
            mult += 1
    score += line1 * mult

print(score)