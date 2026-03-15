import tkinter as tk
import math

class FluidRipples(tk.Canvas):
    def __init__(self, parent, width=300, height=300, **kwargs):
        super().__init__(parent, width=width, height=height, bg='#0F172A', highlightthickness=0, **kwargs)
        self.cx = width / 2
        self.cy = height / 2
        self.frame_count = 0

        self.animate()
        
    def animate(self):
        self.frame_count += 1
        self.delete("all")
        t = self.frame_count
        cx, cy = self.cx, self.cy
        for i in range(4):
            period = (t + i * 25) % 100
            r = period * 1.2
            alpha = max(0, 1 - period/100)
            # Custom stroke width based on expansion
            w = max(1, int(8 * alpha))
            self.create_oval(cx-r, cy-r, cx+r, cy+r, outline="#2DD4BF", width=w)

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Premium Fluid Ripples")
    root.configure(bg='#0F172A')
    
    spinner = FluidRipples(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
