
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

import smtplib
#import getpass
from tkinter import messagebox

def is_entry_empty(entry_widget):
    text = entry_widget.get("1.0", 'end-1c')
    return not bool(text)

import sqlite3

def find_user_by_email(sEmail):
    conn = sqlite3.connect(r'C:\Users\Kai\Desktop\Project\Language_Learner.sqlite3')
    cursor = conn.cursor()

    cursor.execute("SELECT Username, Password FROM Users WHERE Email = ?", (sEmail,))
    
    result = cursor.fetchone()
    
    conn.close()
    
    if result is not None:
        return result  #(username, password) together
    else:
        return None  #No user 

def clear_entry_box():
    entry_1.delete("1.0", 'end-1c')
    
def SendEmail():
    if is_entry_empty(entry_1):
        messagebox.showerror("Error", "Entry Field is empty. Please ensure that you have inputted a valid email address.")
    else:
        sEmailInput = entry_1.get("1.0", 'end-1c')

        sData = find_user_by_email(sEmailInput)

        if sData:
            sUsername, sPassword = sData
            messagebox.showinfo("Information", "User account has been found and login details has been sent to your email. Check your inbox.")
            clear_entry_box()
            
            gmail_user = 'languagelearner314@gmail.com'
            gmail_password = 'pnva wldh ppkt kqsd'
 
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587

            try:
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()  

                server.login(gmail_user, gmail_password)

                to_email = sEmailInput
                subject = 'Account Recovery'
                body = f'As requested, here are your account details:\nUsername: {sUsername}\nPassword: {sPassword}'

                email_text = f'Subject: {subject}\n\n{body}'

                server.sendmail(gmail_user, to_email, email_text)

                #print('Email sent successfully.')

            except Exception as e:
                print(f'Error: {str(e)}')

            finally:
                server.quit()

        else:
            messagebox.showerror("Error", "No user account has been found attached to the provided email.")



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Kai\Desktop\Project\Screen 4 - Forgot Password\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the x and y coordinates to center the window
x = (screen_width - 640) // 2  # 640 is the window width
y = (screen_height - 320) // 2  # 320 is the window height

# Set the window geometry
window.geometry("640x320+{}+{}".format(x, y))

#window.geometry("640x320")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 320,
    width = 640,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    235.0,
    28.0,
    anchor="nw",
    text="Sign in details",
    fill="#4A1BD0",
    font=("RobotoRoman SemiBold", 20 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    336.0,
    154.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=185.0,
    y=137.0,
    width=302.0,
    height=33.0
)

canvas.create_text(
    216.0,
    119.0,
    anchor="nw",
    text="Input email address attached to account",
    fill="#696969",
    font=("MontserratRoman Light", 11 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=SendEmail,
    relief="flat"
)
button_1.place(
    x=176.0,
    y=195.0,
    width=320.0,
    height=35.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    320.0,
    293.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    109.0,
    46.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    520.0,
    42.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    336.0,
    180.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    452.0,
    125.0,
    image=image_image_5
)
window.resizable(False, False)
window.mainloop()
