import tkinter as tk
import math
import colorsys

class AuroraMist(tk.Canvas):
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
        for i in range(5):
            color = self.get_color(hue_offset=i*0.1, sat=0.6)
            pts = []
            for x in range(0, 401, 40):
                y_off = 50 * math.sin(t * 0.05 + x * 0.01 + i)
                pts.extend([x, cy - 100 + i * 40 + y_off])
            self.create_line(pts, fill=color, width=40, smooth=True, capstyle='round')

        self.after(16, self.animate) # High refresh rate for smoothness

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Aurora Mist Effect")
    root.configure(bg='#0B0E14')
    
    # Glow Container
    spinner = AuroraMist(root, width=400, height=400)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
