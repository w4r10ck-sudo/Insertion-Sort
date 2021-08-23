# insertion sort
arr = input().split()
arr = [int(i) for i in arr]  # converting list of string type numbers to int
for i in range(1, len(arr)):  # loop through array from 1 to n
    j = i  # set j = i as a key or pointer
    while arr[j] < arr[j - 1] and j != 0:  # looping while the number on index j is sorted
        temp = arr[j - 1]
        arr[j - 1] = arr[j]
        arr[j] = temp
        j -= 1  # decrementing j to get the index of number being sorted
print(arr)

