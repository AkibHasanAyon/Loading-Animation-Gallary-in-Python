import tkinter as tk
import math

class RotatingSquare(tk.Canvas):
    def __init__(self, parent, width=300, height=300, **kwargs):
        super().__init__(parent, width=width, height=height, bg='#1E1E2E', highlightthickness=0, **kwargs)
        self.cx = width / 2
        self.cy = height / 2
        self.frame_count = 0
        self.animate()

    def animate(self):
        self.frame_count += 1
        self.delete("all")
        t = self.frame_count
        cx, cy = self.cx, self.cy
        angle = math.radians(t * 4)
        size = 75
        pts = []
        for i in range(4):
            a = angle + i * math.pi / 2
            pts.append(cx + size * math.cos(a))
            pts.append(cy + size * math.sin(a))
        self.create_polygon(pts, outline="#89DCEB", fill="", width=5)
        self.after(30, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Rotating Square Loader")
    root.configure(bg='#1E1E2E')
    root.geometry("400x400")
    
    lbl = tk.Label(root, text="Rotating Square Loader", bg="#1E1E2E", fg="#A6ACCD", font=("Arial", 16, "bold"))
    lbl.pack(pady=20)
    
    spinner = RotatingSquare(root, width=300, height=300)
    spinner.pack(expand=True)
    root.mainloop()
