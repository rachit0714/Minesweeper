from Point import Point
from tkinter import Frame

class MyFrame:
    def __init__(self, color, width, height, origin):
        self.color = color
        self.width = width
        self.height = height
        self.origin = origin
        self.frame = None

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_color(self):
        return self.color

    def draw_frame(self, root):
        self.frame = Frame(root, bg=self.color, width=self.width, height=self.height)
        self.frame.place(x=self.origin.x,y=self.origin.y)

    def get_frame(self):
        return self.frame

    def __str__(self):
        return f"A {self.color} frame at {self.origin}"
        
