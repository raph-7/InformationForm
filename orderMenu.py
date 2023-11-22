from tkinter import *
import csv
from tkinter import messagebox

class OrderMenuApp:
    def __init__(self):
        self.window = Tk()
        self.window.attributes("-fullscreen", True)
        self.menu_file = 'menu.csv'
        self.billing_labels = self.read_labels_from_csv(self.menu_file)
        self.menu_items = self.read_menu_from_csv(self.menu_file)
        self.entry_widgets, self.total_labels, self.overall_total_label = self.display_billing_labels(self.billing_labels)
        self.display_data_structure(self.menu_items)
        self.display_ui()

    def display_ui(self):
        self.display_labels()
        self.display_buttons()
        self.window.mainloop()

    def display_labels(self):
        titleLabel = Label(self.window, text="Beach Side Restaurant", font="times 30 bold")
        titleLabel.place(x=650, y=20, anchor="center")

        label1 = Label(self.window, text="Menu", font="times 28 bold")
        label1.place(x=1100, y=70)

        billLabel = Label(self.window, text="Order Here", font="times 28 bold")
        billLabel.place(x=70, y=70)

    def display_buttons(self):
        place_order_button = Button(self.window, text="Place Order", width=25, height=3, command=self.display_order_summary)
        place_order_button.place(x=580, y=600)
        place_order_button.configure(bg="red")

        exit_button = Button(self.window, text="Exit", width=20, command=self.window.destroy)
        exit_button.place(x=600, y=700)
        
    def display_order_summary(self):
        summary_window = Toplevel(self.window)
        summary_window.title("Order Summary")

        # Calculate the total price
        total_price = sum([int(entry.get()) * float(item[1]) for entry, item in zip(self.entry_widgets, self.menu_items)])

        # Display the order summary
        summary_label = Label(summary_window, text="Your Order", font="times 20 bold")
        summary_label.pack()

        for entry, item, total_label in zip(self.entry_widgets, self.menu_items, self.total_labels):
            quantity = int(entry.get())
            item_name = item[0]
            item_price = float(item[1])
            total = quantity * item_price

            summary_text = f"{item_name} x {quantity} = {total}"
            summary_item_label = Label(summary_window, text=summary_text)
            summary_item_label.pack()

            total_label.config(text=f"Total Price: {total_price}")
            
        confirm_button = Button(summary_window, text="Confirm Order", command=lambda: self.confirm_order(total_price))
        confirm_button.pack()
        
    def confirm_order(self, total_price):
        # Get the order details
        order_details = []
        for entry, item in zip(self.entry_widgets, self.menu_items):
            quantity = int(entry.get())
            item_name = item[0]
            item_price = float(item[1])
            total = quantity * item_price
            order_details.append([item_name, quantity, total])

        # Write the order details to a CSV file
        order_file = 'order_details.csv'
        with open(order_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Item', 'Quantity', 'Total'])
            writer.writerows(order_details)
            writer.writerow(['', '', f'Total Price: {total_price}'])

            messagebox.showinfo("Order Confirmation", "Order confirmed!")


    def display_billing_labels(self, labels):
        entry_values = []
        total_values = []
        for i, label in enumerate(labels):
            label = Label(self.window, text=label, font="times 18")
            label.place(x=20, y=120 + (i * 60))

            entry = Entry(self.window)
            entry.insert(0, "0")
            entry.place(x=20, y=150 + (i * 60))
            entry_values.append(entry)

            total_label = Label(self.window, text="Total: 0", font="times 12")
            total_label.place(x=200, y=150 + (i * 60))
            total_values.append(total_label)

            entry.bind("<KeyRelease>", lambda event, index=i: self.update_total(event, index, entry_values, total_values))

        overall_total_label = Label(self.window, text="Overall Total: 0", font="times 12")
        overall_total_label.place(x=600, y=300 + (i * 60))

        return entry_values, total_values, overall_total_label

    def update_total(self, event, index, entry_values, total_values):
        try:
            amount = int(entry_values[index].get())
            if amount < 11:
                price = self.get_multiplier()[index]
                total = amount * price
                total_values[index].config(text="Total: Shs " + str(total))

                overall_total = sum(int(entry.get()) * self.get_multiplier()[i] for i, entry in enumerate(entry_values))
                self.overall_total_label.config(text="Overall Total: Shs " + str(overall_total))
            else:
                entry_values[index].delete(0, END)
                total_values[index].config(text="Total: Shs 0")
        except ValueError:
            total_values[index].config(text="Total: Shs 0")

    def read_menu_from_csv(self, file_path):
        menu_items = []
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                menu_items.append((row[0], row[1]))
        return menu_items

    def display_data_structure(self, data):
        for i, item in enumerate(data):
            if len(item) >= 2:
                label = Label(self.window, text=f"{item[0]} - {item[1]}", font="times 18")
                label.place(x=1100, y=160 + (i * 40))
            else:
                print(f"Invalid data structure at index {i}: {item}")

    def read_labels_from_csv(self, file_path):
        billing_labels = []
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                billing_labels.append(row[0])
        return billing_labels

    def get_multiplier(self):
        prices = []
        with open(self.menu_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) >= 2:
                    price = float(row[1])
                    prices.append(price)
        return prices

if __name__ == "__main__":
    app = OrderMenuApp()
