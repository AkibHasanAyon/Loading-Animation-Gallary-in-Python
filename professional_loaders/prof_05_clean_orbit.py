import tkinter as tk
import math

class CleanOrbit(tk.Canvas):
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
        self.create_oval(cx-50, cy-50, cx+50, cy+50, outline="#EEEEEE", width=1)
        a = math.radians(t * 5)
        x = cx + 50 * math.cos(a)
        y = cy + 50 * math.sin(a)
        self.create_oval(x-6, y-6, x+6, y+6, fill="#1976D2", outline="")

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Clean Minimalist Orbit")
    root.configure(bg='white')
    
    spinner = CleanOrbit(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
