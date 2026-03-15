import tkinter as tk
import math

class ExpandingRing(tk.Canvas):
    def __init__(self, parent, width=300, height=300, **kwargs):
        super().__init__(parent, width=width, height=height, bg='#1E1E2E', highlightthickness=0, **kwargs)
        self.cx = width / 2
        self.cy = height / 2
        self.frame_count = 0

        self.animate()
        

    def animate(self):
        self.frame_count += 1
        self.delete("all")
        t = self.frame_count
        cx, cy = self.cx, self.cy
        r1 = (t * 3) % 120
        alpha1 = max(0, 1 - r1/120)
        r2 = ((t * 3) - 60) % 120
        if r2 < 0: r2 += 120
        alpha2 = max(0, 1 - r2/120)
        
        w1 = max(1, int(12 * alpha1))
        w2 = max(1, int(12 * alpha2))
        
        self.create_oval(cx-r1, cy-r1, cx+r1, cy+r1, outline="#89B4FA", width=w1)
        self.create_oval(cx-r2, cy-r2, cx+r2, cy+r2, outline="#CBA6F7", width=w2)
        self.create_oval(cx-15, cy-15, cx+15, cy+15, fill="#F5C2E7", outline="")

        self.after(30, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Expanding Ring Loader")
    root.configure(bg='#1E1E2E')
    root.geometry("400x400")
    
    lbl = tk.Label(root, text="Expanding Ring Loader", bg="#1E1E2E", fg="#A6ACCD", font=("Arial", 16, "bold"))
    lbl.pack(pady=20)
    
    spinner = ExpandingRing(root, width=300, height=300)
    spinner.pack(expand=True)
    root.mainloop()
