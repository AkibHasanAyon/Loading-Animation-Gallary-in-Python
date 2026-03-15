import tkinter as tk
import math

class SnakeChase(tk.Canvas):
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
        for i in range(6):
            angle = (t * -5 - i * 15) % 360
            r = 80
            x = cx + r * math.cos(math.radians(angle))
            y = cy + r * math.sin(math.radians(angle))
            size = 15 - i * 2
            self.create_oval(x - size, y - size, x + size, y + size, fill="#89DCEB", outline="")
        self.after(30, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Snake Chase Loader")
    root.configure(bg='#1E1E2E')
    root.geometry("400x400")
    
    lbl = tk.Label(root, text="Snake Chase Loader", bg="#1E1E2E", fg="#A6ACCD", font=("Arial", 16, "bold"))
    lbl.pack(pady=20)
    
    spinner = SnakeChase(root, width=300, height=300)
    spinner.pack(expand=True)
    root.mainloop()
