from typing import Generator, List, Optional
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import time
import requests

class Visuals:
    """
    - heights: list of floats showing the elevation values (we're only visualizing a sample of them)
    - index_gen: generator that gives us the next index being visited by the sort algorithm
    - sample_index: the original indices of the sampled values (used to match them with full dataset changes)
    - interval: time between animation fames    """
    
    def __init__(self,
                 heights: List[float],
                 index_gen: Generator[int | None, None, None],
                 sample_index: List[int],
                 elevations: List[float],
                 coord_lookup: dict[float, tuple[float, float]],
                 interval: float = 0.01):
        self.h = heights                            # Bar heights for the sample
        self.index_gen = index_gen                  # Which index is being touched next by the sort
        self.sample_index = sample_index            # Keeps track of where the sample came from in the big list
        self.interval = interval                    # Speed of the animation
        self.elevations = elevations
        self.coord_lookup = coord_lookup

        # Set up the chart
        self.fig, self.ax = plt.subplots(figsize=(9, 4))
        self.fig.canvas.manager.set_window_title("P3 - Elevation Sorting - Jason Tenczar")
        self.bars = self.ax.bar(range(len(heights)), heights, align="edge")
        self.ax.set_xlim(0, len(heights))
        self.ax.set_ylim(min(heights), max(heights))
        self.ax.set_xticks([])                      # no x-axis numbers
        self.ax.set_ylabel("elevation (m)")
        self.msg = self.ax.text(0.02, 0.95, "", transform=self.ax.transAxes)  # text box in the corner

        self.last: Optional[int] = None             # bar we highlighted in the last frame
        self.ani = None                             # the animation object itself
        self.start = 0.00
        self.end = 0.00

    def getLocationName(self, latitude: float, longitude: float):
        url = "https://nominatim.openstreetmap.org/reverse"
        params = {
            "lat": latitude,
            "lon": longitude,
            "format": "json",
            "zoom": 10, 
            "addressdetails": 1
        }

        headers = {
            "User-Agent": "P3-Elevation-Sorter/1.0 (jasontenczar@ufl.edu)"
        }

        try:
            response = requests.get(url, params=params, headers=headers)
            data = response.json()
            return data["display_name"]
        except Exception as e:
            return "Rural or Ocean Area"


    def _update(self, curr: int | None):
        """
        Updates the bar colors and heights on each frame.
        Highlights the bar we're currently working with.
        """
        # un-highlight the last bar
        if self.last is not None:
            self.bars[self.last].set_color("steelblue")

        # if there's a valid index being worked on and it’s in our sample
        if curr is not None and curr in self.sample_index:
            pos = self.sample_index.index(curr)        # find position of this bar in the sample
            self.bars[pos].set_height(self.h[pos])     # update height if it changed
            self.bars[pos].set_color("red")            # highlight it
            self.msg.set_text(f"visiting {curr}")      # update message
            self.last = pos
        elif curr is None:
            self.end = time.time()
            highest = self.elevations[-1]
            latitude, longitude = self.coord_lookup[highest] #allows for lat and lon lookup in O(1) time
            location_name = self.getLocationName(latitude, longitude) 
            time_msg = "Done in "+str(round(self.end-self.start,2))+"s" 
            location_msg = f" / Highest Elevation: {round(highest, 2)}m at {location_name}"
            self.msg.set_text(time_msg + location_msg)                  # sorting is done!

        return (*self.bars, self.msg)  # return everything matplotlib needs to re-draw

    def animate(self):
        """
        Starts the animation by connecting the update function with the generator.
        """
        self.start = time.time()

        self.ani = animation.FuncAnimation(
            self.fig,
            self._update,
            frames=self.index_gen,
            interval=self.interval,
            blit=True,
            repeat=False,
            cache_frame_data=False,
        )
        plt.tight_layout()
        plt.show()

