# Binary Search algorithm


pos = -1

def search(list, n):
    # Lower Bound
    l = 0
    # Upper Bound
    u = len(list)
    # when lower bound is less than the upper bound then only search is performed
    while l <= u:
        # we have to find the mid value to compare with the integer we have to find
        mid = (u + l) // 2
        # when mid value is equal to the value searched for
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            # when mid value is less then the the value searched for the we change the mid value
            # to lower bound and add 1 to mid since we dont need the prev mid value
            if list[mid] < n:
                l = mid + 1
            # when mid is greater than the searched value then we change the mid value to upper bound
            # and remove 1 from the mid to skip that value
            else:
                u = mid - 1
    return False

list = [6,9,56,78,687,732,769,800,100000]

n = 732



if search(list, n):
    print('Found at ',pos + 1)
else:
    print('Not Found')