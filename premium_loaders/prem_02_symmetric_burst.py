import tkinter as tk
import math

class SymmetricBurst(tk.Canvas):
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
        for i in range(12):
            angle = i * 30 + t * 2
            size = 40 + 60 * abs(math.sin(t * 0.1))
            x = cx + size * math.cos(math.radians(angle))
            y = cy + size * math.sin(math.radians(angle))
            color = "#F472B6" if i % 2 == 0 else "#818CF8"
            self.create_rectangle(x-10, y-10, x+10, y+10, fill=color, outline="white", width=1)

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Premium Symmetric Burst")
    root.configure(bg='#0F172A')
    
    spinner = SymmetricBurst(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
