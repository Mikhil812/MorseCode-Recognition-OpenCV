from tkinter import *
from tkinter import messagebox
from converter2 import encrypt
from subprocess import Popen


master = Tk()
master.geometry("700x350")
master.title('MORSE CODE')
master.configure(bg='#DAD2D8')

def open_decode():
    popup_window()

def start_decode():
    global p
    p = Popen(['C:\\Users\\Ahmed\\Desktop\\Sem 6\\DIP\\project\\MorseCode-Recognition-OpenCV\\venv\\Scripts\\python.exe', 'eye_blink.py'])


def stop_decode():
    p.kill()

def popup_window():
    custom_font = ("Arial", 10)
    new_window = Toplevel(master)
    new_window.title("Decode instructions")

    new_window.configure(bg='#DAD2D8')
    new_window.geometry("500x300")
    label = Label(new_window, text="To decode blinks to Morse code:", bg='#DAD2D8', font = ("Arial",12))
    label.grid(row=0, column=0, sticky ="w")

    label1_text = "Close eyes for less than 2 seconds = space"
    label1 = Label(new_window, text=label1_text, font = custom_font, bg='#DAD2D8')
    label1.grid(row=1, column=0, sticky ="w")


    label2_text = "Close eyes for 2-4 seconds = dot"
    label2 = Label(new_window, text=label2_text,  font = custom_font, bg='#DAD2D8')
    label2.grid(row=2, column=0, sticky ="w")

    label3_text = "Close eyes for more than 4 seconds = dash"
    label3 = Label(new_window, text=label3_text,  font = custom_font, bg='#DAD2D8')
    label3.grid(row=3, column=0, sticky ="w")
    create_circle_button(new_window, "START",start_decode , 4, 0)
    create_circle_button(new_window, "STOP",stop_decode , 4, 1)




def openNewWindow():
    def printInput():
        inp = inputText.get(1.0, "end-1c")
        morseSolnLabel.config(text=encrypt(inp.upper()))

    def inp_to_file():
        inp = inputText.get(1.0, "end-1c")
        file_name = "encoded.txt"
        with open(file_name, 'w') as file:
            file.write(encrypt(inp.upper()))

        morseSolnLabel.config(text="created file")

    frame = Toplevel()
    frame.title('ENCODE')
    frame.configure(bg='#DAD2D8')
    frame.geometry("700x500")
    inputText = Text(frame, height=2, width=50, relief="solid", bd=2, borderwidth=2, highlightbackground="#ffffff", highlightcolor="#ffffff", highlightthickness=1, font=("Arial", 16), spacing1=5)
    inputText.pack(pady=50)

    printButton = Button(frame, text="GENERATE MORSE CODE", command=printInput, font=("Arial", 13), foreground='#ffffff', bg='#17BEBB', relief='raised', bd=3, width=30, activebackground='#17BEBB', activeforeground='#ffffff')
    printButton.pack(pady=30)



    morseSolnLabel = Label(frame, text="", font=("Arial", 50, 'bold'), fg='#000000', bg='#ffffff', height=-6, width=20)
    morseSolnLabel.pack()

    fileButton = Button(frame, text="CONVERT TO TXT FILE", command=inp_to_file, font=("Arial", 13),
                        foreground='#ffffff', bg='#17BEBB', relief='raised', bd=3, width=30,
                        activebackground='#17BEBB', activeforeground='#ffffff')
    fileButton.pack(pady=30)

    frame.mainloop()

def change_color(event):
    canvas = event.widget
    canvas.itemconfig("circle", fill="#17BEBB")

def create_circle_button(master, text, command, row, column):
    canvas = Canvas(master, width=150, height=150, bg='#DAD2D8', highlightthickness=0)
    canvas.grid(row=row, column=column, padx=20, pady=20)

    x = y = 75
    r = 60
    circle = canvas.create_oval(x - r, y - r, x + r, y + r, outline='#17BEBB', fill='#0E7C7B', width=3, tags="circle")

    canvas.bind("<Button-1>", lambda event: (change_color(event), command()))

    canvas.create_text(x, y, text=text, font=("Arial", 14), fill="#ffffff")

create_circle_button(master, "ENCODE", openNewWindow, 0, 0)
create_circle_button(master, "DECODE", open_decode, 0, 1)

master.grid_rowconfigure(0, weight=1)
master.grid_columnconfigure(0, weight=1)
master.grid_columnconfigure(1, weight=1)

mainloop()