import tkinter as tk
import math

class LatticeGrowth(tk.Canvas):
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
        for i in range(8):
            ext = 80 * abs(math.sin(t * 0.05 + i * 0.4))
            angle = i * 45
            x = cx + ext * math.cos(math.radians(angle))
            y = cy + ext * math.sin(math.radians(angle))
            self.create_line(cx, cy, x, y, fill="#38BDF8", width=3)
            self.create_oval(x-5, y-5, x+5, y+5, fill="#F0F9FF", outline="#0EA5E9")

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Premium Lattice Growth")
    root.configure(bg='#0F172A')
    
    spinner = LatticeGrowth(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
