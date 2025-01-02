from tkinter import *
import random
import csv
from tkinter import messagebox

# from fontTools.ttLib.tables.otConverters import converterMapping

FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_list.extend(password_letter)
    password_symbols = [random.choice(symbols)for _ in range(nr_symbols)]
    password_list.extend(password_symbols)
    password_numbers =[random.choice(numbers)for _ in range(nr_numbers)]
    password_list.extend(password_numbers)
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_csv():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Check if any field is empty
    if not website or not email or not password:
        messagebox.showwarning("Warning", "Please fill out all fields")
        return

    # Save data to a csv file
    with open("data.csv",mode="a" ,newline = "") as file:
        writer = csv.writer((file))
        writer.writerow([website,email,password])

    #clear entries
    website_entry.delete(0, END)
    password_entry.delete(0,END)

    #Success message
    messagebox.showinfo("Sucess","Details saved successfully")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx= 20,pady =20)

#Create Image
logo_img = PhotoImage(file = "logo.png")
canvas = Canvas(width= 200 ,height=200,highlightthickness=0)
canvas.create_image(100,100, image = logo_img)
canvas.grid(column =1, row =0)

# Create Website Label
website = Label(text ="Website:",font=(FONT_NAME,12))
website.grid(column = 0 , row = 1)
# Website Entry
website_entry = Entry(width=35)
website_entry.grid(column = 1, row =1,columnspan =2)

#Create Email/Username Label
email = Label(text = "Email/Username:",font=(FONT_NAME,12))
email.grid(column = 0, row = 2)
#Email Entry
email_entry = Entry(width=35)
email_entry.grid(column = 1, row = 2,columnspan =2)
email_entry.insert(0,"abc@gmail.com")

# Create Password Label
password = Label(text ="Password:", font=(FONT_NAME,12))
password.grid(column = 0, row = 3)
# Password Entry
password_entry = Entry(width=20)
password_entry.grid(column =1 , row =3,columnspan =1)
# Generate password button
generate_password = Button(text="Generate Password",command= password_generator)
generate_password.grid(column= 2, row =3)
# Add button
add_button = Button(text = "Add",width=36,command= save_to_csv)
add_button.grid(column = 1, row = 4,columnspan =2)

window.mainloop()