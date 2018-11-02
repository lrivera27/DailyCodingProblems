'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''
def checkList(arr, k):
    for elem in arr:
        if(abs(elem - k) in arr):
            if((elem + abs(elem - k)) == k):
                return True
    return False
print(checkList([13, 12, 25, 5, 8], 13))

'''
Explanation:

    My solution was to first take each element of the array and subtracting the value of k to it,
if the resulting value was in the original list, I then added this new value to the element of the
array, if this addition was equal to the value of k, then it meant that the solution was True.

    Of course this only works if the given list is all positive numbers since I am using an absolute
function to calculate the subtraction.
'''