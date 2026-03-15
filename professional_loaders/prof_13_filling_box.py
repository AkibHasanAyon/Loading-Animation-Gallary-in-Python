import tkinter as tk
import math

class FillingBox(tk.Canvas):
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
        self.create_rectangle(cx-40, cy-40, cx+40, cy+40, outline="#BDBDBD", width=2)
        h = 80 * ((t % 100) / 100)
        self.create_rectangle(cx-40, cy+40-h, cx+40, cy+40, fill="#3F51B5", outline="")

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Filling Square Frame")
    root.configure(bg='white')
    
    spinner = FillingBox(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
