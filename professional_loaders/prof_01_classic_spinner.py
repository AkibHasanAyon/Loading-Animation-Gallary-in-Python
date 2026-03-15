import tkinter as tk
import math

class ClassicSpinner(tk.Canvas):
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
        for i in range(12):
            angle = i * 30
            # Opacity simulation using grays
            dist = (i - t // 4) % 12
            color_val = int(240 - (11 - dist) * 20)
            color = f'#%02x%02x%02x' % (color_val, color_val, color_val)
            
            rad_inner = 40
            rad_outer = 70
            x1 = cx + rad_inner * math.cos(math.radians(angle))
            y1 = cy + rad_inner * math.sin(math.radians(angle))
            x2 = cx + rad_outer * math.cos(math.radians(angle))
            y2 = cy + rad_outer * math.sin(math.radians(angle))
            self.create_line(x1, y1, x2, y2, fill=color, width=6, capstyle='round')

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Classic iOS Style Spinner")
    root.configure(bg='white')
    
    spinner = ClassicSpinner(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
