import tkinter as tk

canvas_width = 400
canvas_height = 400
cell_size = 40
eraser_size = 20

def erase_objects(canvas, eraser, x, y):
    overlapping = canvas.find_overlapping(x, y, x + eraser_size, y + eraser_size)
    for obj in overlapping:
        if obj != eraser:
            canvas.itemconfig(obj, fill="white")

def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack()

    # Create the grid
    for row in range(0, canvas_height, cell_size):
        for col in range(0, canvas_width, cell_size):
            canvas.create_rectangle(col, row, col + cell_size, row + cell_size, fill="blue")

    # Create the eraser
    eraser = canvas.create_rectangle(0, 0, eraser_size, eraser_size, fill="pink")

    def on_mouse_move(event):
        canvas.coords(eraser, event.x, event.y, event.x + eraser_size, event.y + eraser_size)
        erase_objects(canvas, eraser, event.x, event.y)

    canvas.bind("<Motion>", on_mouse_move)
    root.mainloop()

if __name__ == "__main__":
    main()