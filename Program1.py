# The range of a set of values is the maximum value minus the minimum
# value. Define a procedure, set_range, which returns the range of three input
# values.

# Hint: the procedure, biggest which you coded in this unit
# might help you with this question. You might also like to find a way to
# code it using some built-in functions.
from Tools.scripts.treesync import raw_input


def set_range(l):
    a = min(l)
    b = max(l)
    return b-a


num_array = list()
num = raw_input("Enter how many elements you want:")
print ('Enter numbers in array: ')
for i in range(int(num)):
    n = raw_input("num :")
    num_array.append(int(n))

print (set_range(num_array))


