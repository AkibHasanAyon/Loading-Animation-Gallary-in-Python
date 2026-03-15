import tkinter as tk
import math

class DoubleHelix(tk.Canvas):
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
        for i in range(12):
            y = 20 + i * 22
            x_offset = 50 * math.sin(t * 0.1 + i * 0.5)
            self.create_oval(cx - 12 + x_offset, y - 8, cx - 4 + x_offset, y + 8, fill="#F38BA8", outline="")
            self.create_oval(cx + 4 - x_offset, y - 8, cx + 12 - x_offset, y + 8, fill="#89DCEB", outline="")
        self.after(30, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Double Helix Loader")
    root.configure(bg='#1E1E2E')
    root.geometry("400x400")
    
    lbl = tk.Label(root, text="Double Helix Loader", bg="#1E1E2E", fg="#A6ACCD", font=("Arial", 16, "bold"))
    lbl.pack(pady=20)
    
    spinner = DoubleHelix(root, width=300, height=300)
    spinner.pack(expand=True)
    root.mainloop()
