import tkinter as tk
import math

class MorphingShape(tk.Canvas):
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
        factor = (math.sin(t * 0.1) + 1) / 2 # 0 to 1
        rad = 60
        pts = []
        for i in range(36):
            a = math.radians(i * 10)
            sx = cx + rad * max(-1, min(1, math.cos(a) * 2))
            sy = cy + rad * max(-1, min(1, math.sin(a) * 2))
            cx_c = cx + rad * math.cos(a)
            cy_c = cy + rad * math.sin(a)
            pts.append(sx * factor + cx_c * (1 - factor))
            pts.append(sy * factor + cy_c * (1 - factor))
        
        r = int(137 * factor + 245 * (1 - factor))
        g = int(220 * factor + 194 * (1 - factor))
        b = int(235 * factor + 231 * (1 - factor))
        color = f"#{r:02x}{g:02x}{b:02x}"
        self.create_polygon(pts, fill=color, outline="#F38BA8", width=4)

        self.after(30, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Morphing Shape Loader")
    root.configure(bg='#1E1E2E')
    root.geometry("400x400")
    
    lbl = tk.Label(root, text="Morphing Shape Loader", bg="#1E1E2E", fg="#A6ACCD", font=("Arial", 16, "bold"))
    lbl.pack(pady=20)
    
    spinner = MorphingShape(root, width=300, height=300)
    spinner.pack(expand=True)
    root.mainloop()
