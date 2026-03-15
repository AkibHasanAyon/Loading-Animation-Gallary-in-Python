import tkinter as tk
import math

class InfinityLoop(tk.Canvas):
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
        pts = []
        for i in range(60):
            a = math.radians(i * 6 + t * 5)
            x = cx + 90 * math.sin(a)
            y = cy + 45 * math.sin(2 * a)
            pts.extend([x, y])
        # Draw full trail
        if len(pts) >= 4:
            self.create_line(pts, fill="#89DCEB", width=6, smooth=True)
        self.after(30, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Infinity Loop Loader")
    root.configure(bg='#1E1E2E')
    root.geometry("400x400")
    
    lbl = tk.Label(root, text="Infinity Loop Loader", bg="#1E1E2E", fg="#A6ACCD", font=("Arial", 16, "bold"))
    lbl.pack(pady=20)
    
    spinner = InfinityLoop(root, width=300, height=300)
    spinner.pack(expand=True)
    root.mainloop()
