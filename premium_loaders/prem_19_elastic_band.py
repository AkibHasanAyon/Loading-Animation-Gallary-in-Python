import tkinter as tk
import math

class ElasticBand(tk.Canvas):
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
        sway = 40 * math.sin(t * 0.2)
        pts = [cx-80, cy, cx+sway, cy-40, cx+80, cy, cx+sway, cy+40]
        self.create_polygon(pts, outline="#818CF8", fill="#312E81", width=3, smooth=True)

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Premium Elastic Band")
    root.configure(bg='#0F172A')
    
    spinner = ElasticBand(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
