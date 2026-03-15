import tkinter as tk
import math

class FadingCircle(tk.Canvas):
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
            angle = i * 45
            size = 6 + 12 * (0.5 + 0.5 * math.sin(t * 0.2 - i))
            rad = 80
            x = cx + rad * math.cos(math.radians(angle))
            y = cy + rad * math.sin(math.radians(angle))
            self.create_oval(x-size, y-size, x+size, y+size, fill=colors[i], outline="")

        self.after(30, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Fading Circle Loader")
    root.configure(bg='#1E1E2E')
    root.geometry("400x400")
    
    lbl = tk.Label(root, text="Fading Circle Loader", bg="#1E1E2E", fg="#A6ACCD", font=("Arial", 16, "bold"))
    lbl.pack(pady=20)
    
    spinner = FadingCircle(root, width=300, height=300)
    spinner.pack(expand=True)
    root.mainloop()
