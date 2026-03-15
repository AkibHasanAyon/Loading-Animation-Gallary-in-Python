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
        self.create_rectangle(60, 100, 220, 200, outline="#A6ACCD", width=6)
        self.create_rectangle(220, 130, 240, 170, fill="#A6ACCD", outline="")
        bars = (t // 10) % 6
        colors = ["#F38BA8", "#FAB387", "#F9E2AF", "#A6E3A1", "#A6E3A1", "#A6E3A1"]
        for i in range(bars):
            x = 75 + i * 25
            self.create_rectangle(x, 115, x+18, 185, fill=colors[i], outline="")

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
