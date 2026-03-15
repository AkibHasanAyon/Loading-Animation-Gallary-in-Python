import tkinter as tk
import math

class ProgressRing(tk.Canvas):
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
        progress = (math.sin(t * 0.05) + 1) / 2 # 0 to 1
        extent = progress * 360
        self.create_oval(50, 50, 250, 250, outline="#3A3A4A", width=12)
        
        # Multi-colored segments based on progress
        color = "#F38BA8"
        if progress > 0.33: color = "#F9E2AF"
        if progress > 0.66: color = "#A6E3A1"

        if extent > 0:
            self.create_arc(50, 50, 250, 250, start=90, extent=-extent, style=tk.ARC, outline=color, width=12)

        self.after(30, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Progress Ring Loader")
    root.configure(bg='#1E1E2E')
    root.geometry("400x400")
    
    lbl = tk.Label(root, text="Progress Ring Loader", bg="#1E1E2E", fg="#A6ACCD", font=("Arial", 16, "bold"))
    lbl.pack(pady=20)
    
    spinner = ProgressRing(root, width=300, height=300)
    spinner.pack(expand=True)
    root.mainloop()
