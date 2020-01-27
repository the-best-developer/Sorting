# TO-DO: Complete the selection_sort() function below 

test_array = [ 4, 2, 3, 1, 9, 8, 7, 6, 5 ]

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

    for i in range(0, len(arr) - 1):

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

def insertion_sort( arr ):

    # Loop through array
    for i in range(1, len(arr)):
        
        # loop through index 0 to i
        for j in range(0, i):

            # we assume our numbers are in order from 0 to i
            # we can then assume the first number that is larger then what is selected is where we should insert our number
            if arr[j] > arr[i]:
                value = arr.pop(i)
                arr.insert(j, value)
                print(f"put: {value} at: {j}")
                print(arr)
                break

    return arr



# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

print(test_array)
# print(new_array_sort(test_array))
print(insertion_sort(test_array))
