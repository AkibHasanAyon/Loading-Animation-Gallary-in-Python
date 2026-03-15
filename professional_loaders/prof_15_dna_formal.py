import tkinter as tk
import math

class DNAFormal(tk.Canvas):
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
            y = cy - 80 + i * 15
            x_off = 40 * math.sin(t * 0.1 + i * 0.5)
            self.create_line(cx-x_off, y, cx+x_off, y, fill="#ECEFF1")
            self.create_oval(cx-x_off-4, y-4, cx-x_off+4, y+4, fill="#546E7A", outline="")
            self.create_oval(cx+x_off-4, y-4, cx+x_off+4, y+4, fill="#90A4AE", outline="")

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Formal Gray Helix")
    root.configure(bg='white')
    
    spinner = DNAFormal(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
