def insertion_sort(arr):
    # Traverse through the entire array starting from the second element
    for i in range(1, len(arr)):
        # Store the current element to be inserted into the sorted subarray
        current_element = arr[i]
        
        # Start comparing with the elements in the sorted subarray
        j = i - 1
        
        # Move elements of the sorted subarray that are greater than the
        # current element one position ahead of their current position
        while j >= 0 and current_element < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert the current element into its correct position in the sorted subarray
        arr[j + 1] = current_element

# Example usage:
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Sorted array is:", arr)
