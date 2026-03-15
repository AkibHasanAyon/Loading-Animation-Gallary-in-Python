import tkinter as tk
import math

class PlasmaRing(tk.Canvas):
    def __init__(self, parent, width=300, height=300, **kwargs):
        super().__init__(parent, width=width, height=height, bg='#0F172A', highlightthickness=0, **kwargs)
        self.cx = width / 2
        self.cy = height / 2
        self.frame_count = 0

        self.animate()
        
    def animate(self):
        self.frame_count += 1
        self.delete("all")
        t = self.frame_count
        cx, cy = self.cx, self.cy
        pts = []
        for i in range(72):
            a = math.radians(i * 5)
            r = 70 + 15 * math.sin(a * 6 + t * 0.2)
            pts.extend([cx + r * math.cos(a), cy + r * math.sin(a)])
        self.create_line(pts, fill="#EC4899", width=6, smooth=True)

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Premium Plasma Ring")
    root.configure(bg='#0F172A')
    
    spinner = PlasmaRing(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
