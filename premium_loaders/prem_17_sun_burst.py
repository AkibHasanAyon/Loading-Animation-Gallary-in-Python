import tkinter as tk
import math

class SunBurst(tk.Canvas):
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
        for i in range(16):
            angle = i * 22.5 + t
            leng = 60 + 40 * abs(math.sin(t * 0.1 + i))
            x = cx + leng * math.cos(math.radians(angle))
            y = cy + leng * math.sin(math.radians(angle))
            self.create_line(cx, cy, x, y, fill="#FBBF24", width=3, capstyle='round')

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Premium Sun Burst")
    root.configure(bg='#0F172A')
    
    spinner = SunBurst(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
