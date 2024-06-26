
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

import subprocess

import ctypes

def minimize_window(): #Provided by StackOverflow
    # Get a handle to the current window
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    
    # Minimize the window
    ctypes.windll.user32.ShowWindow(hwnd, 6)  # 6 corresponds to SW_MINIMIZE

def restore_window(hwnd):
    # Restore the window
    ctypes.windll.user32.ShowWindow(hwnd, 9)  # 9 corresponds to SW_RESTORE

def run_python_file(file_path):
    try:
        hwnd = ctypes.windll.user32.GetForegroundWindow()  # Get the handle of the current window

        minimize_window()  # Minimize the current window

        # Launch the new script in a new Python process
        process = subprocess.Popen(["python", file_path])

        # Wait for the new script to finish
        out, err = process.communicate()

        # Restore the previous window
        restore_window(hwnd)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except FileNotFoundError:
        print("Error: Python interpreter not found. Please make sure Python is installed.")

def ButtonForgotPassClick_Execution():
    sScriptPath = r'C:\Users\Kai\Desktop\Project\Screen 4 - Forgot Password\build\gui.py'  
    run_python_file(sScriptPath)

def ButtonWelcomeClick_Execution():
    sScriptPath = r'C:\Users\Kai\Desktop\Project\Screen 5 - User Screen\build\gui.py'  
    run_python_file(sScriptPath)

import sqlite3

from tkinter import messagebox

#Algo to check if entries are empty
def is_entry_empty(entry_widget):
    text = entry_widget.get("1.0", 'end-1c')
    return not bool(text)

bFilledEntryBoxes = True

def check_entry_boxes():
    global bFilledEntryBoxes 
    bFilledEntryBoxes = True

    if is_entry_empty(entry_1): 
        bFilledEntryBoxes = False
    if is_entry_empty(entry_2):
        bFilledEntryBoxes = False

def ValidateLoginDetails():
    check_entry_boxes()

    if bFilledEntryBoxes == False:
        messagebox.showerror("Error", "Not all fields are filled out. Please ensure that you have completed all fields.")
    else:
        conn = sqlite3.connect(r'C:\Users\Kai\Desktop\Project\Language_Learner.sqlite3')

        cursor = conn.cursor()

        sUsername = entry_1.get("1.0",'end-1c')
        sPassword = entry_2.get("1.0",'end-1c')

        cursor.execute("SELECT * FROM Users WHERE Username = ? AND Password = ?", (sUsername, sPassword))

        # Fetch the result
        bResult = cursor.fetchone()

        if bResult is not None:
            messagebox.showinfo("Information", "Congratulations. Username and Password combination found in the database. You may proceed to the Learning Area.")
            clear_entry_boxes()
            ButtonWelcomeClick_Execution()
        else:
            messagebox.showerror("Error", "Username & Password combination NOT found in the database.")

        conn.close()

def clear_entry_boxes():
    entry_1.delete("1.0", 'end-1c')
    entry_2.delete("1.0", 'end-1c')
     
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Kai\Desktop\Project\Screen 3 - Login\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the x and y coordinates to center the window
x = (screen_width - 640) // 2  # 640 is the window width
y = (screen_height - 380) // 2  # 320 is the window height

# Set the window geometry
window.geometry("640x380+{}+{}".format(x, y))

#window.geometry("640x380")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 380,
    width = 640,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    269.0,
    31.0,
    anchor="nw",
    text="Sign in",
    fill="#4A1BD0",
    font=("RobotoRoman SemiBold", 20 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    331.0,
    132.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=180.0,
    y=115.0,
    width=302.0,
    height=33.0
)

canvas.create_text(
    303.0,
    93.0,
    anchor="nw",
    text="Username",
    fill="#696969",
    font=("MontserratRoman Light", 11 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    331.0,
    193.5,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=180.0,
    y=176.0,
    width=302.0,
    height=33.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    156.0,
    194.0,
    image=image_image_1
)

canvas.create_text(
    305.0,
    155.0,
    anchor="nw",
    text="Password",
    fill="#696969",
    font=("MontserratRoman Light", 11 * -1)
)

canvas.create_text(
    283.0,
    216.0,
    anchor="nw",
    text="Forgot password?",
    fill="#696969",
    font=("MontserratRoman Light", 11 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=ValidateLoginDetails,
    relief="flat"
)
button_1.place(
    x=171.0,
    y=260.0,
    width=320.0,
    height=35.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=ButtonForgotPassClick_Execution,
    relief="flat"
)
button_2.place(
    x=389.0,
    y=216.0,
    width=70.0,
    height=12.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    325.0,
    333.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    109.0,
    46.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    156.0,
    132.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    508.0,
    49.0,
    image=image_image_5
)
window.resizable(False, False)
window.mainloop()
