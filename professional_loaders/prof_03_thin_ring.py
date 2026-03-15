import tkinter as tk
import math

class ThinRing(tk.Canvas):
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
        angle = (t * 6) % 360
        self.create_oval(cx-60, cy-60, cx+60, cy+60, outline="#E0E0E0", width=2)
        self.create_arc(cx-60, cy-60, cx+60, cy+60, start=angle, extent=90, style=tk.ARC, outline="#2196F3", width=3)

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Minimalist Thin Ring")
    root.configure(bg='white')
    
    spinner = ThinRing(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
