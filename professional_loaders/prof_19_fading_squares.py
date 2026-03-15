import tkinter as tk
import math

class FadingSquares(tk.Canvas):
    def __init__(self, parent, width=300, height=300, **kwargs):
        super().__init__(parent, width=width, height=height, bg='white', highlightthickness=0, **kwargs)
        self.cx = width / 2
        self.cy = height / 2
        self.frame_count = 0

        self.animate()
        
    def animate(self):
        self.frame_count += 1
        self.delete("all")
        t = self.frame_count
        cx, cy = self.cx, self.cy
        for i in range(3):
            for j in range(3):
                idx = i * 3 + j
                active = (t // 10) % 9 == idx
                color = "#455A64" if active else "#F5F5F5"
                self.create_rectangle(cx-50+i*35, cy-50+j*35, cx-20+i*35, cy-20+j*35, fill=color, outline="")

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Fading Square Grid")
    root.configure(bg='white')
    
    spinner = FadingSquares(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
