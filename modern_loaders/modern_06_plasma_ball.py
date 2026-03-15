import tkinter as tk
import math
import colorsys

class PlasmaBall(tk.Canvas):
    def __init__(self, parent, width=400, height=400, **kwargs):
        super().__init__(parent, width=width, height=height, bg='#0B0E14', highlightthickness=0, **kwargs)
        self.cx = width / 2
        self.cy = height / 2
        self.frame_count = 0

        self.animate()
        
    def get_color(self, hue_offset=0, sat=0.8, val=1.0):
        # Smooth HSL to RGB conversion
        hue = (self.frame_count * 0.01 + hue_offset) % 1.0
        r, g, b = colorsys.hsv_to_rgb(hue, sat, val)
        return '#%02x%02x%02x' % (int(r*255), int(g*255), int(b*255))


    def animate(self):
        self.frame_count += 1
        self.delete("all")
        t = self.frame_count
        cx, cy = self.cx, self.cy
        self.create_oval(cx-60, cy-60, cx+60, cy+60, outline="white", width=2)
        for i in range(5):
            a1 = t * 0.05 + i * 72
            a2 = t * 0.08 + i * 45
            x1 = cx + 60 * math.cos(math.radians(a1))
            y1 = cy + 60 * math.sin(math.radians(a1))
            x2 = cx + 60 * math.cos(math.radians(a2))
            y2 = cy + 60 * math.sin(math.radians(a2))
            color = self.get_color(hue_offset=i*0.2)
            self.create_line(cx, cy, x1, y1, fill=color, width=4, capstyle='round')
            self.create_oval(x1-5, y1-5, x1+5, y1+5, fill=color, outline="")

        self.after(16, self.animate) # High refresh rate for smoothness

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Plasma Ball")
    root.configure(bg='#0B0E14')
    
    # Glow Container
    spinner = PlasmaBall(root, width=400, height=400)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
