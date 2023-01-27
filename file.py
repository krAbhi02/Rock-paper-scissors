from tkinter import *                    # import Tkinter library
from PIL import Image, ImageTk           # import PILLOW library
from random import choice, randint       # import random library

windows=Tk()   
windows.title('rock paper and scissors')
windows.geometry('1920x780')             # setting the geometry of the interface

                                         # Adding the background image

bg = ImageTk.PhotoImage(file = 'C:\\Users\\DELL\\Downloads\\b.png')
label= Label(windows,image=bg)
label.place(x=0,y=0,relwidth=1,relheight=1)


                                        #Images for rock ,paper and scissors

image_rock1 = ImageTk.PhotoImage(Image.open('D:\Rock paper and scissors game\images for the game\Rock1.png'))
image_paper1= ImageTk.PhotoImage(Image.open('D:\Rock paper and scissors game\images for the game\paper1.png'))
image_scissor1=ImageTk.PhotoImage(Image.open('D:\Rock paper and scissors game\images for the game\scissors1.png'))
image_rock2 = ImageTk.PhotoImage(Image.open('D:\Rock paper and scissors game\images for the game\Rock2.png'))
image_paper2= ImageTk.PhotoImage(Image.open('D:\Rock paper and scissors game\images for the game\paper2.png'))
image_scissor2=ImageTk.PhotoImage(Image.open('D:\Rock paper and scissors game\images for the game\scissors2.png'))


                                       # labels for computer and score

label_player=Label(windows,image=image_rock1)
label_computer=Label(windows,image=image_scissor2)
label_computer.grid(row=1,column=4)
label_player.grid(row=1,column=0)

                                       #counting score indicator
computer_score = Label(windows,text=0,font=('arial',60,'bold'),fg='seagreen')
player_score = Label(windows,text=0,font=('arial',60,'bold'),fg='red')
computer_score.grid(row=1,column=3)
player_score.grid(row=1,column=1)

player_indicator = Label(windows,font=('arial',40,'bold'),text='PLAYER',bg='darkslategray',fg='medium purple')
computer_indicator = Label(windows,font=('arial',40,'bold'),text='COMPUTER',bg='darkslategray',fg='firebrick')

computer_indicator.grid(row=0,column=4)
player_indicator.grid(row=0,column=0)


def updateMessage(a):
    final_message['text'] = a

def Computer_update():
    final = int(computer_score['text'])
    final +=1
    computer_score['text'] = str(final)


def Player_update():
    final = int(player_score['text'])
    final +=1
    player_score['text'] = str(final)

def winner_check(p,c):
    if p==c:
        updateMessage("It's a Tie")
    elif p == 'rock':
        if c == 'paper':
            updateMessage('Computer Wins !!')
            Computer_update()
        else:
            updateMessage('Player Wins !!')  
            Player_update()

    elif p == 'paper':
        if c == 'scissor':
            updateMessage('Computer Wins !!')
            Computer_update()
        else:
            updateMessage('Player Wins !!')
            Player_update()

    elif p == 'scissor':
        if c== 'rock':
            updateMessage("Computer Wins !!")
            Computer_update()
        else:
            updateMessage("Player Wins !!")  
            Player_update() 
    else:
        pass         

to_select = ['rock','paper','scissor']

def choice_update(a):

    #Computer
    choice_computer = to_select[randint(0,2)]
    if choice_computer == 'rock':
        label_computer.configure(image=image_rock2)
    elif choice_computer == 'paper' :
        label_computer.configure(image =image_paper2)
    else:
        label_computer.configure(image=image_scissor2)       

    #Player
    if a == 'rock':
        label_player.configure(image=image_rock1)
    elif a == 'paper':
        label_player.configure(image=image_paper1)
    else:
        label_player.configure(image=image_scissor1)

    winner_check(a,choice_computer)    

final_message = Label(windows,font=('arial',40,'bold'),bg='black',fg='red')
final_message.grid(row=3,column=2)

#Buttons

button_rock = Button(windows,width=16, height=2, text='ROCK',
bg='yellow', fg='red',command=lambda:choice_update('rock')).grid(row=2 , column=1)

button_paper = Button(windows,width=16,height=2,text='PAPER',
bg='white',fg='black',command=lambda:choice_update('paper')).grid(row=2,column=2)

Button_scissor = Button(windows,width=16,height=2,text='SCISSOR',
bg='green',fg='blue',command=lambda:choice_update('scissor')).grid(row=2,column=3)

#exiting the mainloop
windows.mainloop()