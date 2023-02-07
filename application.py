from tkinter import *
from Point import Point
from MyFrame import MyFrame
from Cell import Cell
from constants import *

root = Tk()
# Override the window settings

frames = []

def config_root(width, height):
    root.configure(bg="black")
    root.geometry(str(width) + "x" + str(height))
    root.title("Minesweeper")
#    root.resizable(False,False)


def set_frames(w,h):
    top_frame = MyFrame("red", w,h//4,Point(0,0))
    left_frame = MyFrame("blue",w//4,h*0.75,Point(0,h//4))
    center_frame = MyFrame("green",w*0.75,h*0.75,Point(w//4,h//4))
    grid_frame = MyFrame("black", w*0.75,h*0.75,Point(w//4,h//4))
    frames.append(top_frame)
    frames.append(left_frame)
    frames.append(center_frame)
    frames.append(grid_frame)

    for frame in frames:
        frame.draw_frame(root)

def set_grid(size):
    for c in range(size):
        for r in range(size):
            cell = Cell()
            cell.draw(frames[3].get_frame(),Point(r,c))

def main():
    config_root(window_width, window_height)
    set_frames(window_width, window_height)
    set_grid(grid_size)
    Cell.set_mines(mines_count)    
    # Run the window
    root.mainloop()

if __name__ == "__main__":
    main()

'''
Objects needed:
Point - used to set where cells are located for reference

Cell - Will be either a mine or regular
     - text will say "boom" on a mine or show number of adjacent mines
     - if 0 adjacent mines then it will check how many mines are adjacent to those
     - flag option is given if user wants to track positions they believe a mine to be

Frame - Three main frames, Top, Left, Center, takes in color, width, height, and frame starting point
      - TopFrame will give user option to select difficulty and start/restart the game
      - LeftFrame will display how many cells are remaining along with how many potential mines are unflagged
      - CenterFrame will display all the buttons for mines

- Cells will be able to draw themselves but will be called by TopFrame
- CenterFrame will keep a list of Cells and will end the game when a bomb goes off or when all free cells are clicked





'''
