import tkinter as tk
import math

class MaterialDots(tk.Canvas):
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
        colors = ["#4285F4", "#EA4335", "#FBBC05", "#34A853"] # Google Colors
        for i in range(4):
            x = cx - 60 + i * 40
            y_off = 20 * math.sin(t * 0.15 + i * 0.8)
            self.create_oval(x-10, cy-10+y_off, x+10, cy+10+y_off, fill=colors[i], outline="")

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Material Design Dots")
    root.configure(bg='white')
    
    spinner = MaterialDots(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
