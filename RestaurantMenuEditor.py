import csv
from tkinter import *
from tkinter import messagebox

def write_to_csv():
    item = item_entry.get()
    price = price_entry.get()

    # Prepare the data for the CSV
    data = [[item, price]]

    # Write the data to a CSV file
    with open('menu.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
        
        # Clear the entry fields once submit button has been clicked
    item_entry.delete(0, END)
    price_entry.delete(0, END)

    messagebox.showinfo("Success", "Menu Updated!")

# main window
root = Tk()

# entry fields
Label(root, text="Enter Food Name:").pack()
item_entry = Entry(root)
item_entry.pack()

Label(root, text="Enter Food Price:").pack()
price_entry = Entry(root)
price_entry.pack()

# submit button
submit_button = Button(root, text="Submit", command=write_to_csv)
submit_button.pack()

# Start the main loop
root.mainloop()
