from tkinter import *
import os
from tkinter import messagebox
import random
import pyperclip 

def generate() :

  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = [ '#', '$', '&',  '*',]

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)

  password_letters = [random.choice(letters) for _  in range(nr_letters)]
  password_symbols =  [random.choice(symbols) for _  in range(nr_symbols)]
  password_numbers =  [random.choice(numbers) for _  in range(nr_numbers)]

  password_list = password_letters + password_numbers + password_symbols
  random.shuffle(password_list)


  password = "".join(password_list)
  Password_entry.delete(0, END)
  Password_entry.insert(0, password)
  pyperclip.copy(password)            
  

  

# Function to save data to file
def save():
    website_value = website_entry.get()
    email_value = Email_entry.get()
    password_value = Password_entry.get()

    if len(website_value) == 0 or len(password_value) == 0 :
        messagebox.showinfo(title="Oops" , message="Please make sure you haven't left any field empty.")
    else :
      is_ok = messagebox.askokcancel(title=website_value, message=f"These are the details you submitted.\nEmail: {email_value}\nPassword: {password_value}\nIs it okay to save? ")
      if is_ok:
          try:
              with open("data.txt", "a") as data_file:
                  data_file.write(f"{website_value} | {email_value} | {password_value}\n")
              print("Data saved successfully.")
          except Exception as e:
              print(f"Error saving data: {e}")

          # Clearing the entry fields after saving
          website_entry.delete(0, END)
          Password_entry.delete(0, END)
          Email_entry.delete(0, END)

# UI Setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas and Logo
canvas = Canvas(width=200, height=200)
canvas.grid(column=1, row=0)
logo = PhotoImage(file="C:\\Users\\Welcome\\OneDrive\\Desktop\\Python\\Mini Project\\TKINTER\\My-Passwords\\logo.png")
canvas.create_image(100, 100, image=logo)

# Labels and Entries
website = Label(text="Website:")
website.grid(column=0, row=1)
website_entry = Entry(width=53)
website_entry.grid(column=1, row=1, columnspan=4)
website_entry.focus()

Password = Label(text="Password:")
Password.grid(column=0, row=3)
Password_entry = Entry(width=33)
Password_entry.grid(column=1, row=3)

Email = Label(text="Email/Username:")
Email.grid(column=0, row=2)
Email_entry = Entry(width=53)
Email_entry.grid(column=1, row=2, columnspan=4)
Email_entry.insert(0, "harxhit@gmail.com")  # You can remove it or change it

# Buttons
button1 = Button(text="Generate Password" , command= generate)
button1.grid(column=3, row=3)

button2 = Button(text="Add", width=16, command=save)
button2.grid(column=1, row=4, columnspan=2)

window.mainloop()