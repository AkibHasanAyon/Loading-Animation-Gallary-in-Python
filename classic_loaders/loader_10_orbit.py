import tkinter as tk
import math

class Orbit(tk.Canvas):
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
        self.create_oval(cx-25, cy-25, cx+25, cy+25, fill="#FAB387", outline="") # Sun
        
        # Orbit trails
        self.create_oval(cx-90, cy-90, cx+90, cy+90, outline="#3A3A4A", width=2)
        self.create_oval(cx-60, cy-60, cx+60, cy+60, outline="#3A3A4A", width=2)

        angle1 = math.radians(t * 4)
        x1 = cx + 90 * math.cos(angle1)
        y1 = cy + 90 * math.sin(angle1)
        self.create_oval(x1-15, y1-15, x1+15, y1+15, fill="#89B4FA", outline="") # Planet 1
        
        angle2 = math.radians(t * -6)
        x2 = cx + 60 * math.cos(angle2)
        y2 = cy + 60 * math.sin(angle2)
        self.create_oval(x2-10, y2-10, x2+10, y2+10, fill="#A6E3A1", outline="") # Planet 2

        self.after(30, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Orbit Loader")
    root.configure(bg='#1E1E2E')
    root.geometry("400x400")
    
    lbl = tk.Label(root, text="Orbit Loader", bg="#1E1E2E", fg="#A6ACCD", font=("Arial", 16, "bold"))
    lbl.pack(pady=20)
    
    spinner = Orbit(root, width=300, height=300)
    spinner.pack(expand=True)
    root.mainloop()
