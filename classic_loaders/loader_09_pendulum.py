import tkinter as tk
import math

class Pendulum(tk.Canvas):
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
        angle = math.radians(90 + 50 * math.sin(t * 0.1))
        length = 120
        top_y = cy - 60
        x = cx + length * math.cos(angle)
        y = top_y + length * math.sin(angle)
        
        # Dynamic color based on angle
        color_val = int(abs(math.sin(t * 0.1)) * 255)
        color = f"#{255:02x}{255-color_val:02x}{150:02x}"
        
        self.create_line(cx, top_y, x, y, fill="#A6E3A1", width=6)
        self.create_oval(x-20, y-20, x+20, y+20, fill=color, outline="")
        self.create_oval(cx-8, top_y-8, cx+8, top_y+8, fill="#F38BA8", outline="")

        self.after(30, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pendulum Loader")
    root.configure(bg='#1E1E2E')
    root.geometry("400x400")
    
    lbl = tk.Label(root, text="Pendulum Loader", bg="#1E1E2E", fg="#A6ACCD", font=("Arial", 16, "bold"))
    lbl.pack(pady=20)
    
    spinner = Pendulum(root, width=300, height=300)
    spinner.pack(expand=True)
    root.mainloop()
