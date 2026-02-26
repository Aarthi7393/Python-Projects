#Words input -https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/German_subtitles_1000
#Words- https://github.com/hermitdave/FrequencyWords/blob/master/content/2018/de/de_50k.txt
#googletranslate- https://support.google.com/docs/answer/3093331?hl=en-GB
#google language code - https://docs.cloud.google.com/translate/docs/languages?hl=en
import random
from tkinter import *
import pandas as pd
from playsound3 import playsound
import os
from gtts import gTTS

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
current_card = {}
try:
    df = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("./data/fresh_words.csv")

#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html
to_learn = df.to_dict(orient="records")
print(to_learn)
#--------------------------------REMOVE KNOWN CARD-----------------------------
def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)

    next_word()


#------------------------------GENERATE RANDOM WORD---------------------------
def next_word():
    language = 'de'
    global flip_timer, current_card

    current_card = random.choice(to_learn)
    new_word = current_card["German"]
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(title, text="German", fill="black")
    canvas.itemconfig(word, text = new_word, fill="black")

    window.after(1000)
    audio_output = gTTS(text=current_card["German"], lang=language)
    audio_output.save("german_word.mp3")
    playsound("german_word.mp3", True)
    os.remove("german_word.mp3")



    flip_timer = window.after(3000, flip_card)

#------------------------ CARD FLIP-----------------------------------------------
def flip_card():
    language = 'en'
    word_en = current_card["English"]
    print(word_en)
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text= word_en, fill="white")

    window.after(1000)
    audio_output = gTTS(text=current_card["English"], lang=language)
    audio_output.save("english_word.mp3")
    playsound("english_word.mp3", True)
    os.remove("english_word.mp3")




#----------------------------------UI SETUP---------------------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=25,bg = BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)
#----------------------------------------------------------------------------
#Images
card_front = PhotoImage(file = "./images/card_front.png")
card_back = PhotoImage(file = "./images/card_back.png")
right = PhotoImage(file = "./images/right.png")
wrong = PhotoImage(file = "./images/wrong.png")



#------------------------------------
canvas = Canvas(width=800, height=526,bg = BACKGROUND_COLOR , highlightthickness=0)
canvas_image = canvas.create_image(400,263,image=card_front)

#-----------------------------------
#Text
title= canvas.create_text(400,150, text= "German" , font= LANGUAGE_FONT)
word = canvas.create_text(400,263,text = "word" , font= WORD_FONT)


canvas.grid(row=0, column=0, columnspan=2, sticky="EW")

#Buttons
wrong_button = Button()
right_button = Button()
right_button.config(image= right, highlightthickness=0, command = is_known)
wrong_button.config(image= wrong, highlightthickness=0, command= next_word)

wrong_button.grid(row = 1, column = 0)
right_button.grid(row = 1, column = 1)

next_word()
window.mainloop()
