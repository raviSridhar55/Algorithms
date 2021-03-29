# Linear Search Algorithm

# Variable declared to return the position of the integer searched for
# if pos = -1 used then it will start from 0 index,
# the pos is to specify index and we know start of elements is from index 0 thats the reason
# we take one lesser value -1
pos = -1

# Search function which searches the list in linear manner
# it searches the list from index 0 till it find the integer searched for

# def search(list, n):
#     i = 0
#     while i< len(list):
#         if list[i] == n:
#             globals() ['pos']= i
#             return True
#         i = i+1
#     return False

def search(list, n):
    for i in range(len(list)):
        if list[i] == n:
            globals() ['pos']= i
            return True

    return False

# Given List
# list = input(list[5])
list = [5,9,8,7,3,4]
# element to search for
# n = input(int)
n = 3

# To print the output
if search(list, n):
    print('Found at ',pos)
else:
    print('Not Found')

