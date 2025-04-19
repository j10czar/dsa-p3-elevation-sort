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

    # called each frame
    def _update(self, curr: int | None):
        if self.last is not None:                # un‑highlight old one
            self.bars[self.last].set_color("steelblue")

        if curr is not None and curr in sample_idx:
            pos = sample_idx.index(curr)         # bar slot (0‑99)
            self.bars[pos].set_height(self.h[pos])
            self.bars[pos].set_color("red")
            self.msg.set_text(f"visiting {curr}")
            self.last = pos
        elif curr is None:
            self.msg.set_text("done")

        return (*self.bars, self.msg)            # blit targets

    # launch animation
    def animate(self):
        #create the animation object per the matplot lib docs
        self.ani = animation.FuncAnimation(
            self.fig,
            self._update,
            frames=self.idx_gen,
            interval=self.interval,
            blit=True,
            repeat=False,
            cache_frame_data=False,
        )
        plt.tight_layout(); plt.show()

