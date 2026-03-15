import tkinter as tk
import math

class SlateBar(tk.Canvas):
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
        self.create_rectangle(cx-100, cy-4, cx+100, cy+4, fill="#F5F5F5", outline="")
        x_start = cx - 100 + ((t * 4) % 260) - 60
        x_end = x_start + 60
        # Clip to boundaries
        disp_start = max(cx-100, x_start)
        disp_end = min(cx+100, x_end)
        if disp_start < disp_end:
            self.create_rectangle(disp_start, cy-4, disp_end, cy+4, fill="#455A64", outline="")

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Slate Progress Bar")
    root.configure(bg='white')
    
    spinner = SlateBar(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
