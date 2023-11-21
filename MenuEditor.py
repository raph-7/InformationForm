import csv
import tkinter as tk
from tkinter import messagebox

def save_data():
    # Get the data from the entry fields
    data = []
    for i in range(5):
        row = []
        for j in range(5):
            value = entry_fields[i][j].get()
            row.append(value)
        data.append(row)

    # Writing the data to a CSV file
    with open('menu.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(data)

    # Show a success message
    messagebox.showinfo("Success", "Data saved successfully!")

# Create the main window
window = tk.Tk()
window.title("Menu Editor")

# Create a labels for each row
labels = ["Appetizers", "Entrees", "Desserts", "Beverages", "Sides"]
for i, label_text in enumerate(labels):
        label = tk.Label(window, text=label_text)
        label.grid(row=i, column=0)

# Create entry fields for data input
entry_fields = []
for i in range(5):
    row = []
    for j in range(1, 6):
        entry = tk.Entry(window)
        entry.grid(row=i, column=j)
        row.append(entry)
    entry_fields.append(row)

# Create a button to save the data
save_button = tk.Button(window, text="Save", command=save_data)
save_button.grid(row=5, columnspan=6)

# Start the Tkinter event loop
window.mainloop()