import tkinter as tk
import math

class WaveBars(tk.Canvas):
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
        for i in range(5):
            h = 20 + 60 * abs(math.sin(t * 0.15 + i * 0.5))
            x = cx - 60 + i * 30
            self.create_rectangle(x - 10, cy - h, x + 10, cy + h, fill="#89DCEB", outline="", width=0)
        self.after(30, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Wave Bars Loader")
    root.configure(bg='#1E1E2E')
    root.geometry("400x400")
    
    lbl = tk.Label(root, text="Wave Bars Loader", bg="#1E1E2E", fg="#A6ACCD", font=("Arial", 16, "bold"))
    lbl.pack(pady=20)
    
    spinner = WaveBars(root, width=300, height=300)
    spinner.pack(expand=True)
    root.mainloop()
