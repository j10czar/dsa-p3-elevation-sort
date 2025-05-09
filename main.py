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

#this will generate an OSM link so users can see what box they are sorting from 
    center_lat = base_lat + 5.3 / 2
    center_long = base_long + 5.3 / 2
    zoom = 7 #around a 5.3x5.3 grid

    osm_url = f"https://www.openstreetmap.org/#map={zoom}/{center_lat:.4f}/{center_long:.4f}"
    print("View bounding box on map:", osm_url)


    #i also want to put each elevation in a map with the elevation as the key and the latitude and longidude as the value
    #this will help later when we find the location with the highest altidude in O(1) time

    lat_len = len(ele_obj.data)
    lon_len = len(ele_obj.data[0])

    print("Dataset size: ", lat_len*lon_len)

    lat_step = 5.3/lat_len #how much we are moving the latitude or longitude by when we move in each direction of the matrix
    lon_step = 5.3/lon_len

    #will be used later to find the location with the highest elevation
    coord_lookup = {}
    
    #latidue is row, longitude are columns
    #runs in O(n) to flatten our data and put it in a map for later
    #now we need to put all of our elevation data into one list 

    elevations = []
    for i in range(lat_len):
        for j in range(lon_len):
            elevation = ele_obj.data[i][j]
            elevations.append(elevation)
            latitude = base_lat + lat_step*i
            longitude = base_long + lon_step*j
            coord_lookup[elevation] = (latitude,longitude)






# step 2 – keep only 100 bars for the graph (sample mirrors big list)
    def make_sample(arr, k: int = 100):
        idx = np.linspace(0, len(arr) - 1, k, dtype=int)  # even spread
        return idx.tolist(), [arr[i] for i in idx]        # indices + heights

    sample_idx, sample_vals = make_sample(elevations)     # 100‑bar snapshot


#step 3, initiazlie our plot and run an algorithm based on user input

    if args[0] == "help":
        printHelp()
    elif args[0] == "insertion":
        Visuals(sample_vals, sort.insertion(elevations, sample_idx, sample_vals), sample_idx, elevations, coord_lookup).animate()


    elif args[0] == "selection":
        Visuals(sample_vals, sort.selection(elevations, sample_idx, sample_vals), sample_idx, elevations, coord_lookup).animate()


    elif args[0] == "bubble":
        Visuals(sample_vals, sort.bubble(elevations, sample_idx, sample_vals), sample_idx, elevations, coord_lookup).animate()

    elif args[0] == "quick":
        Visuals(sample_vals, sort.quick(elevations, sample_idx, sample_vals), sample_idx, elevations, coord_lookup).animate()
    elif args[0] == "heap":
        Visuals(sample_vals, sort.heap(elevations, sample_idx, sample_vals), sample_idx, elevations, coord_lookup).animate()

    elif args[0] == "merge":
        Visuals(sample_vals, sort.merge(elevations, sample_idx, sample_vals), sample_idx, elevations, coord_lookup).animate()

  


if __name__ == "__main__":
    main()

