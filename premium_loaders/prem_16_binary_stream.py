import tkinter as tk
import math

class BinaryStream(tk.Canvas):
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
        import random
        random.seed(42)
        for i in range(20):
            x = (i * 20 + t * 2) % 300
            y = cy + 20 * math.sin(t * 0.05 + i)
            self.create_text(x, y, text=random.choice("01"), fill="#22C55E", font=("Arial", 10))

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Premium Binary Stream")
    root.configure(bg='#0F172A')
    
    spinner = BinaryStream(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
