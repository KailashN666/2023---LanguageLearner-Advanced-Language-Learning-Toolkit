import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import nltk
#nltk.download('omw-1.4')
from nltk.corpus import wordnet
import spacy
from googletrans import Translator
import requests
import pyttsx3

from PIL import Image, ImageTk

translator = Translator()
nlp = spacy.load("en_core_web_sm")
text_speech = pyttsx3.init()
text_speech.setProperty("rate", 150)

STATES = {
    "START": ["NOUN", "VERB", "PRON", "ADJ", "ADV", "DET", "ADP", "CONJ", "INTJ", "NUM"],
    "NOUN": ["NOUN", "VERB", "PRON", "ADJ", "ADV", "DET", "ADP", "CONJ", "INTJ", "NUM", "END"],
    "VERB": ["NOUN", "VERB", "PRON", "ADJ", "ADV", "DET", "ADP", "CONJ", "INTJ", "NUM", "END"],
    "PRON": ["NOUN", "VERB", "PRON", "ADJ", "ADV", "DET", "ADP", "CONJ", "INTJ", "NUM", "END"],
    "ADJ": ["NOUN", "VERB", "PRON", "ADJ", "ADV", "DET", "ADP", "CONJ", "INTJ", "NUM", "END"],
    "ADV": ["NOUN", "VERB", "PRON", "ADJ", "ADV", "DET", "ADP", "CONJ", "INTJ", "NUM", "END"],
    "DET": ["NOUN", "VERB", "PRON", "ADJ", "ADV", "DET", "ADP", "CONJ", "INTJ", "NUM", "END"],
    "ADP": ["NOUN", "VERB", "PRON", "ADJ", "ADV", "DET", "ADP", "CONJ", "INTJ", "NUM", "END"],
    "CONJ": ["NOUN", "VERB", "PRON", "ADJ", "ADV", "DET", "ADP", "CONJ", "INTJ", "NUM", "END"],
    "INTJ": ["NOUN", "VERB", "PRON", "ADJ", "ADV", "DET", "ADP", "CONJ", "INTJ", "NUM", "END"],
    "NUM": ["NOUN", "VERB", "PRON", "ADJ", "ADV", "DET", "ADP", "CONJ", "INTJ", "NUM", "END"],
    "END": []
}

current_state = "START"
meaning=" " 

def check_part_of_speech(word):
    global current_state
    current_state = "START"
    doc = nlp(word)
    pos = doc[0].pos_
    if pos in STATES[current_state]:
        current_state = pos
        if current_state=="VERB":
            current_state="Verb"
        if current_state=="NOUN":
            current_state="Noun"
        if current_state=="PRON":
            current_state="Pronoun"
        if current_state=="ADJ":
            current_state="Adjective"
        if current_state=="ADV":
            current_state="Adverb"
        if current_state=="DET":
            current_state="Determiner"
        if current_state=="ADP":
            current_state="Preposition"
        if current_state=="CONJ":
            current_state="Conjunction"
        if current_state=="INTJ":
            current_state="Interjection"
        if current_state=="NUM":
            current_state="Numeral"
    else:
        current_state = "START"

def get_word_meaning(word):
    global meaning
    synsets = wordnet.synsets(word)
    if synsets:
        meaning = synsets[0].definition()
        return meaning
    else:
        return "No meaning found."
    
#Translator function
def translate_word(word, target_lang):
    translation = translator.translate(word, dest=target_lang)
    return translation.text

#Synonym function
def find_synonyms(userInput):
    try:
        endpoint = "https://api.datamuse.com/words"
        
        params = {
            "rel_syn": userInput 
        }

        response = requests.get(endpoint, params=params)
        
        synonyms = [result["word"] for result in response.json()]

        if synonyms:
            synonyms_str = ", ".join(synonyms[:10])
            lbl_synonyms.config(text=f"Synonyms: {synonyms_str}")
        else:
            lbl_synonyms.config(text="No synonyms found.")
    except Exception as e:
        messagebox.showerror("Error", f"Synonym Finding Error: {str(e)}")

# Function to perform text-to-speech
def perform_text_to_speech():
    text_to_speech_text = entry.get()
    if text_to_speech_text.strip() == "":
        messagebox.showwarning("Warning", "Please enter text for speech.")
        return

    text_speech.say(text_to_speech_text)
    text_speech.runAndWait()

def on_button_click(event=None):
    #to get the user word
    user_input = entry.get()
    if user_input.strip() == "":
        messagebox.showwarning("Warning", "Please enter a word.")
        return
    check_part_of_speech(user_input)
    if current_state=="START":
      partOfS="Unidentifiable"                                   
    else:                                                        
        partOfS=current_state 
    meaning = get_word_meaning(user_input)
    selected_language = combo_language.get()
    if selected_language != "":
        #to get the translated word
        translation = translate_word(user_input, selected_language)
        lblTranslated.config(text=f"Translated: {translation}") 
    lblSpeech.config(text="Part of Speech: "+partOfS)
    lblMean.config(text="Meaning: "+meaning)
    find_synonyms(user_input)

window = tk.Tk()
window.title("Quick Search")

bg_image = Image.open(r"C:\Users\Kai\Desktop\Project\Screen 6 - Quick Search\Quick Search Background.png")
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

input_frame_part = tk.LabelFrame(window,  padx=10, pady=0, bg="white")
input_frame_part.pack(fill="both", expand="no", padx=10, pady=0)

label = tk.Label(input_frame_part, text="Enter a word:", background="white")
label.grid(row=0, column=0, padx=5, pady=5)

entry = tk.Entry(input_frame_part)
entry.grid(row=0, column=1, padx=5, pady=5)

listen_button = tk.Button(input_frame_part, text="Listen",command=perform_text_to_speech)
listen_button.grid(row=0, column=2, padx=5, pady=5)

# Create a Canvas for the image
#canvas = tk.Canvas(input_frame_part, width=40, height=40, bg="white")
#canvas.grid(row=0, column=3, padx=5, pady=5, sticky="e")

# Draw a rectangle (change the coordinates and size as needed)
#canvas.create_rectangle(10, 10, 40, 40, fill="blue")

language_options = ["English", "Afrikaans", "Zulu"] 

combo_language = ttk.Combobox(input_frame_part, values=language_options)
combo_language.set("English")
combo_language.bind("<<ComboboxSelected>>", on_button_click)
combo_language.grid(row=1, column=1, padx=5, pady=5)

button = tk.Button(input_frame_part, text="Perform Action", command=on_button_click)
button.grid(row=2, column=1, padx=5, pady=10)

lblTranslated = tk.Label(window, text=" ", background="white")
lblTranslated.pack(pady=10)

lblSpeech = tk.Label(window, text=" ", background="white")
lblSpeech.pack(pady=10)

lblMean = tk.Label(window, text=" ", background="white")
lblMean.pack(pady=10)

lbl_synonyms = tk.Label(window, text=" ", background="white")
lbl_synonyms.pack(pady=10)

photo_references = [bg_photo]  #PhotoImage objects

window.mainloop()


