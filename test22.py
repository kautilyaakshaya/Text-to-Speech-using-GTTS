from tkinter import *
from gtts import gTTS
import os

def test1():
    #label
    Label(root, text ='Enter the text', font ='Times 15 bold', bg ='White').place(x=222,y=180)

    ##text variable
    Msg = StringVar()

    #Entry
    entry_field = Entry(root, textvariable=Msg, width='84')
    entry_field.place(x=20, y=220)

    ###################define function##############################

    def Text_to_speech():
        Message = entry_field.get()
        speech = gTTS(text=Message)
        speech.save('DataFlair.mp3')
        os.system('DataFlair.mp3')

    def Exit():
        root.destroy()

    def Reset():
        Msg.set("")

    #Button
    Button(root, text="PLAY", font='times 15 italic', command=Text_to_speech, width=5).place(x=40, y=260)
    Button(root, text='EXIT', font='times 15 italic', command=Exit, bg='Red1').place(x=245, y=260)
    Button(root, text='RESET', font='times 15 italic', command=Reset).place(x=420, y=260)

def test2():
    #label
    Label(root, text='Enter the file name', font='Times 15 bold', bg='White').place(x=200, y=180)

    ##text variable
    Msg = StringVar()

    #Entry
    entry_field = Entry(root, textvariable=Msg, width='84')
    entry_field.place(x=20, y=220)

    ###################define function##############################

    def Text_to_speech():
        z = entry_field.get()
        q = z + ".txt"
        f = open(q, "r")
        input_text = f.read().replace("\n", " ")
        speech = gTTS(text=input_text)
        speech.save('DataFlair.mp3')
        os.system('DataFlair.mp3')

    def Exit():
        root.destroy()

    def Reset():
        Msg.set("")

    #Button
    Button(root, text="PLAY", font='times 15 italic', command=Text_to_speech, width=5).place(x=40, y=260)
    Button(root, text='EXIT', font='times 15 italic', command=Exit, bg='Red1').place(x=245, y=260)
    Button(root, text='RESET', font='times 15 italic', command=Reset).place(x=420, y=260)

root = Tk()
root.geometry('550x600')
root.resizable(0,0)
root.config(bg='cyan2')
root.title("Insane's - TEXT_TO_SPEECH")

##heading
Label(root, text='TEXT_TO_SPEECH', font='times 20 bold', bg='gray79').pack()
Label(root, text='Insane', font='times 15 bold', bg='ghost white').pack(side=BOTTOM)

Button(root, text='Want to Read Text', font='times 15 italic', command=test1, bg='steelblue1').place(x=200, y=70)
Button(root, text='Want to Read File', font='times 15 italic', command=test2, bg='steelblue1').place(x=200, y=130)

#infinite loop to run program
root.mainloop()
