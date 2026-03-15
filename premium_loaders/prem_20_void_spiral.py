import tkinter as tk
import math

class VoidSpiral(tk.Canvas):
    def __init__(self, parent, width=300, height=300, **kwargs):
        super().__init__(parent, width=width, height=height, bg='#0F172A', highlightthickness=0, **kwargs)
        self.cx = width / 2
        self.cy = height / 2
        self.frame_count = 0

        self.animate()
        
    def animate(self):
        self.frame_count += 1
        self.delete("all")
        t = self.frame_count
        cx, cy = self.cx, self.cy
        for i in range(20):
            a = math.radians(i * 20 + t * 5)
            r = i * 6
            x = cx + r * math.cos(a)
            y = cy + r * math.sin(a)
            size = i / 2
            self.create_oval(x-size, y-size, x+size, y+size, fill="#C084FC", outline="")

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Premium Void Spiral")
    root.configure(bg='#0F172A')
    
    spinner = VoidSpiral(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
