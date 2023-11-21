import tkinter as tk
import csv

next_window = None

def next_page():
    # Close the current window
    window.withdraw()

    # Create the next page window
    global next_window
    next_window = tk.Toplevel()

    # Read the CSV file and create the data structure
    menu_data = read_csv_file("menu.csv")

    # Display the data structure
    display_data_structure(menu_data)

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

def display_data_structure(data):
    # Create labels for each row and column
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            button = tk.Button(next_window, text=cell, command=lambda text=cell: display_value(text))
            button.grid(row=i, column=j)

def display_value(text):
    # clear any existing value label
    for widget in next_window.winfo_children():
        if isinstance(widget, tk.Label) and widget.winfo_y() == next_window.winfo_height() - 1:
            widget.destroy()
            
    # Create a label to display the value
    value_label = tk.Label(next_window, text=text)
    value_label.grid(row=next_window.winfo_height(), columnspan=len(next_window.grid_size()))
    
# Create the main window
window = tk.Tk()

# Create a button to go to the next page
button = tk.Button(window, text="Next Page", command=next_page)
button.pack()

# Start the Tkinter event loop
window.mainloop()