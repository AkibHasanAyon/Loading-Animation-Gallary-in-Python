import tkinter as tk
import math
import colorsys

class DNARainbow(tk.Canvas):
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
        for i in range(20):
            y = 50 + i * 15
            phase = t * 0.1 + i * 0.3
            x_off = 70 * math.sin(phase)
            c1 = self.get_color(hue_offset=i/20)
            c2 = self.get_color(hue_offset=i/20 + 0.5)
            self.create_line(cx-x_off, y, cx+x_off, y, fill="gray20")
            self.create_oval(cx-x_off-8, y-8, cx-x_off+8, y+8, fill=c1, outline="white")
            self.create_oval(cx+x_off-8, y-8, cx+x_off+8, y+8, fill=c2, outline="white")

        self.after(16, self.animate) # High refresh rate for smoothness

if __name__ == "__main__":
    root = tk.Tk()
    root.title("DNA Rainbow Helix")
    root.configure(bg='#0B0E14')
    
    # Glow Container
    spinner = DNARainbow(root, width=400, height=400)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
