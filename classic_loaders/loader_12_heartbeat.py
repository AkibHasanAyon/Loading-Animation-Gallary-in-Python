import tkinter as tk
import math

class Heartbeat(tk.Canvas):
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
        pts = [20, 150, 80, 150, 110, 70, 140, 230, 170, 150, 280, 150]
        offset = - (t * 6) % 300
        shifted = []
        for i in range(0, len(pts), 2):
            nx = pts[i] + offset
            if nx < 0: nx += 300
            shifted.append(nx)
            shifted.append(pts[i+1])
        
        self.create_line(pts, fill="#3A3A4A", width=6, smooth=False)
        sweep_x = (t * 8) % 300
        self.create_line(pts, fill="#F38BA8", width=6, smooth=False)
        self.create_rectangle(sweep_x, 0, 300, 300, fill="#1E1E2E", outline="") # Mask

        self.after(30, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Heartbeat Loader")
    root.configure(bg='#1E1E2E')
    root.geometry("400x400")
    
    lbl = tk.Label(root, text="Heartbeat Loader", bg="#1E1E2E", fg="#A6ACCD", font=("Arial", 16, "bold"))
    lbl.pack(pady=20)
    
    spinner = Heartbeat(root, width=300, height=300)
    spinner.pack(expand=True)
    root.mainloop()
