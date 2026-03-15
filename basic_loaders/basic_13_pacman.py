import tkinter as tk
import math

class Pacman(tk.Canvas):
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
        # Pacman
        mouth_angle = 35 * abs(math.sin(t * 0.2))
        r = 60
        self.create_arc(cx - r - 30, cy - r, cx + r - 30, cy + r,
                        start=mouth_angle, extent=360 - 2 * mouth_angle,
                        fill="#F9E2AF", outline="")
        # Dots
        dot_offset = (t * 3) % 50
        for i in range(3):
            x = cx + 80 - dot_offset + i * 50
            if x > cx + 30:
                self.create_oval(x - 8, cy - 8, x + 8, cy + 8, fill="#F9E2AF", outline="")
        self.after(30, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pacman Loader")
    root.configure(bg='#1E1E2E')
    root.geometry("400x400")
    
    lbl = tk.Label(root, text="Pacman Loader", bg="#1E1E2E", fg="#A6ACCD", font=("Arial", 16, "bold"))
    lbl.pack(pady=20)
    
    spinner = Pacman(root, width=300, height=300)
    spinner.pack(expand=True)
    root.mainloop()
