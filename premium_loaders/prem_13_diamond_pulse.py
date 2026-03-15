import tkinter as tk
import math

class DiamondPulse(tk.Canvas):
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
        for i in range(3):
            scale = ( (t*0.05 + i*0.3) % 1.0 )
            size = scale * 120
            pts = [cx, cy-size, cx+size, cy, cx, cy+size, cx-size, cy]
            alpha = int(255 * (1-scale))
            color = f'#%02x%02x%02x' % (100, 100 + alpha//2, 255)
            self.create_polygon(pts, outline=color, fill="", width=2)

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Premium Diamond Pulse")
    root.configure(bg='#0F172A')
    
    spinner = DiamondPulse(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
