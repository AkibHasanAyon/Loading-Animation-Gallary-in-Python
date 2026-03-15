import tkinter as tk
import math
import colorsys

class LiquidBlob(tk.Canvas):
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
        pts = []
        color = self.get_color()
        for i in range(72):
            a = math.radians(i * 5)
            # Complex oscillation for liquid feel
            r = 80 + 15 * math.sin(a * 3 + t * 0.1) + 10 * math.cos(a * 5 - t * 0.15)
            pts.extend([cx + r * math.cos(a), cy + r * math.sin(a)])
        self.create_polygon(pts, fill=color, outline="white", width=2, smooth=True)

        self.after(16, self.animate) # High refresh rate for smoothness

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Liquid Blob Morph")
    root.configure(bg='#0B0E14')
    
    # Glow Container
    spinner = LiquidBlob(root, width=400, height=400)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
