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
        w = int(self['width'])
        h = int(self['height'])
        cy = self.cy
        # Heartbeat line points scaled to full canvas
        pts = [20, cy, 75, cy, 112, cy - 75, 138, cy + 75, 175, cy, 280, cy]
        # Draw background trace
        self.create_line(pts, fill="#3A3A4A", width=4, smooth=False)
        # Draw active trace
        self.create_line(pts, fill="#89DCEB", width=4, smooth=False)
        # Sweeping mask
        sweep_x = (t * 4) % w
        self.create_rectangle(sweep_x, 0, w, h, fill="#1E1E2E", outline="")
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
