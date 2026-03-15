import tkinter as tk
import math

class DotSpinner(tk.Canvas):
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
        colors = ["#F38BA8", "#FAB387", "#F9E2AF", "#A6E3A1", "#89DCEB", "#89B4FA", "#CBA6F7", "#F5C2E7"]
        for i in range(8):
            angle = i * 45 + (t * 2) # Adding rotation
            r = 60
            x = cx + r * math.cos(math.radians(angle))
            y = cy + r * math.sin(math.radians(angle))
            active = (t // 3) % 8 == i
            if active:
                self.create_oval(x-15, y-15, x+15, y+15, fill=colors[i], outline="")
                self.create_oval(cx-5, cy-5, cx+5, cy+5, fill=colors[i], outline="") # Center dot echoes
            else:
                self.create_oval(x-8, y-8, x+8, y+8, fill="#3A3A4A", outline="")

        self.after(30, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Dot Spinner Loader")
    root.configure(bg='#1E1E2E')
    root.geometry("400x400")
    
    lbl = tk.Label(root, text="Dot Spinner Loader", bg="#1E1E2E", fg="#A6ACCD", font=("Arial", 16, "bold"))
    lbl.pack(pady=20)
    
    spinner = DotSpinner(root, width=300, height=300)
    spinner.pack(expand=True)
    root.mainloop()
