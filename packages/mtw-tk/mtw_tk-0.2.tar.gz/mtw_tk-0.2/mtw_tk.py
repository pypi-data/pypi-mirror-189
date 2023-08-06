import tkinter as tk

class MoveTextWidget:
    """A class for moving Tkinter text widgets."""

    def __init__(self, widget):
        """Initialize the class with a Tkinter text widget."""
        self.widget = widget
        self.widget.bind("<Button-1>", self.start_move)
        self.widget.bind("<B1-Motion>", self.move)
        self.widget.bind("<ButtonRelease-1>", self.stop_move)
        self.x = self.y = 0

    def start_move(self, event):
        """Start moving the text widget."""
        self.x = event.x
        self.y = event.y

    def move(self, event):
        """Move the text widget."""
        delta_x = event.x - self.x
        delta_y = event.y - self.y
        x = self.widget.winfo_x() + delta_x
        y = self.widget.winfo_y() + delta_y
        self.widget.place(x=x, y=y)

    def stop_move(self, event):
        """Stop moving the text widget."""
        pass


class StopMoving:
    def __init__(self,widget):
        widget.unbind("<Button-1>")
        widget.unbind("<B1-Motion>")
        widget.unbind("<ButtonRelease-1>")