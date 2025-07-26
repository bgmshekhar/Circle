import keyboard
from config import HOTKEY

def start_hotkey_listener(callback):
    """
    Starts listening for the global hotkey and triggers the callback function.
    """
    keyboard.add_hotkey(HOTKEY, callback)
    print(f"Hotkey '{HOTKEY}' is set. Press it to trigger the callback.")

if __name__ == '__main__':
    # This is a placeholder for testing the hotkey listener directly.
    # For example, you can have a simple callback that prints a message.
    def example_callback():
        print("Hotkey pressed! Executing callback.")

    print("Starting hotkey listener for testing...")
    start_hotkey_listener(example_callback)