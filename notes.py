# what do we need for a recursive function?
# base case 
# function that calls itself
# progress toward the base case  

# often elegant, terse, few lines of code
#Divide and conquer algorithms are recursive!
 #can divide into subproblems that have the same shape as the parent problem
 #solve subproblems
 #combine your solutions, the overall problem is solved

# example:
# if findng the most efficient route to deliver all mail at onece
#     divide into subregions
#     find most efficient rount in the subregions
#     all mail delivered 


# in sorting
#     break up the array
#     sort each peice
#     put them back together


# quicksort example:
# chose your pivot: median or first or last number in the array. 
# arr = [5, 4,6,8,9,1,2]

#base case: empty array
# choose pivot
def partition(arr):
    pivot = arr[0]
    left = []
    right = []
    


# partitiion around the pivot
    for num in arr:
        if num < pivot:
            left.append(num)
        if num > pivot:
            right.append(num)
    return left, pivot, right



#quicksort
def quicksort(arr):
    ## Base case: empty array
    if len(arr) == 0:
        return arr
## recurse on left and right sides
        # tuple unpacking
    left, pivot, right = partition(arr)
    return quicksort(left) + [pivot] + quicksort(right)
print(quicksort([1, 3, 11, 4, 6, 5, 9]))