import tkinter as tk
import math
import colorsys

class FidgetSpinner(tk.Canvas):
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
        angle = math.radians(t * 10)
        for i in range(3):
            a = angle + i * (math.pi * 2 / 3)
            x = cx + 70 * math.cos(a)
            y = cy + 70 * math.sin(a)
            color = self.get_color(hue_offset=i*0.33)
            self.create_line(cx, cy, x, y, fill="white", width=20, capstyle='round')
            self.create_oval(x-30, y-30, x+30, y+30, fill=color, outline="white", width=4)

        self.after(16, self.animate) # High refresh rate for smoothness

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Modern Fidget Glow")
    root.configure(bg='#0B0E14')
    
    # Glow Container
    spinner = FidgetSpinner(root, width=400, height=400)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
