import tkinter as tk
import math

class RadarSweep(tk.Canvas):
    def __init__(self, parent, width=300, height=300, **kwargs):
        super().__init__(parent, width=width, height=height, bg='#1E1E2E', highlightthickness=0, **kwargs)
        self.cx = width / 2
        self.cy = height / 2
        self.frame_count = 0
        self.animate()

    def animate(self):
        self.frame_count += 1
        self.delete("all")
        t = self.frame_count
        cx, cy = self.cx, self.cy
        r = 100
        self.create_oval(cx - r, cy - r, cx + r, cy + r, outline="#89DCEB", width=3)
        angle = (t * -5) % 360
        x = cx + r * math.cos(math.radians(angle))
        y = cy + r * math.sin(math.radians(angle))
        self.create_line(cx, cy, x, y, fill="#89DCEB", width=4)
        self.after(30, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Radar Sweep Loader")
    root.configure(bg='#1E1E2E')
    root.geometry("400x400")
    
    lbl = tk.Label(root, text="Radar Sweep Loader", bg="#1E1E2E", fg="#A6ACCD", font=("Arial", 16, "bold"))
    lbl.pack(pady=20)
    
    spinner = RadarSweep(root, width=300, height=300)
    spinner.pack(expand=True)
    root.mainloop()
