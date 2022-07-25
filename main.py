with open("file1_data.txt") as file1:
    file1_data = file1.readlines()

with open("file2_data.txt") as file2:
    file2_data = file2.readlines()

result = [int(num) for num in file2_data if num in file1_data];

print(result)