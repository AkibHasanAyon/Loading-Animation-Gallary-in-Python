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
        colors = ["#F38BA8", "#FAB387", "#F9E2AF", "#A6E3A1", "#89DCEB", "#89B4FA", "#CBA6F7", "#F5C2E7"]
        for i in range(8):
            angle = (t * -6 - i * 15) % 360
            r = 70 + 10 * math.sin(t * 0.1 + i)  # Wobbly radius
            x = cx + r * math.cos(math.radians(angle))
            y = cy + r * math.sin(math.radians(angle))
            size = 15 - i * 1.5
            self.create_oval(x-size, y-size, x+size, y+size, fill=colors[i], outline="")

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
