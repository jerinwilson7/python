number = 1 + 2 + 3

print(number)

remainder = 11 % 3

print(remainder)

e = [2,4,6,8]
o=[1,3,5,7,9]

allN = o + e
print(allN)

print([1,2]*3)


x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list  + y_list 

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")