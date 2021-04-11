from tkinter import *


# Funcoes

def raja():
    from pyperclip import copy
    from pynput.keyboard import Controller, Key
    global spam
    global enviado
    global countdown
    global quantidades
    global mensagi
    kb = Controller()
    if spam:
        if enviado != int(quantidades):
            enviado +=1
            if enviado == 1:
                copy(f'{mensagi}')
            kb.press(Key.ctrl)
            kb.press('v')
            kb.release(Key.ctrl)
            kb.release('v')
            kb.press(Key.enter)
            kb.release(Key.enter)
            root.after(50)
            raja()
            print('convertible')
        elif enviado == quantidades:
            print('i like ya cut')
            spam = False
        # print('iceee')


def comeca():
    global countdown
    global spam
    global enviado
    global quantidades
    global mensagi
    quantidades = qnt_entry.get("1.0", 'end')
    if len(quantidades) == 1:
        quantidades = 0
    mensagi = msg_entry.get("1.0", 'end')

    print(f"coun{countdown}")
    if type(countdown) == int:
        if countdown > 0:
            countdown -= 1
            timer['text'] = countdown
            root.after(1000, comeca)
        if countdown == 0:
            countdown = 'Comecando!...'
            timer['text'] = countdown

    else:
        spam = True
        countdown = 5
        enviado = 0
        timer['text'] = countdown
        print('convertible')
        raja()


# Gui

root = Tk()
root.title('Rajador_5.0 By D0C_')
root.geometry('350x500')
imagem = PhotoImage(file='N1-L3.png')
root.iconphoto(False, imagem)

# Variables
enviado = 0
spam = False
countdown = 5

# Widgets

credito = Label(
    text='Rajazap 5.0\nBy D0C_',
    font='none 14 bold'
)

msg_label = Label(
    text='Mensagem\nPara spam',
    justify=LEFT,
    font='none 10 bold'
)
msg_entry = Text(
    width='30',
    height='10',
    bd='2',
    relief='solid'
)
qnt_label = Label(
    text='quantidade',
    justify=LEFT,
    font='none 10 bold'
)
qnt_entry = Text(
    width='5',
    height='1',
    bd=2,
    relief='solid',
)
raja_button = Button(
    text='Raja!',
    font='none 10 bold',
    command=lambda: comeca()
)
timer = Label(
    text=countdown,
    font='none 20 bold',
    fg='green'
)

# Grid

credito.grid(row=0, column=1)
msg_label.grid(row=1, column=0, sticky=NW)
msg_entry.grid(row=1, column=1, sticky=SW)
qnt_label.grid(row=2, column=0, sticky=SW)
qnt_entry.grid(row=2, column=1, sticky=W)
raja_button.grid(row=2, column=1)
timer.grid(row=3, column=1)

# Loop
root.mainloop()
