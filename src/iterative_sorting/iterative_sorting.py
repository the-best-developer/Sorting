# TO-DO: Complete the selection_sort() function below 

test_array = [ 5, 4, 7, 1, 8, 3, 5, 2, 19, 34, 12 ]

##################################################
# 
# This was a test sorting function i made to verify my sorting function
#
##################################################

# def new_array_sort( arr ):
#     new_arr = []
#     old_arr = arr

#     for i in range(0, len(arr)):

#         # For every loop, find smallest number in array and set the index when found
#         small_index = 0
#         for k in range(0, len(arr)):
#             if old_arr[k] < old_arr[small_index]:
#                 small_index = k
#         # Add smallest number to new array

#         new_arr.append(old_arr[small_index])
#         old_arr.pop(small_index)
        
#     old_arr.extend(new_arr)
#     return old_arr

##################################################
##################################################
##################################################

def selection_sort( arr ):
    # loop through n-1 elements

    for i in range(0, len(arr)):

        # Define smallest index as i because you do not check numbers before i in the list
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        
        # loop through the array starting at i
        # find the smallest number from i to end of array
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        
        # smallest number is found at smallest_index and is swapped with number found at i
        
        # TO-DO: swap
        # Copy values to be used for swapping
        orig_value = arr[i]
        new_value = arr[smallest_index]

        # if original index is equal to smallest_index, that means our number is already in order.
        if(i != smallest_index):
            arr[i] = new_value
            arr[smallest_index] = orig_value
        print(arr)

    return arr



# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

print(test_array)
# print(new_array_sort(test_array))
selection_sort(test_array)
