# IMPORTS
from tkinter import *
from googletrans import Translator
from pandas import read_csv
import pandas as pd

# VARIABLES DECLARATION
BACKGROUND_COLOR="#131313"
FROM_LANGUAGES = {}
TO_LANGUAGES = {}
root = Tk()
translator = Translator()
file = './languages.csv'
df = pd.read_csv(file)
title = 'Python translator'

# METHODS
def translate():
    """Translate the text from the input and write it on the output
    """
    if get_iso_language(input_language_clicked.get()) == 'Automatic':
        translation = translator.translate(input_text.get(1.0, END), dest=get_active_option(output_language_clicked))
    else:
        translation = translator.translate(input_text.get(1.0, END), src=get_active_option(input_language_clicked), dest=get_active_option(output_language_clicked))
    output_text.delete(1.0, END)
    output_text.insert(1.0, translation.text)

def get_iso_language(language):
    """Return the iso representation of the language

    Args:
        language (string): the language

    Returns:
        string: the iso representation
    """
    return FROM_LANGUAGES.get(language)

def get_active_option(option):
    """Return the active option of an option menu

    Args:
        option (string): the option menu

    Returns:
        string: the option
    """
    return option.get()

# READING LANGUAGES FROM CSV
for index, row in df.iterrows():
    if index == 0:
        FROM_LANGUAGES[row['Long-Language']] = row['Short-Language']
    if index > 0:
        FROM_LANGUAGES[row['Long-Language']] = row['Short-Language']
        TO_LANGUAGES[row['Long-Language']] = row['Short-Language']

# MORE VARIABLES DECLARATION
input_language_clicked = StringVar(root)
output_language_clicked = StringVar(root)
input_language_clicked.set(list(FROM_LANGUAGES)[0])
output_language_clicked.set(list(TO_LANGUAGES)[0])
title_label = Label(root, text=title)
input_text = Text(root, height="5", width="20",borderwidth=1, relief="flat", font=("Monospace", 15))
output_text = Text(root, height="5", width="20",borderwidth=1, relief="flat", font=("Monospace", 15))
button = Button(root, text="Translate", command=translate)
input_option_menu = OptionMenu(root, input_language_clicked, *FROM_LANGUAGES)
output_option_menu = OptionMenu(root, output_language_clicked, *TO_LANGUAGES)

# CONFIGURATIONS
root.title(title)
root.geometry("500x500")
root.resizable(False, False)
root.configure(bg=BACKGROUND_COLOR)
title_label.config(font=("Monospace", 20))
title_label.config(bg=BACKGROUND_COLOR)
title_label.config(fg="white")

# PACK
title_label.pack()
input_text.pack()
output_text.pack()
button.pack()
input_option_menu.pack()
output_option_menu.pack()

mainloop()
