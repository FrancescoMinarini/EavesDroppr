try:
    import os
    import glob
    from Tkinter import *
    import tkMessageBox as tkmessbox
    import speech_recognition as srec
    print("all packages up and running")
except:
    print("oops, something's wrong i can feel it")

listOfFiles = glob.glob('*.wav')

def onSelect():
    global root
    root.destroy

def quitOnPress():
    global root
    tkmessbox.showinfo("Advancing...", "{} will be transcribed".format(str(var.get())))
    root.destroy

root = Tk()
var = StringVar()
var.set(listOfFiles[0])

for item in listOfFiles:
    button = Radiobutton(root, text=str(item), variable=var, value=item)
    button.pack(anchor = W)

sel_button = Button(root, text = "Eavesdrop", command=quitOnPress)
sel_button.pack()


root.mainloop()

toAnalyze = var.get()

AudioSource = srec.AudioFile(toAnalyze)
r = srec.Recognizer()

with AudioSource as source:
    Vocal = r.record(source)

echo = r.recognize_google(Vocal, language = 'it-IT')

root1 = Tk()
root1.geometry("700x700")
T = Text(root1, width = 700)
l = Label(root1, text = "The extendable ear eavesdropped:")
l.config(font = ("Verdana", 14))

close_button = Button(root1, text = "Close", command = root1.destroy)
again_button = Button(root1, text = "Eavesdrop again")

l.pack()
T.pack()
close_button.pack()
again_button.pack()
T.insert(END, echo)
root1.mainloop()
