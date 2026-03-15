import tkinter as tk
import math

class StepSegments(tk.Canvas):
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
            angle = i * 45
            active = (t // 8) % 8 == i
            color = "#1976D2" if active else "#E0E0E0"
            self.create_arc(cx-60, cy-60, cx+60, cy+60, start=angle+5, extent=35, style=tk.ARC, outline=color, width=8)

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Segmented Step Loader")
    root.configure(bg='white')
    
    spinner = StepSegments(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
