'''
Given an array of integers, return a new array such that each element 
at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output 
would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''
def solution(arr):
    result = 1
    for elem in arr:
        result = result * elem
    
    resultingArr = []
    for elem in arr:
        resultingArr.append(int(result / elem))
        
    return resultingArr
    
print(solution([1, 2, 3, 4, 5]))

'''
Explanation:

    My solution was to take the multiplication of all elements inside the array
and then divide by each element in the array. 

    This solution isn't the best posible solution since I have to iterate the array
twice before getting the final solution. Also, this solution uses division, and there's
supposed to be way to do this problem without division.
'''