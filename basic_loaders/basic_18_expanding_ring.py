import tkinter as tk
import math

class ExpandingRing(tk.Canvas):
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
        r = (t * 2) % 120
        alpha = max(0, 1 - r / 120)
        width_val = max(1, int(6 * alpha))
        self.create_oval(cx - r, cy - r, cx + r, cy + r, outline="#89DCEB", width=width_val)
        self.create_oval(cx - 12, cy - 12, cx + 12, cy + 12, fill="#89DCEB", outline="")
        self.after(30, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Expanding Ring Loader")
    root.configure(bg='#1E1E2E')
    root.geometry("400x400")
    
    lbl = tk.Label(root, text="Expanding Ring Loader", bg="#1E1E2E", fg="#A6ACCD", font=("Arial", 16, "bold"))
    lbl.pack(pady=20)
    
    spinner = ExpandingRing(root, width=300, height=300)
    spinner.pack(expand=True)
    root.mainloop()
