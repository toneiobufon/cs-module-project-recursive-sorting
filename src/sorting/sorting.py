# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    x = 0
    y = 0

   # to loop the merged array
    for i in range(len(merged_arr)):
    
        if x >= len(arrA):
            merged_arr[i] = arrB[y]
            y += 1
        elif y >= len(arrB):
            merged_arr[i] = arrA[x]
            x += 1
        elif arrA[x] < arrB[y]:
            merged_arr[i] = arrA[x]
            x += 1
        else:
            merged_arr[i] = arrB[y]
            y += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
    else: 
        mid = len(arr)//2
        #recurse on left and right
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        #then put back together
        arr = merge(left, right)


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    pass
    # Your code here

