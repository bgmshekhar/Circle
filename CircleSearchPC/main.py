import tkinter as tk
import keyboard
import hotkey_handler
import overlay_selector
import ocr_engine
import screenshot

def on_hotkey_press():
    """
    Callback function to be executed when the hotkey is pressed.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window

    # Create a Toplevel window for the overlay
    overlay_window = tk.Toplevel(root)
    overlay = overlay_selector.OverlaySelector(overlay_window)
    
    coordinates = overlay.start_selection()

    if coordinates:
        screenshot_path = screenshot.take_screenshot(region=coordinates)
        print(f"Screenshot saved to: {screenshot_path}")

        # Call OCR engine and print the extracted text
        extracted_text = ocr_engine.extract_text(screenshot_path)
        print("Extracted Text:")
        print(extracted_text)

    root.destroy() # Clean up the root window

def main():
    """
    Main function to initialize and run the application.
    """
    hotkey_handler.start_hotkey_listener(on_hotkey_press)
    keyboard.wait()

if __name__ == "__main__":
    main()