# Script is intended to read a file with decimal numbers (one number per line) and add them
# Example use case: large file full of prices, add them up to see total_sum
file_name = input("Enter Name of File: ")
file_name += ".txt"
total_sum = 0

with open(file_name) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        line.strip()
        total_sum += float(line)
        line = fp.readline()
        cnt += 1
print(total_sum)