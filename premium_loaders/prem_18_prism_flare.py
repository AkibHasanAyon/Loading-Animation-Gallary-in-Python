import tkinter as tk
import math

class PrismFlare(tk.Canvas):
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
        self.create_polygon([cx, cy-50, cx+50, cy+40, cx-50, cy+40], outline="white", fill="", width=2)
        colors = ["#EF4444", "#F59E0B", "#10B981", "#3B82F6", "#8B5CF6"]
        for i in range(5):
            angle = math.radians(10 + i * 10 + math.sin(t * 0.1)*5)
            self.create_line(cx+20, cy+10, cx+120, cy+10+100*math.tan(angle), fill=colors[i], width=4)

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Premium Prism Flare")
    root.configure(bg='#0F172A')
    
    spinner = PrismFlare(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
