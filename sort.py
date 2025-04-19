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
    def quick(elevations, sample_idx, sample_vals) -> Generator[int | None, None, None]:
        stack = [(0, len(elevations) - 1)]                # manual recursion bc too lazy to write a helper
        while stack:
            lo, hi = stack.pop()
            if lo >= hi: continue
            pivot = elevations[(lo + hi) // 2]
            i, j = lo, hi
            while i <= j:
                while elevations[i] < pivot: i += 1
                while elevations[j] > pivot: j -= 1
                if i <= j:
                    swap_i, swap_j = i, j
                    if swap_i in sample_idx or swap_j in sample_idx:
                        yield swap_i                     # tell UI to refresh
                    elevations[i], elevations[j] = elevations[j], elevations[i]
                    if swap_i in sample_idx:
                        sample_vals[sample_idx.index(swap_i)] = elevations[swap_i]
                    if swap_j in sample_idx:
                        sample_vals[sample_idx.index(swap_j)] = elevations[swap_j]
                    i += 1; j -= 1
            if lo < j: stack.append((lo, j))
            if i < hi: stack.append((i, hi))
        yield None

