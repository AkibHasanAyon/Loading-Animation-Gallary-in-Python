import tkinter as tk
import math

class Orbit(tk.Canvas):
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
        self.create_oval(cx - 15, cy - 15, cx + 15, cy + 15, fill="#F38BA8", outline="")  # Sun
        angle = math.radians(t * 5)
        r = 80
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        self.create_oval(x - 12, y - 12, x + 12, y + 12, fill="#89DCEB", outline="")  # Planet
        self.after(30, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Orbit Loader")
    root.configure(bg='#1E1E2E')
    root.geometry("400x400")
    
    lbl = tk.Label(root, text="Orbit Loader", bg="#1E1E2E", fg="#A6ACCD", font=("Arial", 16, "bold"))
    lbl.pack(pady=20)
    
    spinner = Orbit(root, width=300, height=300)
    spinner.pack(expand=True)
    root.mainloop()
