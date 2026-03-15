import tkinter as tk
import math

class AppleRing(tk.Canvas):
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
        angle = (t * 8) % 360
        self.create_arc(cx-50, cy-50, cx+50, cy+50, start=angle, extent=300, style=tk.ARC, outline="#8E8E93", width=4)

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Apple Style Indeterminate")
    root.configure(bg='white')
    
    spinner = AppleRing(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
