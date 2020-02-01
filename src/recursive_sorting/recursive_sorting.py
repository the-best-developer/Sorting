test_array1 = [ 11, 18 ]
test_array2 = [ 12, 13 ]
test_array3 = [ 2, 1, 5, 12, 9, 11, 14, 3 ]

# TO-DO: complete the helpe function below to merge 2 sorted arrays

def merge(arr, arrA, arrB ):
    
    # Integers used for keeping track of A and B indexes, as well as the original array
    a_i = 0
    b_i = 0
    c_i = 0

    # Check if a_i and b_i are valid indexes
    while a_i < len(arrA) and b_i < len(arrB):
        # If A item is smaller than B item, add A first
        if arrA[a_i] <= arrB[b_i]:
            arr[c_i] = arrA[a_i]
            a_i += 1
            c_i += 1

        # If A item is bigger than B item, add B first
        elif arrA[a_i] >= arrB[b_i]:
            arr[c_i] = arrB[b_i]
            b_i += 1
            c_i += 1

    # If only a_i is a valid index, add item to end of list
    while a_i < len(arrA):
        arr[c_i] = arrA[a_i]
        a_i += 1
        c_i += 1

    # If only b_i is a valid index, add item to end of list
    while b_i < len(arrB):
        arr[c_i] = arrB[b_i]
        b_i += 1
        c_i += 1


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort_rec( arr ):
    # TO-DO

    # Base case: if no more items in array, start merging
    if len(arr) < 2:
        return arr
    
    # Split array
    hlf = int(len(arr) / 2)
    arr1 = arr[hlf:]
    arr2 = arr[:hlf]
    
    # Recurse splitting
    merge_sort_rec(arr1)
    merge_sort_rec(arr2)

    # After splitting is done, merge arrays
    # Since the arrays are now in order, we can run a more efficient sorting function
    return merge(arr, arr1, arr2)


def merge_sort( arr ):

    # Make new array to work with
    new_arr = []
    # Add arr values to new_arr
    new_arr.extend(arr)

    # Pass new_arr to merge_sort function to be sorted
    merge_sort_rec(new_arr)
    
    # Return sorted array
    return new_arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr