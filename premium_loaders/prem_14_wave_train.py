import tkinter as tk
import math

class WaveTrain(tk.Canvas):
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
        for i in range(3):
            pts = []
            for x in range(50, 251, 10):
                y = cy - 40 + i * 40 + 20 * math.sin(t * 0.1 + x * 0.05)
                pts.extend([x, y])
            self.create_line(pts, fill=f"#{(i+1)*50:02x}BDF8", width=4, smooth=True)

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Premium Wave Train")
    root.configure(bg='#0F172A')
    
    spinner = WaveTrain(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
