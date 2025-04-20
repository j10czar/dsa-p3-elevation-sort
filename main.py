from __future__ import annotations     # forward type refs
import random
import sys
from typing import Generator, List, Optional
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from bridges.data_src_dependent import data_source  # NOAA elevations
from visuals import Visuals
from sort import sort


def printHelp():
    print("\nSort‑Visualizer Help")
    print("--------------------")
    print("Run the script with one of the algorithms below:")
    print("  python main.py <algorithm>\n")
    print("Algorithms available:")
    print("  insertion  – Insertion Sort   (O(n²))")
    print("  selection  – Selection Sort   (O(n²))")
    print("  bubble     – Bubble Sort      (O(n²))")
    print("  merge      – Merge Sort       (O(n log n))")
    print("  heap       – Heap Sort        (O(n log n))")
    print("  quick      – Quick Sort       (avg O(n log n), worst O(n²))")
    print("\nExample:")
    print("  python main.py quick")
    print("\nTip: Run this script without arguments or with 'help' to see this message again.\n")



def main():
    if len(sys.argv) == 1:
        printHelp()
        exit()
    args = sys.argv[1:]  # skip script name


#pick a random latitude and longitude value to start with 
    base_lat = random.uniform(-83,83)
    base_long = random.uniform(-173,173)

#step 1 - get the data from a specific grid and flatten it into a single list
# defines the box where we are taking our coordinates 
# box size of 5.3x5.3degrees gets us around 100k data points
    bbox = [base_lat, base_long, base_lat+5.3, base_long+5.3]  
    ele_obj = data_source.get_elevation_data(bbox)

#now we need to put all of our elevation data into one list 
    elevations = []
    for row in ele_obj.data:
        for val in row:
            elevations.append(val)




# step 2 – keep only 100 bars for the graph (sample mirrors big list)
    def make_sample(arr, k: int = 100):
        idx = np.linspace(0, len(arr) - 1, k, dtype=int)  # even spread
        return idx.tolist(), [arr[i] for i in idx]        # indices + heights

    sample_idx, sample_vals = make_sample(elevations)     # 100‑bar snapshot


#step 3, initiazlie our plot and run an algorithm based on user input

    if args[0] == "help":
        printHelp()
    elif args[0] == "insertion":
        Visuals(sample_vals, sort.insertion(elevations, sample_idx, sample_vals), sample_idx).animate()


    elif args[0] == "selection":
        Visuals(sample_vals, sort.selection(elevations, sample_idx, sample_vals), sample_idx).animate()


    elif args[0] == "bubble":
        Visuals(sample_vals, sort.bubble(elevations, sample_idx, sample_vals), sample_idx).animate()

    elif args[0] == "quick":
        Visuals(sample_vals, sort.quick(elevations, sample_idx, sample_vals), sample_idx).animate()
    elif args[0] == "heap":
        Visuals(sample_vals, sort.heap(elevations, sample_idx, sample_vals), sample_idx).animate()

    elif args[0] == "merge":
        Visuals(sample_vals, sort.merge(elevations, sample_idx, sample_vals), sample_idx).animate()

    else:
        print("Please pass in a sorting algorithm! Or run the command with help to see possible algorithms.")



if __name__ == "__main__":
    main()

