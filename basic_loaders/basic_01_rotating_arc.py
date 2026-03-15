import tkinter as tk
import math

class RotatingArc(tk.Canvas):
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
        angle = (t * 5) % 360
        self.create_arc(50, 50, 250, 250, start=angle, extent=270, style=tk.ARC, outline="#89DCEB", width=8)
        self.after(30, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Rotating Arc Loader")
    root.configure(bg='#1E1E2E')
    root.geometry("400x400")
    
    lbl = tk.Label(root, text="Rotating Arc Loader", bg="#1E1E2E", fg="#A6ACCD", font=("Arial", 16, "bold"))
    lbl.pack(pady=20)
    
    spinner = RotatingArc(root, width=300, height=300)
    spinner.pack(expand=True)
    root.mainloop()
