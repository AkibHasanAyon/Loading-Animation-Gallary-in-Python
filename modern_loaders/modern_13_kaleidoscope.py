import tkinter as tk
import math
import colorsys

class Kaleidoscope(tk.Canvas):
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
        for i in range(8):
            angle = math.radians(i * 45 + t)
            color = self.get_color(hue_offset=i/8)
            r1 = 20 + 60 * abs(math.sin(t * 0.08))
            r2 = r1 + 40
            x1, y1 = cx + r1 * math.cos(angle), cy + r1 * math.sin(angle)
            x2, y2 = cx + r2 * math.cos(angle + 0.5), cy + r2 * math.sin(angle + 0.5)
            x3, y3 = cx + r2 * math.cos(angle - 0.5), cy + r2 * math.sin(angle - 0.5)
            self.create_polygon([x1, y1, x2, y2, x3, y3], fill=color, outline="white")

        self.after(16, self.animate) # High refresh rate for smoothness

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Kaleidoscope Burst")
    root.configure(bg='#0B0E14')
    
    # Glow Container
    spinner = Kaleidoscope(root, width=400, height=400)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
