def bubbleSort(arr):
    while True:
        corrected = False
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                corrected = True
        if not corrected:
            return arr

print(bubbleSort([14,46,43,27,57,41,45,21,70]))
