import tkinter as tk
import math

class OrbitDots(tk.Canvas):
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
        for i in range(8):
            angle = i * 45 + t * 4
            r = 60
            size = 3 + 4 * (1 - i/8)
            x = cx + r * math.cos(math.radians(angle))
            y = cy + r * math.sin(math.radians(angle))
            self.create_oval(x-size, y-size, x+size, y+size, fill="#607D8B", outline="")

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Clean Orbital Dots")
    root.configure(bg='white')
    
    spinner = OrbitDots(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
