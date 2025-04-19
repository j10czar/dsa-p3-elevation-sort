import heapq
from typing import Generator, List

class sort:
    # worst & average: O(n^2)
    def bubble(elevations: List[float],
                   sample_idx: List[int],
                   sample_vals: List[float]) -> Generator[int | None, None, None]:
        n = len(elevations)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if elevations[j] > elevations[j + 1]:
                    elevations[j], elevations[j + 1] = elevations[j + 1], elevations[j]
                    swapped = True
                    for k in (j, j + 1):
                        if k in sample_idx:
                            sample_vals[sample_idx.index(k)] = elevations[k]
                            yield k
            if not swapped:
                break
        yield None

    # Time Complexity: O(n log n)
    def merge(elevations: List[float],
                  sample_idx: List[int],
                  sample_vals: List[float]) -> Generator[int | None, None, None]:
        n = len(elevations)
        width = 1
        while width < n:
            for lo in range(0, n, 2 * width):
                mid = min(lo + width, n)
                hi = min(lo + 2 * width, n)
                left, right = lo, mid
                temp: List[float] = []
                while left < mid and right < hi:
                    if elevations[left] <= elevations[right]:
                        temp.append(elevations[left]); left += 1
                    else:
                        temp.append(elevations[right]); right += 1
                temp.extend(elevations[left:mid])
                temp.extend(elevations[right:hi])
                for offset, val in enumerate(temp, start=lo):
                    if elevations[offset] != val:
                        elevations[offset] = val
                        if offset in sample_idx:
                            sample_vals[sample_idx.index(offset)] = val
                            yield offset
            width *= 2
        yield None

    # Time Complexity: O(n log n)
    def heap(elevations: List[float],
             sample_idx: List[int],
             sample_vals: List[float]) -> Generator[int | None, None, None]:
        n    = len(elevations)
        heap = elevations[:]          # work on a copy so len() never changes
        heapq.heapify(heap)

        for i in range(n):
            elevations[i] = heapq.heappop(heap)        # smallest next
            if i in sample_idx:                        # keep the viz in sync
                sample_vals[sample_idx.index(i)] = elevations[i]
                yield i
        yield None

    # worst & average: O(n^2)
    def insertion(elevations: List[float],
                      sample_idx: List[int],
                      sample_vals: List[float]) -> Generator[int | None, None, None]:
        for i in range(1, len(elevations)):
            key = elevations[i]
            j = i - 1
            while j >= 0 and elevations[j] > key:
                elevations[j + 1] = elevations[j]
                if j + 1 in sample_idx:
                    sample_vals[sample_idx.index(j + 1)] = elevations[j + 1]
                    yield j + 1
                j -= 1
            elevations[j + 1] = key
            if j + 1 in sample_idx:
                sample_vals[sample_idx.index(j + 1)] = key
                yield j + 1
        yield None

    # Time Complexity: O(n^2)
    def selection(elevations: List[float],
                      sample_idx: List[int],
                      sample_vals: List[float]) -> Generator[int | None, None, None]:
        n = len(elevations)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if elevations[j] < elevations[min_idx]:
                    min_idx = j
            if min_idx != i:
                elevations[i], elevations[min_idx] = elevations[min_idx], elevations[i]
                for k in (i, min_idx):
                    if k in sample_idx:
                        sample_vals[sample_idx.index(k)] = elevations[k]
                        yield k
        yield None

    # average: O(n log n), worst: O(n^2)
    def quick(elevations: List[float],
              sample_idx: List[int],
              sample_vals: List[float]) -> Generator[int | None, None, None]:
        stack = [(0, len(elevations) - 1)]
        while stack:
            lo, hi = stack.pop()
            if lo >= hi:
                continue
            pivot = elevations[(lo + hi) // 2]
            i, j = lo, hi
            while i <= j:
                while elevations[i] < pivot:
                    i += 1
                while elevations[j] > pivot:
                    j -= 1
                if i <= j:
                    swap_i, swap_j = i, j
                    if swap_i in sample_idx or swap_j in sample_idx:
                        yield swap_i
                    elevations[i], elevations[j] = elevations[j], elevations[i]
                    if swap_i in sample_idx:
                        sample_vals[sample_idx.index(swap_i)] = elevations[swap_i]
                    if swap_j in sample_idx:
                        sample_vals[sample_idx.index(swap_j)] = elevations[swap_j]
                    i += 1
                    j -= 1
            if lo < j:
                stack.append((lo, j))
            if i < hi:
                stack.append((i, hi))
        yield None

