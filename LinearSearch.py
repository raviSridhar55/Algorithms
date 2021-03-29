# Linear Search Algorithm

# Variable declared to return the position of the integer searched for
pos = -1

# Search function which searches the list in linear manner
# it searches the list from index 0 till it find the integer searched for

def search(list, n):
    i = 0
    while i< len(list):
        if list[i] == n:
            globals() ['pos']= i
            return True
        i = i+1
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

