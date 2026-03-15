import tkinter as tk
import math
import colorsys

class OrbitalGlow(tk.Canvas):
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
        for i in range(3):
            r_base = 60 + i * 30
            angle_speed = (4 - i) * 2
            a = math.radians(t * angle_speed)
            x = cx + r_base * math.cos(a)
            y = cy + r_base * math.sin(a)
            color = self.get_color(hue_offset=i*0.3)
            # Glow trail simulation
            for streak in range(5):
                prev_a = math.radians(t * angle_speed - streak * 5)
                px = cx + r_base * math.cos(prev_a)
                py = cy + r_base * math.sin(prev_a)
                self.create_oval(px-8+streak, py-8+streak, px+8-streak, py+8-streak, fill=color, outline="")

        self.after(16, self.animate) # High refresh rate for smoothness

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Orbital Glow")
    root.configure(bg='#0B0E14')
    
    # Glow Container
    spinner = OrbitalGlow(root, width=400, height=400)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
