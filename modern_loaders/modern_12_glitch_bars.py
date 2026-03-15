import tkinter as tk
import math
import colorsys

class GlitchBars(tk.Canvas):
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
        import random
        for i in range(10):
            y = 80 + i * 25
            w = 200 + random.randint(-20, 20)
            off = random.randint(-5, 5) if t % 5 == 0 else 0
            color = self.get_color(hue_offset=random.random() if t % 10 == 0 else i/10)
            self.create_rectangle(cx-w/2+off, y, cx+w/2+off, y+15, fill=color, outline="")

        self.after(16, self.animate) # High refresh rate for smoothness

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Cyberpunk Glitch Bars")
    root.configure(bg='#0B0E14')
    
    # Glow Container
    spinner = GlitchBars(root, width=400, height=400)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
