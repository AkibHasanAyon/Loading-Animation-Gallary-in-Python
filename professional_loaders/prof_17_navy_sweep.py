import tkinter as tk
import math

class NavySweep(tk.Canvas):
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
        self.create_oval(cx-70, cy-70, cx+70, cy+70, outline="#CFD8DC", width=1)
        angle = (t * 5) % 360
        self.create_arc(cx-70, cy-70, cx+70, cy+70, start=angle, extent=-60, fill="#1A237E", outline="")

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Navy Radar Sweep")
    root.configure(bg='white')
    
    spinner = NavySweep(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
