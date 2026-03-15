import tkinter as tk
import math

class CubeSpin(tk.Canvas):
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
        # 3D to 2D project approx
        nodes = [(-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
                 (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)]
        edges = [(0,1), (1,2), (2,3), (3,0), (4,5), (5,6), (6,7), (7,4), (0,4), (1,5), (2,6), (3,7)]
        angle = t * 0.05
        # Transform & Project
        proj = []
        for x,y,z in nodes:
            # Rotate Y
            rx = x * math.cos(angle) - z * math.sin(angle)
            rz = x * math.sin(angle) + z * math.cos(angle)
            # Rotate X
            ry = y * math.cos(angle*0.5) - rz * math.sin(angle*0.5)
            rrz = y * math.sin(angle*0.5) + rz * math.cos(angle*0.5)
            proj.append((cx + rx * 50, cy + ry * 50))
        for e1, e2 in edges:
            self.create_line(proj[e1][0], proj[e1][1], proj[e2][0], proj[e2][1], fill="#E2E8F0", width=2)

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Premium Cube Wireframe")
    root.configure(bg='#0F172A')
    
    spinner = CubeSpin(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
