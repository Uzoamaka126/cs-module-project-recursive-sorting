# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB) # total number of length we want to sort
    # merged_arr = [0] * elements

    # Your code here
    i = 0
    j = 0
    merged_arr = []
    if len(arrA) == 0:
        return arrB
    if len(arrB) == 0:
        return arrA
    while len(merged_arr) < elements:  # we want to stop when we have finished sorting
        if arrA[i] <= arrB[j]:
            merged_arr.append(arrA[i])
            # then move to the next element
            i = i + 1
        else:
            merged_arr.append(arrB[j])
            # then move to the next element
            j = j + 1
        # next edge case
        if i == len(arrA):
            merged_arr += arrB[j:]
            break
        if j == len(arrB):
            merged_arr += arrA[i:]
            break

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # define base case
    if len(arr) <= 1:
        return arr
    # start moving towards the base case
    # get a middle value
    middle = len(arr) // 2
    # define the left array
    left = arr[:middle]
    # define the right array
    right = arr[middle:]
    # if the length of the left array is greater than 1, keep splitting it recursively
    new_left = merge_sort(left) 
    new_right = merge_sort(right)
    # now we have individual elements in place
    
    return merge(new_left, new_right)

arr = [1, 4, 77, 45, 22, 34, 76, 20]
new_arr = merge_sort(arr)
print(new_arr)
# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

