class sort:
    def bubbleSort(elevations):

    def mergeSort(elevations):

    def heapSort(elevations):

    #O(n^2)
    def insertionSort(elevations):

        for i in range(len(elevations)):
            item = elevations[i]             
            j = i - 1

        # shift elements of arr that are greater than key, to one position ahead
        while j >= 0 and elevations[j] > item:
            elevations[j + 1] = elevations[j]
            j -= 1

        arr[j + 1] = item  # insert the key at the correct position

        return elevations

    def selectionSort(elevations):

    def quickSort(elevations):

