import tkinter as tk
import sys
import os

# Add parent directory to path so we can import the loader modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from basic_01_rotating_arc import RotatingArc
from basic_02_pulsing_circle import PulsingCircle
from basic_03_bouncing_dots import BouncingDots
from basic_04_fading_circle import FadingCircle
from basic_05_radar_sweep import RadarSweep
from basic_06_wave_bars import WaveBars
from basic_07_rotating_square import RotatingSquare
from basic_08_progress_ring import ProgressRing
from basic_09_pendulum import Pendulum
from basic_10_orbit import Orbit
from basic_11_double_helix import DoubleHelix
from basic_12_heartbeat import Heartbeat
from basic_13_pacman import Pacman
from basic_14_snake_chase import SnakeChase
from basic_15_hourglass import Hourglass
from basic_16_morphing_shape import MorphingShape
from basic_17_battery import Battery
from basic_18_expanding_ring import ExpandingRing
from basic_19_dot_spinner import DotSpinner
from basic_20_infinity_loop import InfinityLoop


class BasicLoadersGallery(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("20 Basic Loading Animations (Pure Python/Tkinter)")
        self.configure(bg="#1E1E2E")
        self.geometry("1100x800")

        self.main_frame = tk.Frame(self, bg="#1E1E2E")
        self.main_frame.pack(expand=True, fill="both", padx=20, pady=20)

        loader_classes = [
            ("Rotating Arc", RotatingArc),
            ("Pulsing Circle", PulsingCircle),
            ("Bouncing Dots", BouncingDots),
            ("Fading Circle", FadingCircle),
            ("Radar Sweep", RadarSweep),
            ("Wave Bars", WaveBars),
            ("Rotating Square", RotatingSquare),
            ("Progress Ring", ProgressRing),
            ("Pendulum", Pendulum),
            ("Orbit", Orbit),
            ("Double Helix", DoubleHelix),
            ("Heartbeat", Heartbeat),
            ("Pacman", Pacman),
            ("Snake Chase", SnakeChase),
            ("Hourglass", Hourglass),
            ("Morphing Shape", MorphingShape),
            ("Battery", Battery),
            ("Expanding Ring", ExpandingRing),
            ("Dot Spinner", DotSpinner),
            ("Infinity Loop", InfinityLoop),
        ]

        for i, (name, LoaderClass) in enumerate(loader_classes):
            row = i // 5
            col = i % 5

            frame = tk.Frame(self.main_frame, bg="#2A2A3A", bd=0,
                             highlightthickness=1, highlightbackground="#3A3A4A")
            frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

            self.main_frame.grid_columnconfigure(col, weight=1)
            self.main_frame.grid_rowconfigure(row, weight=1)

            lbl = tk.Label(frame, text=name, bg="#2A2A3A", fg="#A6ACCD",
                           font=("Arial", 10, "bold"))
            lbl.pack(side="bottom", pady=5)

            loader = LoaderClass(frame, width=120, height=120)
            loader.pack(expand=True)


if __name__ == "__main__":
    app = BasicLoadersGallery()
    app.mainloop()
