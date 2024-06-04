import tkinter as tk
from tkinter import IntVar, ttk
from tkinter import messagebox

from PIL import Image, ImageTk

window = tk.Tk()
window.title("Quiz")

bg_image = Image.open(r"C:\Users\Kai\Desktop\Project\Screen 7 - Quiz\Quiz Background.png")
# Resize the image to match the frame dimensions
bg_image = bg_image.resize((700, 400), Image.ANTIALIAS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label to display the background image
bg_label = tk.Label(window, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)  # Set label to cover the entire window

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_width = 700
window_height = 400

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.config(bg='pink')

file1 = open(r'C:\Users\Kai\Desktop\Project\Screen 7 - Quiz\Text.txt', 'r')
Lines = file1.readlines()
 
count = 0
current_question = 1
questions = []
# Strips the newline character
for line in Lines:
    count += 1
    text = line.strip()
    questions.append(line.strip())

file2 = open(r'C:\Users\Kai\Desktop\Project\Screen 7 - Quiz\Options.txt', 'r')
Lines2 = file2.readlines()

options = []
countOpt = 0
for line in Lines2:
    countOpt += 1
    text = line.strip()
    options.append(line.strip())


file3 = open(r'C:\Users\Kai\Desktop\Project\Screen 7 - Quiz\Answers.txt', 'r')
Lines3 = file3.readlines()
 
correct_answer = []
countAns = 0
for line in Lines3:
    countAns += 1
    correct_answer.append(int(line.strip()))


quest_label = tk.Label(window, width=45, font=("Times New Roman", 20), text=questions[0], background="white" )
quest_label.pack(pady=0)
quest_label.place(x=10,y=50)

scorelbl = tk.Label(window, width=40, font=("Times New Roman", 15), text="Score: 0", background="white" )
scorelbl.pack(pady=0)
scorelbl.place(x=10,y=10)

num1 = IntVar()
num2 = IntVar()
num3 = IntVar()
num4 = IntVar()

def check_answers(option):
    if (option == 1):
        num2.set(0)
        num3.set(0)
        num4.set(0)
    elif (option == 2):
        num1.set(0)
        num3.set(0)
        num4.set(0)
    elif (option == 3):
        num1.set(0)
        num2.set(0)
        num4.set(0)
    else:
        num1.set(0)
        num2.set(0)
        num3.set(0)


option1 = tk.Checkbutton(window, width=25, font=("Times New Roman", 15), text=options[0], background="#4A1BD0", variable=num1, command=lambda:check_answers(1))
option1.pack(pady=0)
option1.place(x=200,y=100)

option2 = tk.Checkbutton(window, width=25, font=("Times New Roman", 15), text=options[1], background="#4A1BD0", variable=num2, command=lambda:check_answers(2))
option2.pack(pady=0)
option2.place(x=200,y=150)

option3 = tk.Checkbutton(window, width=25, font=("Times New Roman", 15), text=options[2], background="#4A1BD0", variable=num3, command=lambda:check_answers(3))
option3.pack(pady=0)
option3.place(x=200,y=200)

option4 = tk.Checkbutton(window, width=25, font=("Times New Roman", 15), text=options[3], background="#4A1BD0", variable=num4, command=lambda:check_answers(4))
option4.pack(pady=0)
option4.place(x=200,y=250)

tot_options = 3
answer = 0
scoreVal = 0

def nextA():
    global current_question, tot_options, scoreVal

    if num1.get() == 1:
        answer = 1
    elif num2.get() == 1:
        answer = 2
    elif num3.get() == 1:
        answer = 3
    elif num4.get() == 1:
        answer = 4
    else:
        answer = -1
    
    if correct_answer[current_question-1] == answer:
        scoreVal += 1
        scorelbl.config(text=("Score: ",scoreVal))
    
    current_question += 1
    option1.deselect()
    option2.deselect()
    option3.deselect()
    option4.deselect()
    
    if current_question <= len(questions):
        quest_label.config(text=questions[current_question-1])
    
    tot_options += 4
    option1.config(text = options[tot_options-3])
    option2.config(text = options[tot_options-2])
    option3.config(text = options[tot_options-1])
    option4.config(text = options[tot_options])

def nextB():
    global current_question, tot_options, scoreVal

    if num1.get() == 1:
        answer = 1
    elif num2.get() == 1:
        answer = 2
    elif num3.get() == 1:
        answer = 3
    elif num4.get() == 1:
        answer = 4
    else:
        answer = -1
    
    if correct_answer[current_question-1] == answer:
        scoreVal += 1
        scorelbl.config(text=("Score: ",scoreVal))
    

iCounter = 0
def Execution():
    global iCounter
    global scoreVal
    global answer

    if iCounter == 4:
        next_button.config(state="disabled")
        nextB()
        messagebox.showinfo("Information", "Quiz is complete. Your score is " + str(scoreVal))
    else:
        nextA()    
    
    iCounter += 1

next_button = tk.Button(window, text="Next", width=10, font=("Times New Roman", 15), command=Execution)
next_button.pack(pady=10)
next_button.place(x = 290, y = 320)

photo_references = [bg_photo]  #PhotoImage objects

window.mainloop()