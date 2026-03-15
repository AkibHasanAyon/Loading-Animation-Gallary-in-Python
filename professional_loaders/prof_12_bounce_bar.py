import tkinter as tk
import math

class BounceBar(tk.Canvas):
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
        self.create_rectangle(cx-80, cy-2, cx+80, cy+2, fill="#F0F0F0", outline="")
        pos = 60 * math.sin(t * 0.1)
        self.create_rectangle(cx+pos-20, cy-3, cx+pos+20, cy+3, fill="#00ACC1", outline="")

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Bouncing Segment Bar")
    root.configure(bg='white')
    
    spinner = BounceBar(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
