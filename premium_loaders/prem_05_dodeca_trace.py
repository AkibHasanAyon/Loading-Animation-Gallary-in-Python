import tkinter as tk
import math

class DodecaTrace(tk.Canvas):
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
        for i in range(5):
            angle = i * 72 + t
            r1 = 60
            r2 = 90
            x1, y1 = cx + r1 * math.cos(math.radians(angle)), cy + r1 * math.sin(math.radians(angle))
            x2, y2 = cx + r2 * math.cos(math.radians(angle+36)), cy + r2 * math.sin(math.radians(angle+36))
            self.create_line(x1, y1, x2, y2, fill="#A78BFA", width=3)
            self.create_oval(x1-4, y1-4, x1+4, y1+4, fill="white")

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Premium Dodecahedron Trace")
    root.configure(bg='#0F172A')
    
    spinner = DodecaTrace(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
