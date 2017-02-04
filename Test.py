import os

data_dir = os.path.join(os.path.dirname(__file__), 'data')
print(data_dir)
filename1 = os.path.join(data_dir, '1984-chp01.txt')
print(filename1)

with open(filename1, 'r') as myfile:
    data1 = myfile.read().replace('\n', '')

print(data1)