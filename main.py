import tkinter as tk
from PIL import ImageGrab

class ShapeDrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shape Notepad")

        # Create the canvas
        self.canvas = tk.Canvas(root, width=300, height=300, bg='white')
        self.canvas.pack()

        # Mouse event to draw
        self.canvas.bind('<B1-Motion>', self.draw)

        # Buttons
        self.save_button = tk.Button(root, text="Save Drawing", command=self.save_drawing)
        self.save_button.pack(side=tk.LEFT, padx=10)

        self.clear_button = tk.Button(root, text="Clear", command=self.clear)
        self.clear_button.pack(side=tk.RIGHT, padx=10)

    def draw(self, event):
        x, y = event.x, event.y
        radius = 8  # Size of the brush
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill='black')

    def clear(self):
        self.canvas.delete('all')

    def save_drawing(self):
        # Get coordinates of the canvas
        x = self.root.winfo_rootx() + self.canvas.winfo_x()
        y = self.root.winfo_rooty() + self.canvas.winfo_y()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()

        # Grab the canvas content and save as PNG
        image = ImageGrab.grab().crop((x, y, x1, y1))
        image = image.convert('L')  # Grayscale
        image.save("data/drawing.png")
        print("Drawing saved to data/drawing.png")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeDrawingApp(root)
    root.mainloop()
