################################
# https://github.com/pradhansonia/03230316_BIA101_CAP3
# Sonia Pradhan
#"A" 
# 03230316
################################
# REFERENCES
#GeeksforGeeks. (2023, March 20). Calculate sum of all numbers present in a string. GeeksforGeeks.
#https://www.geeksforgeeks.org/calculate-sum-of-all-numbers-present-in-a-string/
#https://youtu.be/6jsCbjQB3y0?feature=shared
#https://youtu.be/Uh2ebFW8OYM?feature=shared
################################
# SOLUTION
# Your Solution Score: <total sum>

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def extract_two_digit_number(line):
    first_digit = None
    last_digit = None
    
    for char in line:
        if char.isdigit():
            first_digit = char
            break
    
    for char in reversed(line):
        if char.isdigit():
            last_digit = char
            break
    
    if first_digit is not None and last_digit is not None:
        return int(first_digit + last_digit)
    else:
        return 0

def print_solution(file_path):
    lines = read_input(file_path)
    total_sum = 0
    two_digit_numbers = []
    
    for line in lines:
        line = line.strip()
        two_digit_number = extract_two_digit_number(line)
        two_digit_numbers.append(two_digit_number)
        total_sum += two_digit_number
    
    for i, number in enumerate(two_digit_numbers, start=1):
        print(f"Line {i}'s number is: {number}")
    
    print(f"The total sum from the given input file {file_path} is {total_sum}")

file_path = '316 (1).txt'
print_solution(file_path)