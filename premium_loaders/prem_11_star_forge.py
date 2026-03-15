import tkinter as tk
import math

class StarForge(tk.Canvas):
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
        for i in range(10):
            angle = math.radians(i * 36 + t * 3)
            r = 80 if i % 2 == 0 else 30
            pts.extend([cx + r * math.cos(angle), cy + r * math.sin(angle)])
        self.create_polygon(pts, outline="#FBBF24", fill="", width=4)
        # Inner pulse
        pulse = 20 * abs(math.sin(t * 0.1))
        self.create_oval(cx-pulse, cy-pulse, cx+pulse, cy+pulse, fill="#F59E0B", outline="")

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Premium Star Forge")
    root.configure(bg='#0F172A')
    
    spinner = StarForge(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
