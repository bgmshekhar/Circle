import tkinter as tk

class OverlaySelector:
    def __init__(self, master):
        self.master = master
        self.master.attributes("-fullscreen", True)
        self.master.attributes("-alpha", 0.3)
        self.master.overrideredirect(True)
        self.master.wait_visibility(self.master)

        self.canvas = tk.Canvas(self.master, cursor="cross", bg="gray")
        self.canvas.pack(fill="both", expand=True)

        self.rect = None
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        self.selection_done = tk.BooleanVar()
        
        self.master.bind("<Escape>", self._on_escape)

    def _on_escape(self, event=None):
        """Handles Escape key press to cancel selection."""
        self.selection_done.set(True)
        self.master.destroy()

    def _on_mouse_press(self, event):
        """Handles mouse press event."""
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        if not self.rect:
            self.rect = self.canvas.create_rectangle(
                self.start_x, self.start_y, self.start_x, self.start_y, 
                outline="red", width=2, fill="white"
            )
        # Change canvas transparency to make rectangle more visible
        self.master.attributes("-alpha", 0.1)


    def _on_mouse_drag(self, event):
        """Handles mouse drag event."""
        if self.rect and self.start_x is not None and self.start_y is not None:
            self.end_x = self.canvas.canvasx(event.x)
            self.end_y = self.canvas.canvasy(event.y)
            self.canvas.coords(self.rect, self.start_x, self.start_y, self.end_x, self.end_y)

    def _on_mouse_release(self, event):
        """Handles mouse release event."""
        if self.start_x is not None and self.start_y is not None:
            self.end_x = self.canvas.canvasx(event.x)
            self.end_y = self.canvas.canvasy(event.y)
            self.selection_done.set(True)
            self.master.destroy()

    def start_selection(self):
        """Starts the region selection process and returns the selected coordinates."""
        self.canvas.bind("<ButtonPress-1>", self._on_mouse_press)
        self.canvas.bind("<B1-Motion>", self._on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self._on_mouse_release)
        
        self.master.focus_force()
        self.master.wait_variable(self.selection_done)

        if self.start_x is not None and self.end_x is not None and self.start_y is not None and self.end_y is not None:
            left = int(min(self.start_x, self.end_x))
            top = int(min(self.start_y, self.end_y))
            right = int(max(self.start_x, self.end_x))
            bottom = int(max(self.start_y, self.end_y))
            
            # Check for a minimal size to avoid accidental clicks
            if right - left > 5 and bottom - top > 5:
                return (left, top, right, bottom)
        return None

if __name__ == "__main__":
    # This block demonstrates how to use the OverlaySelector
    def run_selection():
        root = tk.Tk()
        root.withdraw()  # Hide the main window

        selector_window = tk.Toplevel(root)
        selector = OverlaySelector(selector_window)
        
        coordinates = selector.start_selection()
        
        if coordinates:
            print(f"Selected coordinates: {coordinates}")
        else:
            print("Selection cancelled or invalid.")
            
        root.quit()

    run_selection()