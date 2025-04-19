from typing import Generator, List, Optional
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

class Visuals:
    #all of this setup was taken from matplotlib docs
    def __init__(self,
                 heights: List[float],           # bar heights (sample)
                 idx_gen: Generator[int | None, None, None],
                 interval: float = 0.01): #this gives the animation some time to catch up lol
        self.h = heights
        self.idx_gen = idx_gen
        self.interval = interval

        # axes setup
        self.fig, self.ax = plt.subplots(figsize=(9, 4))
        self.bars = self.ax.bar(range(len(heights)), heights, align="edge")
        self.ax.set_xlim(0, len(heights))
        self.ax.set_ylim(min(heights), max(heights))
        self.ax.set_xticks([]); self.ax.set_ylabel("elevation (m)")
        self.msg = self.ax.text(0.02, 0.95, "", transform=self.ax.transAxes)
        self.last: Optional[int] = None          
        self.ani = None                          



