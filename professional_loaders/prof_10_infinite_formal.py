import tkinter as tk
import math

class InfiniteFormal(tk.Canvas):
    def __init__(self, parent, width=300, height=300, **kwargs):
        super().__init__(parent, width=width, height=height, bg='white', highlightthickness=0, **kwargs)
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
        for i in range(30):
            a = math.radians(i * 12 + t * 5)
            x = cx + 70 * math.sin(a)
            y = cy + 30 * math.sin(2 * a)
            pts.extend([x, y])
        self.create_line(pts, fill="#263238", width=3, smooth=True)

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Formal Infinity Trace")
    root.configure(bg='white')
    
    spinner = InfiniteFormal(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
