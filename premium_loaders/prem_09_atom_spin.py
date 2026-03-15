import tkinter as tk
import math

class AtomSpin(tk.Canvas):
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
        self.create_oval(cx-15, cy-15, cx+15, cy+15, fill="#FDE047") # Nucleus
        for i in range(3):
            angle = math.radians(t * (5+i))
            rx = 80
            ry = 30
            rot = i * math.pi / 3
            # Rotate ellipse
            pts = []
            for a in range(0, 361, 10):
                rad = math.radians(a)
                lx = rx * math.cos(rad)
                ly = ry * math.sin(rad)
                # Apply rotation
                nx = cx + lx * math.cos(rot) - ly * math.sin(rot)
                ny = cy + lx * math.sin(rot) + ly * math.cos(rot)
                pts.extend([nx, ny])
            self.create_line(pts, fill="#94A3B8", width=1)
            # Electron
            ex = rx * math.cos(angle)
            ey = ry * math.sin(angle)
            enx = cx + ex * math.cos(rot) - ey * math.sin(rot)
            eny = cy + ex * math.sin(rot) + ey * math.cos(rot)
            self.create_oval(enx-5, eny-5, enx+5, eny+5, fill="#38BDF8")

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Premium Atom Spin")
    root.configure(bg='#0F172A')
    
    spinner = AtomSpin(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
