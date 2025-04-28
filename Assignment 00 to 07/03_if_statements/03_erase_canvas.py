from tkinter import Canvas
import time

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser):
    """Erase blue squares that the eraser touches."""
    mouse_x = canvas.get_mouse_x()
    mouse_y = canvas.get_mouse_y()
    
    # Define eraser's bounding box
    left_x = mouse_x
    top_y = mouse_y
    right_x = mouse_x + ERASER_SIZE
    bottom_y = mouse_y + ERASER_SIZE
    
    # Find all items touching the eraser
    overlapping = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
    
    for item in overlapping:
        if item != eraser:
            canvas.set_color(item, 'white')

def main():
    # Set up the canvas
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Create a grid of blue squares
    for y in range(0, CANVAS_HEIGHT, CELL_SIZE):
        for x in range(0, CANVAS_WIDTH, CELL_SIZE):
            canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, 'blue')
    
    # Wait for first click to place the eraser
    canvas.wait_for_click()
    click_x, click_y = canvas.get_last_click()
    
    eraser = canvas.create_rectangle(
        click_x, click_y, 
        click_x + ERASER_SIZE, click_y + ERASER_SIZE, 
        'pink'
    )
    
    # Main loop: move eraser with mouse and erase
    while True:
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        canvas.moveto(eraser, mouse_x, mouse_y)
        erase_objects(canvas, eraser)
        time.sleep(0.05)

if __name__ == '__main__':
    main()
