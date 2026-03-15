import tkinter as tk
import math

class DualRing(tk.Canvas):
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
        a1 = (t * 4) % 360
        a2 = (-t * 6) % 360
        self.create_arc(cx-60, cy-60, cx+60, cy+60, start=a1, extent=120, style=tk.ARC, outline="#37474F", width=4)
        self.create_arc(cx-45, cy-45, cx+45, cy+45, start=a2, extent=120, style=tk.ARC, outline="#90A4AE", width=3)

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Dual Opposing Rings")
    root.configure(bg='white')
    
    spinner = DualRing(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
