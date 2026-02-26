from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
#----------------------------------SEARCH PASSWORD------------------------------------#
def search_password():
    try:
        with open("password.json", "r") as file:
            content= json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "No data file found")

    else:
        try:
            website_name = website_entry.get()
            website = content[website_name]
        except KeyError:
            messagebox.showerror("Error", "No data for this website")
        else:
            email_id = website["email"]
            password = website["password"]
            print(f"Website Name: {website_name} , email: {email_id}, pass:{password}")
            messagebox.showinfo(website_name, f"Email : {email_id} \nPassword:{password}")
    finally:
        website_entry.delete(0, "end")


#---------------------------------------PASSWORD GENERATOR-------------------------------#

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)


    password = [random.choice(letters) for i in range(nr_letters)]
    password += [random.choice(symbols) for i in range(nr_symbols)]
    password += [random.choice(numbers) for i in range(nr_numbers)]

    random.shuffle(password)

    final_password = "".join(password)
    print("Your password is:", final_password)
    pass_entry.delete(0, "end")
    pass_entry.insert(0,final_password)
    pyperclip.copy(final_password)

#---------------------------------------SAVE PASSWORD -------------------------------#
def save_password():
    website_name = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    new_data ={
        website_name: {
            "email": email,
            "password": password
        }
    }
    if len(website_name) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror("Oops", "Please don't leave any fields empty!")
    else:
        #messagebox.showinfo(title="Password Manager",message = "Your password is " + password)
        is_ok = messagebox.askokcancel(title= website_name, message= f"These are the details entered: \n "
                                                         f"Email : {email} \n"
                                                         f"Your password is  {password}\n "
                                                         f"Is it ok to save?" )

        if is_ok:
            # with open("password.txt","a") as file:
            #     file.write(f"{website_name} | {email} | {password}\n")
            try:
                with open("password.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("password.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                #Update
                data.update(new_data)
                with open("password.json", "w") as file:
                    #Write
                    json.dump(data, file, indent= 4)
            finally:
                website_entry.delete(0, "end")
                #email_entry.delete(0, "end")
                pass_entry.delete(0, "end")
                website_entry.focus()

#---------------------------------------UI SETUP-------------------------------#
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")


#---------------------------------------
logo = PhotoImage(file = "logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0, bg="white")
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)
#-------------------------
#Labels
website_label = Label(text="Website:", bg="white")
email_label = Label(text="Email/Username:", bg="white")
pass_label = Label(text="Password:", bg="white")

website_label.grid(row=1,column=0)
email_label.grid(row=2,column=0)
pass_label.grid(row=3,column=0)


#Entry
website_entry = Entry(width=35, bg="white")
website_entry.focus()
email_entry = Entry(width=35, bg="white")
email_entry.insert(0,"aarthimcbe@gmail.com")
pass_entry = Entry(width=21, bg="white")

#sticky" parameter, the EW part is the compass directions (E)ast and (W)est and
# the sticky basically "sticks" the widget to the edges of the column.
website_entry.grid(row=1,column=1, sticky="EW")
email_entry.grid(row=2,column=1,columnspan = 2, sticky="EW")
pass_entry.grid(row=3,column=1, sticky="EW")


#Buttons
search_button = Button(text="Search", bg="white", width=15, command= search_password)
generate_button = Button(text="Generate Password", bg="white", command= generate_password)
add_button = Button(text="Add", width=36, bg="white", command= save_password)
search_button.grid(row=1,column=2, sticky="E")
generate_button.grid(row=3,column=2, sticky="E")
add_button.grid(row=4,column=1,columnspan = 2, sticky="EW")



window.mainloop()