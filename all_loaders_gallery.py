import tkinter as tk
from tkinter import ttk
import os
import importlib.util
import sys

class UnifiedGallery(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Master Loading Animation Gallery (80+ Loaders)")
        self.configure(bg="#0B0E14")
        self.geometry("1400x900")
        
        # Main Layout
        self.canvas = tk.Canvas(self, bg="#0B0E14", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#0B0E14")
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        # Bind mouse wheel
        self.bind_all("<MouseWheel>", self._on_mousewheel)
        
        self.loaders_data = []
        self.load_all_loaders()
        self.setup_ui()
        
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def load_all_loaders(self):
        base_path = "/home/akib/Desktop/IIT/animation"
        categories = [
            ("Premium (Geometric/Eye-Catching)", "premium_loaders"),
            ("Professional (Formal)", "professional_loaders"),
            ("Modern (Funky/Neon)", "modern_loaders"),
            ("Classic (Standard)", "classic_loaders"),
            ("Basic (Minimal)", "basic_loaders")
        ]
        
        for cat_name, folder in categories:
            full_path = os.path.join(base_path, folder)
            if not os.path.isdir(full_path):
                continue
                
            cat_group = {"name": cat_name, "folder": folder, "classes": []}
            sys.path.append(full_path)
            
            files = sorted([f for f in os.listdir(full_path) if f.endswith(".py") and not f.startswith("__")])
            for f in files:
                module_name = f[:-3]
                try:
                    spec = importlib.util.spec_from_file_location(module_name, os.path.join(full_path, f))
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    
                    # Find the class inside the module (usually matches the CamelCase version or is the only class)
                    for attribute_name in dir(module):
                        attribute = getattr(module, attribute_name)
                        if isinstance(attribute, type) and issubclass(attribute, tk.Canvas) and attribute != tk.Canvas:
                            cat_group["classes"].append({
                                "class": attribute,
                                "name": module_name.replace("_", " ").title()
                            })
                            break
                except Exception as e:
                    print(f"Error loading {f}: {e}")
            
            self.loaders_data.append(cat_group)

    def setup_ui(self):
        for group in self.loaders_data:
            # Header
            header = tk.Label(
                self.scrollable_frame, text=group["name"], 
                bg="#1E222A", fg="white", font=("Arial", 18, "bold"),
                pady=15, anchor="w", padx=20
            )
            header.pack(fill="x", pady=(20, 10))
            
            grid_frame = tk.Frame(self.scrollable_frame, bg="#0B0E14")
            grid_frame.pack(fill="x", padx=10)
            
            cols = 4 # 4 loaders per row
            for i, loader in enumerate(group["classes"]):
                r, c = i // cols, i % cols
                
                cell = tk.Frame(grid_frame, bg="#161B22", bd=0, highlightthickness=1, highlightbackground="#30363D")
                cell.grid(row=r, column=c, padx=10, pady=10, sticky="nsew")
                
                # Title
                lbl = tk.Label(cell, text=loader["name"], bg="#161B22", fg="#8B949E", font=("Arial", 9, "bold"))
                lbl.pack(side="bottom", pady=5)
                
                # Instance
                try:
                    # We create the canvas instance. We need to handle sizing carefully.
                    # The loaders were designed for 300x300 or 400x400. We'll show them at 200x200 scaled.
                    # NOTE: Since loaders are raw Tkinter with hardcoded cx/cy, we rely on them centering themselves.
                    l_inst = loader["class"](cell, width=220, height=220)
                    l_inst.configure(bg="#161B22")
                    # If the loader has a specific bg in its code, it might override this, 
                    # but most of my templates used the bg parameter in __init__.
                    l_inst.pack(expand=True, padx=10, pady=10)
                except Exception as e:
                    err_lbl = tk.Label(cell, text="Error", fg="red", bg="#161B22")
                    err_lbl.pack()

if __name__ == "__main__":
    app = UnifiedGallery()
    app.mainloop()
