import tkinter as tk
import math
import colorsys

class SpectrumRing(tk.Canvas):
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
        for i in range(60):
            angle = i * 6
            h = 20 + 40 * abs(math.sin(t * 0.1 + i * 0.1))
            color = self.get_color(hue_offset=i/60)
            x1 = cx + 80 * math.cos(math.radians(angle))
            y1 = cy + 80 * math.sin(math.radians(angle))
            x2 = cx + (80+h) * math.cos(math.radians(angle))
            y2 = cy + (80+h) * math.sin(math.radians(angle))
            self.create_line(x1, y1, x2, y2, fill=color, width=3)

        self.after(16, self.animate) # High refresh rate for smoothness

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Spectrum Ring")
    root.configure(bg='#0B0E14')
    
    # Glow Container
    spinner = SpectrumRing(root, width=400, height=400)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
