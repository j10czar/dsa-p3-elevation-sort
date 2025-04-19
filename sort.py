import heapq

class sort:

    #   worst & average: O(n^2)
    def bubbleSort(elevations):
        n = len(elevations)
        for i in range(n):
            swapped = False
            # compare each pair of neighbors; move the larger one right
            for j in range(0, n - i - 1):
                if elevations[j] > elevations[j + 1]:
                    temp = elevations[j]
                    elevations[j] = elevations[j + 1]
                    elevations[j + 1] = temp
                    swapped = True
            # stop early if a complete pass made no swaps
            if not swapped:
                break
        return elevations


    # Time Complexity: O(n log n) in all cases
    def mergeSort(elevations):
        if len(elevations) <= 1:
            return elevations

        mid = len(elevations) // 2
        left = sort.mergeSort(elevations[:mid])
        right = sort.mergeSort(elevations[mid:])

        # merge the two sorted halves
        i = 0
        j = 0
        merged = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        while i < len(left):
            merged.append(left[i])
            i += 1

        while j < len(right):
            merged.append(right[j])
            j += 1

        # write merged values back into the original list
        for k in range(len(merged)):
            elevations[k] = merged[k]

        return elevations

 
    # Time Complexity: O(n log n)
    def heapSort(elevations):
        heapq.heapify(elevations)
        sorted_out = []
        for i in range(len(elevations)):
            smallest = heapq.heappop(elevations)
            sorted_out.append(smallest)
        for j in range(len(sorted_out)):
            elevations[j] = sorted_out[j]
        return elevations

  
    #   worst & average: O(n^2)
   
    def insertionSort(elevations):
        # traverse each element; treat left portion as a growing sorted list
        for i in range(len(elevations)):
            key = elevations[i]
            j = i - 1
            # shift larger elements one position to the right
            while j >= 0 and elevations[j] > key:
                elevations[j + 1] = elevations[j]
                j -= 1
            # insert the key into its proper location
            elevations[j + 1] = key
        return elevations


    # Time Complexity: O(n^2)
    def selectionSort(elevations):
        n = len(elevations)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if elevations[j] < elevations[min_idx]:
                    min_idx = j
            temp = elevations[i]
            elevations[i] = elevations[min_idx]
            elevations[min_idx] = temp
        return elevations


    #   average: O(n log n)
    #   worst:   O(n^2)
    def quickSort(elevations):
        def _quick(arr):
            if len(arr) <= 1:
                return arr

            pivot_index = len(arr) // 2
            pivot = arr[pivot_index]

            left = []
            mid = []
            right = []

            for x in arr:
                if x < pivot:
                    left.append(x)
                elif x == pivot:
                    mid.append(x)
                else:
                    right.append(x)

            sorted_left = _quick(left)
            sorted_right = _quick(right)

            result = []
            for item in sorted_left:
                result.append(item)
            for item in mid:
                result.append(item)
            for item in sorted_right:
                result.append(item)

            return result

        elevations[:] = _quick(elevations)
        return elevations

