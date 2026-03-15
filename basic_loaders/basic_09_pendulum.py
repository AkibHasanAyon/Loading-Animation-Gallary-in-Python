import tkinter as tk
import math

class Pendulum(tk.Canvas):
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
        pivot_y = 40
        angle = math.radians(90 + 35 * math.sin(t * 0.1))
        length = 120
        x = cx + length * math.cos(angle)
        y = pivot_y + length * math.sin(angle)
        self.create_line(cx, pivot_y, x, y, fill="#89DCEB", width=3)
        self.create_oval(x - 25, y - 25, x + 25, y + 25, fill="#89DCEB", outline="")
        self.create_oval(cx - 6, pivot_y - 6, cx + 6, pivot_y + 6, fill="#F38BA8", outline="")
        self.after(30, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pendulum Loader")
    root.configure(bg='#1E1E2E')
    root.geometry("400x400")
    
    lbl = tk.Label(root, text="Pendulum Loader", bg="#1E1E2E", fg="#A6ACCD", font=("Arial", 16, "bold"))
    lbl.pack(pady=20)
    
    spinner = Pendulum(root, width=300, height=300)
    spinner.pack(expand=True)
    root.mainloop()
