import tkinter as tk

next_window = None

def next_page():
    
    # Close the current window
    window.withdraw()

    # Create the next page window4
    global next_window
    next_window = tk.Toplevel()

    # Add widgets and layout for the next page
    label = tk.Label(next_window, text="This is the next page")
    label.pack()

    # Add a button to go back to the first window
    back_button = tk.Button(next_window, text="Go Back", command=go_back)
    back_button.pack()

def go_back():
    global next_window

    # Close the current window
    next_window.destroy()
    
    window.deiconify()

window = tk.Tk()

# Create a button widget
button = tk.Button(window, text="Next Page", command=next_page)
button.pack()

# Start the Tkinter event loop
window.mainloop()
