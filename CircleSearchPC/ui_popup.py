import tkinter

class UIPopup:
    def __init__(self):
        """Initializes the Tkinter window."""
        self.window = tkinter.Tk()
        self.window.withdraw() # Hide the main window. A Toplevel will be used for the popup.

    def show_popup(self, text):
        """
        Shows a popup window with the extracted text and action buttons.
        """
        popup = tkinter.Toplevel(self.window)
        popup.title("CircleSearchPC")

        text_label = tkinter.Label(popup, text=text, padx=20, pady=20)
        text_label.pack()

        button_frame = tkinter.Frame(popup)
        button_frame.pack(pady=10)

        google_button = tkinter.Button(button_frame, text="Google Search")
        google_button.pack(side="left", padx=5)

        translate_button = tkinter.Button(button_frame, text="Translate")
        translate_button.pack(side="left", padx=5)

        gemini_button = tkinter.Button(button_frame, text="Ask Gemini")
        gemini_button.pack(side="left", padx=5)

        copy_button = tkinter.Button(button_frame, text="Copy Text")
        copy_button.pack(side="left", padx=5)

        popup.attributes("-topmost", True)
        # The main application loop will handle updating the window.