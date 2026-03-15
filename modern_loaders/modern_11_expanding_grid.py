import tkinter as tk
import math
import colorsys

class ExpandingGrid(tk.Canvas):
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
        for i in range(-3, 4):
            for j in range(-3, 4):
                px = cx + i * 40
                py = cy + j * 40
                dist = math.sqrt(i**2 + j**2)
                size = 15 * abs(math.sin(t * 0.1 - dist * 0.5))
                color = self.get_color(hue_offset=dist*0.1)
                self.create_rectangle(px-size, py-size, px+size, py+size, fill=color, outline="white")

        self.after(16, self.animate) # High refresh rate for smoothness

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hex Grid Pulse")
    root.configure(bg='#0B0E14')
    
    # Glow Container
    spinner = ExpandingGrid(root, width=400, height=400)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
