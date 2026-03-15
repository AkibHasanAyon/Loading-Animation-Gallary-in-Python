import tkinter as tk
import math

class LotusBloom(tk.Canvas):
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
        for i in range(8):
            angle = i * 45
            bloom = 40 * abs(math.sin(t * 0.05))
            x = cx + (40 + bloom) * math.cos(math.radians(angle))
            y = cy + (40 + bloom) * math.sin(math.radians(angle))
            self.create_oval(x-15, y-15, x+15, y+15, fill="#D8B4FE", outline="#A855F7")

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Premium Lotus Bloom")
    root.configure(bg='#0F172A')
    
    spinner = LotusBloom(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
