#Name 
#Date
#Assignment Title
#version

import csv
from guizero import App, Box, Text, TextBox, PushButton

# This is a function that is called when the submit button is clicked
def submit_data():
    
    # This code fetches the values entered by the user
    name = name_field.value   # name is the variable name for the username
    email = email_field.value # email is the variable name for the email address
    phone = phone_field.value # phone is the variable name for the phone number
    address = address_field.value # address is the variable name for the address
    city = city_field.value # city is the variable name for the city
    state = state_field.value # state is the variable name for the state
    zipCode = zipCode_field.value # zipCode is the variable name for the zip code

    # This code prints the values to the console as the user enters them
    print("Name:", name)
    print("Email:", email)
    print("Phone Number:", phone)
    print("Address:", address)
    print("City:", city)
    print("State:", state)
    print("Zip:", zipCode)
    
    # This code write the values to a csv file once the submit button is clicked
    with open('information.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, phone, address, city, state, zipCode])

# This code creates the Graphical User Interface (GUI) for the form
app = App("Information Form", layout="grid")

# This code creates a box to hold the form
box = Box(app, layout="grid", grid=[0,0])

# This is the title of the form
Text(box, "Please Enter Your Information", size=16, grid=[1,0])

# Code for the name field
Text(box, "Name:", align="left", grid=[0,1])
name_field = TextBox(box, align="left", grid=[0,2,3,1], width=50)

# Code for the first line separator
Text(box, "-"*70, grid=[0,3,3,1])

# Code for the email address field
Text(box, "Email Address:", align="left", grid=[0,4])
email_field = TextBox(box, align="left", grid=[0,5,3,1], width=50)

# Second line separator
Text(box, "-"*70, grid=[0,6,3,1])

# Code for the phone number field
Text(box, "Phone Number:", align="left", grid=[0,7])
phone_field = TextBox(box, align="left", grid=[0,8,3,1], width=50)

#  Third line separator
Text(box, "-"*70, grid=[0,9,3,1])

# Code for the address field
Text(box, "Address:", align="left", grid=[0,10])
address_field = TextBox(box, align="left", grid=[0,11,3,1], width=50)

#  Fourth line separator
Text(box, "-"*70, grid=[0,12,3,1])

# Code for the city field
Text(box, "City:", grid=[0,13])
city_field = TextBox(box, grid=[0,14])

# Code for the state field
Text(box, "State:", grid=[1,13])
state_field = TextBox(box, grid=[1,14])

# Code for the zip code field
Text(box, "Zip:", align="left", grid=[2,13])
zipCode_field = TextBox(box, align="left", grid=[2,14])

# last line separator
Text(box, "-"*70, grid=[0,15,3,1])

# submit button
PushButton(app, text="Submit", command=submit_data, align="left", grid=[0,2])

app.display()