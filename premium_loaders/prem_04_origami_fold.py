import tkinter as tk
import math

class OrigamiFold(tk.Canvas):
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
        angle = math.radians(t * 3)
        pts = []
        for i in range(3):
            a = angle + i * (math.pi * 2 / 3)
            # Scaling logic to mimic folding
            scale = 0.5 + 0.5 * math.sin(t * 0.1)
            pts.extend([cx + 60 * scale * math.cos(a), cy + 60 * scale * math.sin(a)])
        self.create_polygon(pts, fill="#FACC15", outline="#EAB308", width=2)
        # Reflected triangle
        pts2 = []
        for i in range(3):
            a = -angle + i * (math.pi * 2 / 3)
            pts2.extend([cx + 40 * math.cos(a), cy + 40 * math.sin(a)])
        self.create_polygon(pts2, fill="#FB923C", outline="#F97316", width=2)

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Premium Origami Fold")
    root.configure(bg='#0F172A')
    
    spinner = OrigamiFold(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
