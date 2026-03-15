import tkinter as tk
import math

class ProgressRing(tk.Canvas):
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
        progress = (math.sin(t * 0.05) + 1) / 2  # 0 to 1
        extent = progress * 360
        r = 100
        self.create_oval(cx - r, cy - r, cx + r, cy + r, outline="#3A3A4A", width=8)
        if extent > 0:
            self.create_arc(cx - r, cy - r, cx + r, cy + r, start=90, extent=-extent, style=tk.ARC, outline="#89DCEB", width=8)
        self.after(30, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Progress Ring Loader")
    root.configure(bg='#1E1E2E')
    root.geometry("400x400")
    
    lbl = tk.Label(root, text="Progress Ring Loader", bg="#1E1E2E", fg="#A6ACCD", font=("Arial", 16, "bold"))
    lbl.pack(pady=20)
    
    spinner = ProgressRing(root, width=300, height=300)
    spinner.pack(expand=True)
    root.mainloop()
