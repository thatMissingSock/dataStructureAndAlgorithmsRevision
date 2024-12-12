def countingSort(arr):
    # Step 1: Find the range of the input
    minValue = min(arr)
    maxValue = max(arr)
    rangeSize = maxValue - minValue + 1

    # Step 2: Initialize the count array
    count = [0] * rangeSize

    # Step 3: Populate the count array
    for num in arr:
        count[num - minValue] += 1

    # Step 4: Transform the count array to cumulative counts
    for i in range(1, rangeSize):
        count[i] += count[i - 1]

    # Step 5: Build the sorted array
    output = [0] * len(arr)
    for num in reversed(arr):  # Traverse in reverse to maintain stability
        output[count[num - minValue] - 1] = num
        count[num - minValue] -= 1

    return output

# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
print(countingSort(arr))  # Output: [1, 2, 2, 3, 3, 4, 8]

tempList = [4, 2, 2, 8, 3, 3, 1, 2, 4, 5, 2, 5 , 2]
print(countingSort(tempList))
