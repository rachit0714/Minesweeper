from tkinter import Button
from Point import Point
import random
from constants import *

class Cell:
    all = []
    free_cells = grid_size * grid_size
    mines_left = 0
    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self.flag = False
        self.clicked = False
        self.btn = None
        self.where = None

    def get_position(self, axis="xy"):
        if axis == "x":
            return self.where.x
        elif axis == "y":
            return self.where.y
        elif axis == "xy":
            return [self.where.x, self.where.y]

    def left_clicked(self, event):
        if not (self.clicked or self.flag):
            if self.is_mine:
                self.show_mine()
            else:
                self.show_cell()

    def show_mine(self):
        self.clicked = True
        self.btn.configure(text="BOOM")
        for cell in Cell.all:
            if not cell.clicked:
                if cell.is_mine and (not cell.flag):
                    cell.show_mine()
                else:
                    if cell.flag:
                        cell.btn.configure(text="X")
                    else:
                        cell.show_cell()
                

    def show_cell(self):
        Cell.free_cells -= 1
        self.clicked = True
        mines = self.nearby_mines()
        self.btn.configure(text=str(len(mines)))
        if len(mines) == 0:
            for cell in self.surronding_cells():
                if not cell.clicked:
                    cell.show_cell()

    def surronding_cells(self):
        sur_cells = []
        position = self.get_position()
        for i in range(-1,2):
            for j in range(-1,2):
                x = position[0] + j
                y = position[1] + i
                if (in_range(x) and in_range(y)):
                    row = grid_size * y
                    p = row + x
                    sur_cells.append(Cell.all[p])
        return sur_cells
    

    def right_clicked(self, event):
        if not self.clicked:
            self.flag = not self.flag
            if self.flag:
                self.btn.configure(text="FLAG")
                Cell.mines_left += 1
            else:
                Cell.mines_left -= 1
                self.btn.configure(text="")

    def draw(self, frame, where):
        self.where = where
        self.btn = Button(frame, width=(3*window_width)//(40*(grid_size)), height=window_height//(30*grid_size))
        self.btn.grid(column=where.x, row=where.y)
        self.btn.bind('<Button-1>', self.left_clicked)
        self.btn.bind('<Button-3>', self.right_clicked)
        Cell.all.append(self)
    '''
        def draw_button(self, frame, where):
            self.where = where
            self.btn = Button(
                frame,
                width = 8, height = 2
                )
            self.btn.grid(column=where.x,row=where.y)
            self.btn.bind('<Button-1>', self.left_clicked)
            self.btn.bind('<Button-3>', self.right_clicked)
            Cell.all[where.tuppulate()] = self
    '''

    def nearby_mines(self):
        mines = []
        position = self.get_position()
        sur_cells = self.surronding_cells()
        for c in sur_cells:
            if c.is_mine:
                mines.append(c)
        return mines

    '''
        00 01 02 03
        10 11 12 13
        20 21 22 23
        30 31 32 33
             0   1   2   3    4   5   6   7   8  9   10  11  12  13  14  15
            [00, 01, 02, 03, 10, 11, 12, 13, 20, 21, 22, 23, 30, 31, 32, 33]
    
    '''


    
    '''
        def right_clicked(self, event):
            if not self.clicked:
                self.clicked = True
                self.flag = not self.flag
                if self.flag:
                    self.btn.configure(text="flag")
                else:
                    self.btn.configure(text="")
                print("User right clicked")
    '''

    def set_mines(n):
        mines = random.sample(Cell.all, n)
        for m in mines:
            m.is_mine = True


    def __repr__(self):
        return f"Cell({self.where.x}, {self.where.y})"

    def __str__(self):
        if self.is_mine:
            return "A mine"
        return "A Cell"
