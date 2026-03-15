import tkinter as tk
import math

class FoldingCube(tk.Canvas):
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
        size = 40
        for i in range(4):
            # Logic to "hide" segments based on time
            if (t // 20) % 4 == i: continue
            ax = cx + (size if i in [1,2] else -size)
            ay = cy + (size if i in [2,3] else -size)
            self.create_rectangle(ax-18, ay-18, ax+18, ay+18, fill="#03A9F4", outline="white")

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Minimalist Folding Logic")
    root.configure(bg='white')
    
    spinner = FoldingCube(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
