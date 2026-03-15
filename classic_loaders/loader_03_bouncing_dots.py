import tkinter as tk
import math

class BouncingDots(tk.Canvas):
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
        colors = ["#F38BA8", "#F9E2AF", "#A6E3A1", "#89DCEB", "#CBA6F7"]
        for i in range(5):
            y_offset = 30 * math.sin(t * 0.2 + i)
            x = cx - 80 + i * 40
            self.create_oval(x-15, cy-15+y_offset, x+15, cy+15+y_offset, fill=colors[i], outline="")

        self.after(30, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Bouncing Dots Loader")
    root.configure(bg='#1E1E2E')
    root.geometry("400x400")
    
    lbl = tk.Label(root, text="Bouncing Dots Loader", bg="#1E1E2E", fg="#A6ACCD", font=("Arial", 16, "bold"))
    lbl.pack(pady=20)
    
    spinner = BouncingDots(root, width=300, height=300)
    spinner.pack(expand=True)
    root.mainloop()
