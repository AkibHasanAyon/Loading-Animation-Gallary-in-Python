import tkinter as tk
import math

class LoadingVortex(tk.Canvas):
    def __init__(self, parent, width=300, height=300, **kwargs):
        super().__init__(parent, width=width, height=height, bg='white', highlightthickness=0, **kwargs)
        self.cx = width / 2
        self.cy = height / 2
        
        # Colors extracted from your provided image: 
        # Red, Orange, Light Green, Dark Green
        self.colors = ["#e15b64", "#f8b26a", "#abbd81", "#849b87"]
        
        # Customizable vortex parameters to tweak shapes
        self.R_outer = width * 0.35      # Distance from center to outer tip
        self.R_inner = width * 0.08      # Distance from center to inner tip
        self.max_thickness = width * 0.12 # Peak thickness of each fin
        self.sweep_angle = -150          # How far the fin wraps around (degrees)
        self.rotation_speed = 4          # Rotation speed (degrees per frame)
        self.current_angle = 0           # Starting rotation state
        
        self.animate()

    def get_fin_polygon(self, start_angle):
        points = []
        steps = 40  # Number of segments for the curve (higher = smoother)
        
        # Outer curve
        for i in range(steps + 1):
            t = i / steps
            
            # Linear angle progression
            angle = start_angle + t * self.sweep_angle
            
            # Non-linear radius progression to make it look more fluid
            radius_t = math.pow(t, 0.8)
            r_base = self.R_outer * (1 - radius_t) + self.R_inner * radius_t
            
            # Thickness uses a sine wave so we get sharp points at both ends
            thickness = self.max_thickness * math.sin(t * math.pi)
            
            r_outer = r_base + thickness * 0.5
            x = self.cx + r_outer * math.cos(math.radians(angle))
            y = self.cy - r_outer * math.sin(math.radians(angle))
            points.append((x, y))
            
        # Inner curve (walk backwards back to the start point)
        for i in range(steps, -1, -1):
            t = i / steps
            angle = start_angle + t * self.sweep_angle
            
            radius_t = math.pow(t, 0.8)
            r_base = self.R_outer * (1 - radius_t) + self.R_inner * radius_t
            thickness = self.max_thickness * math.sin(t * math.pi)
            
            r_inner = r_base - thickness * 0.5
            x = self.cx + r_inner * math.cos(math.radians(angle))
            y = self.cy - r_inner * math.sin(math.radians(angle))
            points.append((x, y))
            
        return points

    def draw(self):
        self.delete("all")
        
        for i in range(4):
            # 4 fins, spaced equally by 90 degrees
            base_angle = self.current_angle + i * 90
            
            # Fetch coordinates for the polygon
            poly_points = self.get_fin_polygon(base_angle)
            flat_points = [coord for pt in poly_points for coord in pt]
            
            # create_polygon draws the curve filled with the given color
            self.create_polygon(flat_points, fill=self.colors[i], outline="", smooth=False)

    def animate(self):
        # Update rotation (subtracting to rotate clockwise)
        self.current_angle = (self.current_angle - self.rotation_speed) % 360
        self.draw()
        
        # Schedule next frame (~60 FPS)
        self.after(16, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Vortex Loading Spinner")
    root.configure(bg='white')
    
    # # Loading label above the animation
    # lbl = tk.Label(root, text="Loading...", font=("Helvetica", 18, "bold"), bg="white", fg="#e15b64")
    # lbl.pack(pady=(30, 0))
    
    # Create the animated canvas
    spinner = LoadingVortex(root, width=300, height=300)
    spinner.pack(padx=30, pady=20)
    
    # # Subtext label
    # inst = tk.Label(root, text="Built entirely from scratch in Tkinter \nNo external libraries needed!", font=("Arial", 10, "italic"), bg="white", fg="#a0a0a0")
    # inst.pack(pady=(0, 30))
    
    root.mainloop()
