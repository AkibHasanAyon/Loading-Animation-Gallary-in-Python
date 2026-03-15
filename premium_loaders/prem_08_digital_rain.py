import tkinter as tk
import math

class DigitalRain(tk.Canvas):
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
        for i in range(8):
            x = cx - 70 + i * 20
            y_base = (t * 5 + i * 40) % 200
            for j in range(5):
                alpha_y = y_base - j * 15
                if 50 < alpha_y < 250:
                    color = f'#%02x%02x%02x' % (0, 255 - j*40, 0)
                    self.create_text(x, alpha_y, text=str(i%2), fill=color, font=("Courier", 12, "bold"))

        self.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Premium Digital Rain")
    root.configure(bg='#0F172A')
    
    spinner = DigitalRain(root, width=300, height=300)
    spinner.pack(expand=True, padx=50, pady=50)
    
    root.mainloop()
