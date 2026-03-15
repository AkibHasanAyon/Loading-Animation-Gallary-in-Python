import tkinter as tk
import math

class RadialEcho(tk.Canvas):
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
            shift = (t + i * 20) % 60
            r = shift * 1.5
            alpha = int(255 * (1 - shift/60))
            color = f'#%02x%02x%02x' % (255-alpha, 255-alpha, 255-alpha)
            self.create_oval(cx-r, cy-r, cx+r, cy+r, outline="#78909C", width=1)

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Radial Echo Ripples")
    root.configure(bg='white')
    
    spinner = RadialEcho(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
