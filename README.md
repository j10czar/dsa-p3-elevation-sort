# Elevation Data Sorting Visualizer

Live Demo Video: https://www.youtube.com/watch?v=Vpd3DNyJ0XE

<img width="1455" alt="image" src="https://github.com/user-attachments/assets/f888c277-d138-4514-aa47-4c7ac5eac2f3" />


A Python-based project that demonstrates how common sorting algorithms work — using real elevation data from NOAA’s global elevation dataset. This project visualizes the step-by-step sorting of elevation values sampled from randomly selected geographic coordinates, making it easier to understand how each algorithm functions.

---

##  Problem

Sorting algorithms can be hard to understand in the abstract. Raw elevation data is also tough to interpret on its own. This project addresses both problems by combining them: visualizing sorting algorithms using real-world elevation data.

---

##  Motivation

- Help students better understand how sorting algorithms behave over time.
- Make sense of NOAA elevation data through color-coded visualizations.
- Provide interactive exploration of different sorting strategies.

---

##  Features

- Retrieves elevation data for a random 5.3° x 5.3° bounding box using the [BRIDGES elevation dataset](https://bridgesuncc.github.io/tutorials/Data_Elevation.html).
- Visualizes a sample of the elevation data as a bar graph using `matplotlib`.
- Animates the sorting process using various algorithms:
  - Bubble Sort
  - Insertion Sort
  - Selection Sort
  - Merge Sort
  - Heap Sort
  - Quick Sort
- Displays the time taken to sort and the real-world location of the highest elevation point in the dataset using reverse geocoding.
- Allows selection of sorting algorithm from the command line.

---

##  How It Works

1. **Data Collection**: Random geographic coordinates are generated and used to pull elevation data from NOAA via the BRIDGES API.
2. **Flattening**: The elevation grid is flattened into a list for sorting.
3. **Visualization**: A `matplotlib` animation shows the sorting progress on a sample of the data.
4. **Reverse Lookup**: The highest elevation is reverse-geocoded to find its real-world location.

---

##  Tools & Libraries

- Python 3.11+
- [`matplotlib`](https://matplotlib.org/) – for animation/visualization
- [`numpy`](https://numpy.org/) – for efficient array manipulation
- [`requests`](https://docs.python-requests.org/) – for reverse geocoding lookups
- [`bridges`](https://bridgesuncc.github.io/) – for accessing NOAA elevation data

---

##  Setup Instructions

1. Clone the repository:

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the visualizer:
   ```bash
   python main.py quick     # options: quick, heap, merge, bubble, insertion, selection
   ```


