#first we get users input
num = int(input("enter an integer:"))
shift = int(input("enter number of shift positions:"))
print(f"\nOrigional number:{num}")
print(f"binary form: {bin(num)}")
#right shift
right_shifted = num >> shift
print(f"\nAfter right shift by {shift}:{right_shifted}")
print(f"binary form:{bin(right_shifted)}")
#left shift
left_shifted = num << shift
print(f"\nAfter left shift by{shift}:{left_shifted}")
print(f"binary form:{bin(left_shifted)}")