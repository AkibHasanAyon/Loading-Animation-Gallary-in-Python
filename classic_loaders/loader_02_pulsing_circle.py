import tkinter as tk
import math

class PulsingCircle(tk.Canvas):
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
        r = 30 + 60 * abs(math.sin(t * 0.1))
        # Gradient effect simulated by drawing multiple layered circles
        for i in range(5, 0, -1):
            curr_r = r * (i / 5.0)
            alpha_color = f"#{int(137 + 10*(5-i)):02x}{int(180 + 10*(5-i)):02x}{int(250 + 10*i):02x}"
            if i == 5: alpha_color = "#89B4FA"
            self.create_oval(cx-curr_r, cy-curr_r, cx+curr_r, cy+curr_r, fill=alpha_color, outline="")

        self.after(30, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pulsing Circle Loader")
    root.configure(bg='#1E1E2E')
    root.geometry("400x400")
    
    lbl = tk.Label(root, text="Pulsing Circle Loader", bg="#1E1E2E", fg="#A6ACCD", font=("Arial", 16, "bold"))
    lbl.pack(pady=20)
    
    spinner = PulsingCircle(root, width=300, height=300)
    spinner.pack(expand=True)
    root.mainloop()
