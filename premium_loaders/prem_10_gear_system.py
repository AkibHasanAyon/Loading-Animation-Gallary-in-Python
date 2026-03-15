import tkinter as tk
import math

class GearSystem(tk.Canvas):
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
        # Main Gear
        angle = t * 2
        self.create_oval(cx-40, cy-40, cx+40, cy+40, outline="#64748B", width=8)
        for i in range(8):
            a = math.radians(angle + i * 45)
            self.create_line(cx+35*math.cos(a), cy+35*math.sin(a), cx+55*math.cos(a), cy+55*math.sin(a), fill="#64748B", width=8)
        
        # Small Gear
        angle2 = -t * 4
        scx, scy = cx + 75, cy
        self.create_oval(scx-20, scy-20, scx+20, scy+20, outline="#94A3B8", width=5)
        for i in range(6):
            a = math.radians(angle2 + i * 60)
            self.create_line(scx+15*math.cos(a), scy+15*math.sin(a), scx+30*math.cos(a), scy+30*math.sin(a), fill="#94A3B8", width=6)

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Premium Gear System")
    root.configure(bg='#0F172A')
    
    spinner = GearSystem(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
