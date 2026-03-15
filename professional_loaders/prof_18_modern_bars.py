import tkinter as tk
import math

class ModernBars(tk.Canvas):
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
        for i in range(5):
            h = 10 + 40 * abs(math.sin(t * 0.1 + i * 0.4))
            x = cx - 60 + i * 30
            self.create_rectangle(x-8, cy-h, x+8, cy+h, fill="#263238", outline="", width=0)

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Modern Corporate Bars")
    root.configure(bg='white')
    
    spinner = ModernBars(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
