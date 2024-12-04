import csv
import numpy as np


def import_data() -> (np.array, np.array):
    with open(r'C:\Users\robert.karsthof\PycharmProjects\AdventOfCode2024\1\input.txt', 'r') as file:
        content = file.readlines()
        data = np.array([line.split() for line in content])
        column1, column2 = data[:, 0].astype(int), data[:, 1].astype(int)
        return column1, column2


def sort_column(column: np.array):
    return np.sort(column)

col1, col2 = import_data()
sorted_col1 = sort_column(col1)
sorted_col2 = sort_column(col2)

differences = [abs(sorted_col2[index] - sorted_col1[index]) for index, row in enumerate(sorted_col1)]
sum = np.sum(differences)
# for index, row in enumerate(sorted_col1):
#     differences.append(np.abs(sorted_col2[index] - sorted_col1[index]))

print(sum)