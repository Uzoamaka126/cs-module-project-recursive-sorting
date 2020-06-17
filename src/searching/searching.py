# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # start at the beginning of the array
    start = 0
    # get the end of the array which is the length of the array minus 1
    end = len(arr) - 1
    # write our base case
    if arr(len) < 1:
        return
    # have our code get us closer to the base case
    # if low < high:
        middle = (end - start) // 2
        guess = arr[middle]
        if guess == target:
            print(middle, target)
            return "target has been found"
        elif target < guess:
            high = middle - 1
            return binary_search(arr, target, start, high)
        elif target > guess:
            low = middle + 1
            return binary_search(arr, target, low, high)
        
        print("Number not done")
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here

