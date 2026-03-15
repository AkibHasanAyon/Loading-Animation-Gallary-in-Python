import tkinter as tk
import math

class PulseCircle(tk.Canvas):
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
        scale = (t % 50) / 50
        r = 20 + 60 * scale
        opacity = int(200 * (1 - scale))
        color = '#%02x%02x%02x' % (255-opacity, 255-opacity, 255) # Fades towards white
        self.create_oval(cx-r, cy-r, cx+r, cy+r, outline="#90CAF9", width=2)
        self.create_oval(cx-20, cy-20, cx+20, cy+20, fill="#2196F3", outline="")

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Professional Pulse")
    root.configure(bg='white')
    
    spinner = PulseCircle(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
