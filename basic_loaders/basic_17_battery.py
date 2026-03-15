import tkinter as tk
import math

class Battery(tk.Canvas):
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
        # Battery body
        bx1, by1 = cx - 80, cy - 50
        bx2, by2 = cx + 60, cy + 50
        self.create_rectangle(bx1, by1, bx2, by2, outline="#89DCEB", width=4)
        # Battery terminal
        self.create_rectangle(bx2, cy - 20, bx2 + 15, cy + 20, fill="#89DCEB", outline="")
        # Filling bars
        bars = (t // 10) % 5
        bar_width = 24
        for i in range(bars):
            x = bx1 + 12 + i * (bar_width + 6)
            self.create_rectangle(x, by1 + 10, x + bar_width, by2 - 10, fill="#89DCEB", outline="")
        self.after(30, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Battery Loader")
    root.configure(bg='#1E1E2E')
    root.geometry("400x400")
    
    lbl = tk.Label(root, text="Battery Loader", bg="#1E1E2E", fg="#A6ACCD", font=("Arial", 16, "bold"))
    lbl.pack(pady=20)
    
    spinner = Battery(root, width=300, height=300)
    spinner.pack(expand=True)
    root.mainloop()
