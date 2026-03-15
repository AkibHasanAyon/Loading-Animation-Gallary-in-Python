import tkinter as tk
import math

class MSDots(tk.Canvas):
    def __init__(self, parent, width=300, height=300, **kwargs):
        super().__init__(parent, width=width, height=height, bg='white', highlightthickness=0, **kwargs)
        self.cx = width / 2
        self.cy = height / 2
        self.frame_count = 0

        self.animate()
        
    def animate(self):
        self.frame_count += 1
        self.delete("all")
        t = self.frame_count
        cx, cy = self.cx, self.cy
        for i in range(5):
            # Non-linear speed for that MS "swing" feel
            phase = (t * 0.05 - i * 0.15) % (math.pi * 2)
            x_off = 80 * math.cos(phase)
            size = 5 if abs(x_off) < 60 else 3
            self.create_oval(cx+x_off-size, cy-size, cx+x_off+size, cy+size, fill="#0078D4", outline="")

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("MS Style Progress Dots")
    root.configure(bg='white')
    
    spinner = MSDots(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
