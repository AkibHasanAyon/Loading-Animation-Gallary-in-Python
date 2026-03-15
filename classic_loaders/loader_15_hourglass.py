import tkinter as tk
import math

class Hourglass(tk.Canvas):
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
        angle = math.radians((t * 2) % 360)
        pts = [cx-60, cy-60, cx+60, cy-60, cx-60, cy+60, cx+60, cy+60]
        rot_pts = []
        for i in range(0, 8, 2):
            dx = pts[i] - cx
            dy = pts[i+1] - cy
            rx = cx + dx * math.cos(angle) - dy * math.sin(angle)
            ry = cy + dx * math.sin(angle) + dy * math.cos(angle)
            rot_pts.extend([rx, ry])
            
        # Draw sand
        sand_level = abs(math.sin(angle))
        
        self.create_polygon(rot_pts, fill="#F5C2E7", outline="#CBA6F7", width=6)
        self.create_oval(cx-10, cy-10, cx+10, cy+10, fill="#F9E2AF", outline="")

        self.after(30, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hourglass Loader")
    root.configure(bg='#1E1E2E')
    root.geometry("400x400")
    
    lbl = tk.Label(root, text="Hourglass Loader", bg="#1E1E2E", fg="#A6ACCD", font=("Arial", 16, "bold"))
    lbl.pack(pady=20)
    
    spinner = Hourglass(root, width=300, height=300)
    spinner.pack(expand=True)
    root.mainloop()
