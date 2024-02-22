#Missing Number
# Write a function to find the missing number in a given integer array of 1 to 100. The function takes to parameter the array and the number of elements that needs to be in array.  
#For example if we want to find missing number from 1 to 6 the second parameter will be 6.

def missing_number(arr,n):
    full_array = [i for i in range(1, n+1)]
    for element in full_array:
        if element not in arr:
            return element
        
print(missing_number([1, 2, 3, 4, 6], 6))


#solutie aritmetica (mai eficienta):

# def missing_number(arr, n):
#     # Calculate the sum of first n natural numbers
#     total = n * (n + 1) // 2
    
#     # Calculate the sum of numbers in the array
#     sum_arr = sum(arr)
    
#     # Find the missing number by subtracting sum_arr from total
#     missing = total - sum_arr
    
#     return missing
 
# # Example
# print(missing_number([1, 2, 3, 4, 6], 6))  # Output: 5