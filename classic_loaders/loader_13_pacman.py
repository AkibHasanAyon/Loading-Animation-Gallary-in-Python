import tkinter as tk
import math

class Pacman(tk.Canvas):
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
        mouth_angle = 45 * abs(math.sin(t * 0.2))
        self.create_arc(cx-60, cy-60, cx+60, cy+60, start=mouth_angle, extent=360 - 2*mouth_angle, fill="#F9E2AF", outline="")
        
        dot_offset = (t * 6) % 60
        for i in range(3):
            x = cx + 120 - dot_offset + i * 60
            if x > cx + 15:
                # Alternate dot colors
                c = "#F5C2E7" if i % 2 == 0 else "#89DCEB"
                self.create_oval(x-12, cy-12, x+12, cy+12, fill=c, outline="")

        self.after(30, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pacman Loader")
    root.configure(bg='#1E1E2E')
    root.geometry("400x400")
    
    lbl = tk.Label(root, text="Pacman Loader", bg="#1E1E2E", fg="#A6ACCD", font=("Arial", 16, "bold"))
    lbl.pack(pady=20)
    
    spinner = Pacman(root, width=300, height=300)
    spinner.pack(expand=True)
    root.mainloop()
