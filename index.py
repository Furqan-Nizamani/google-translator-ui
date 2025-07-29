from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text='type', src='English', dest='Urdu'):
    test1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text, src=src1, dest=dest1)
    return trans1.text

def data():
    s = combo_sor.get()
    d = combo_dest.get()
    masag = sor_txt.get(1.0, END)
    textget = change(text= masag, src=s, dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END, textget)











root = Tk()

root.title('**Translator**')
root.geometry('500x800')
root.config(bg='red')

lab_txt = Label(root, text='Translator', font=('Time New Roman', 40, 'bold'),bg='red')
lab_txt.place(x=100, y=30, height=100, width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root, text='Source Text', font=('Time New Roman', 20, 'bold'),fg='Black',bg='red')
lab_txt.place(x=100, y=110, height=30, width=300)

sor_txt = Text(frame, font=('Time New Roman', 20, 'bold'),wrap=WORD)
sor_txt.place(x=10, y=150, height=150, width=480)

list_txt = list(LANGUAGES.values())
combo_sor = ttk.Combobox(frame, value=list_txt)
combo_sor.place(x=10, y=310, height=20, width=100)
combo_sor.set('english')

button_change = Button(frame, text = 'Translate', relief=RAISED, command=data)
button_change.place(x=120, y=310, height=40, width=260)

combo_dest = ttk.Combobox(frame, value=list_txt)
combo_dest.place(x=390, y=310, height=20, width=100)
combo_dest.set('english')

lab_txt = Label(root, text='Dest Text', font=('Time New Roman', 20, 'bold'),fg='Black',bg='red')
lab_txt.place(x=100, y=360, height=30, width=300)

dest_txt = Text(frame, font=('Time New Roman', 20, 'bold'),wrap=WORD)
dest_txt.place(x=10, y=400, height=150, width=480)


root.mainloop()