import tkinter as tk
import math
import colorsys

class InfinityRainbow(tk.Canvas):
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
        for trail in range(20):
            pts = []
            color = self.get_color(hue_offset=-trail*0.02)
            for i in range(40):
                a = math.radians(i * 9 + t * 4 - trail * 2)
                x = cx + 120 * math.sin(a)
                y = cy + 60 * math.sin(2 * a)
                pts.extend([x, y])
            width = 10 - (trail * 0.4)
            if width > 0:
                self.create_line(pts[:4], fill=color, width=width, smooth=True, capstyle='round')

        self.after(16, self.animate) # High refresh rate for smoothness

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Infinity Rainbow Glow")
    root.configure(bg='#0B0E14')
    
    # Glow Container
    spinner = InfinityRainbow(root, width=400, height=400)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
