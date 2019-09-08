#!/usr/bin/env python3


from tkinter import *
from random import randint, shuffle


# Click receive the answer text and compare with answer in data
def click(answer):
        global texts, use
        global button1, button2, button3, button4
        print(answer)

        def go_ahead(event):

                global a, b, c, d, e, f, use, img

                # add 6 (each question has six atribbutes) to every variable used in list calls, so the next questions and answers will come
                if use == True:
                   a += 6
                   b += 6
                   c += 6
                   d += 6
                   e += 6
                   f += 6

                # delete the labels used to inform the user that he got it right
                left.delete(correct_label)
                left.delete(correct_label_border)
                left.delete(info_label)


                try:
                        positions = [a,c,d,e]
                        shuffle(positions)

                        left.itemconfig(questiontext, text=texts[b])
                        button1.configure(text = texts[positions[0]])
                        button2.configure(text = texts[positions[1]])
                        button3.configure(text = texts[positions[2]])
                        button4.configure(text = texts[positions[3]])

                        img = PhotoImage(file=texts[f])
                        left.itemconfig(image, image=img)
                        left.update()

                        use = False


                # if the list options is over the game will end
                except:
                        left.create_text(250, 250, text="Fim!\nObrigado por jogar <3", font=("Chilanka", 31, "bold"), fill="black", justify='center')
                        left.create_text(250, 250, text="Fim!\nObrigado por jogar <3", font=("Chilanka", 30, "bold"), fill="red", justify='center')


        if use == False:

                # Check each button possibility (certainly a bad way to do that)
                if 'button1' == answer and button1['text'] == texts[a]:
                        use = True
                        print(button1['text'])

                        correct_label = left.create_text(250, 110, text="Correto!", font=("Chilanka", 45, "bold"), fill="black")
                        correct_label_border = left.create_text(250, 110, text="Correto!", font=("Chilanka", 47, "bold"), fill="green2")
                        info_label = left.create_text(250, 450, text="Clique na tela para continuar.", font=("Chilanka", 15, "bold"), fill="steelblue3")

                        root.bind("<Button-1>", go_ahead)
                
                if 'button2' == answer and button2['text'] == texts[a]:
                        use = True
                        print(button2['text'])

                        correct_label = left.create_text(250, 110, text="Correto!", font=("Chilanka", 45, "bold"), fill="black")
                        correct_label_border = left.create_text(250, 110, text="Correto!", font=("Chilanka", 47, "bold"), fill="green2")
                        info_label = left.create_text(250, 450, text="Clique na tela para continuar.", font=("Chilanka", 15, "bold"), fill="steelblue3")

                        root.bind("<Button-1>", go_ahead)
                
                if 'button3' == answer and button3['text'] == texts[a]:
                        use = True
                        print(button3['text'])

                        correct_label = left.create_text(250, 110, text="Correto!", font=("Chilanka", 45, "bold"), fill="black")
                        correct_label_border = left.create_text(250, 110, text="Correto!", font=("Chilanka", 47, "bold"), fill="green2")
                        info_label = left.create_text(250, 450, text="Clique na tela para continuar.", font=("Chilanka", 15, "bold"), fill="steelblue3")

                        root.bind("<Button-1>", go_ahead)
                
                if 'button4' == answer and button4['text'] == texts[a]:
                        use = True
                        print(button4['text'])

                        correct_label = left.create_text(250, 110, text="Correto!", font=("Chilanka", 45, "bold"), fill="black")
                        correct_label_border = left.create_text(250, 110, text="Correto!", font=("Chilanka", 47, "bold"), fill="green2")
                        info_label = left.create_text(250, 450, text="Clique na tela para continuar.", font=("Chilanka", 15, "bold"), fill="steelblue3")

                        root.bind("<Button-1>", go_ahead)
                

                else:
                        print("incorreto!")

root = Tk()
root.geometry('1000x500+100+100')
root.title('Abacate')
root.resizable(False, False)

use = False
a = 0
b = 1
c = 2
d = 3
e = 4
f = 5


right = Canvas(root, width=500, height=500, bg='SteelBlue3', highlightthickness=0)
right.place(x=500,y=0)

left = Canvas(root, width=500, height=500, bg='white', highlightthickness=0)
left.place(x=0, y=0)


# Left Side: Questions Location.

# Texts that will be displayed in GUI
data_file = open('data.csv', 'r')
data = data_file.read()
data_file.close()

texts = data.split(",")
texts = [s.replace('\n', '') for s in texts]

positions = [a,c,d,e]
shuffle(positions)

question = texts[b]
opt1_text = texts[positions[0]]
opt2_text = texts[positions[1]]
opt3_text = texts[positions[2]]
opt4_text = texts[positions[3]]

# Head: Tell the user the actual level and how much levels are.
total_questions = 7
actual_question = 1

left.create_text(250, 50, text=f'Pergunta {actual_question}/{total_questions}', font=('Chilanka', 17, 'bold'), fill='VioletRed2')
left.create_line(170, 68, 330, 68,  fill='VioletRed2')

# Question: A image ilustrate it.

img = PhotoImage(file=texts[5])

image = left.create_image(250, 250, image=img)

questiontext = left.create_text(250, 400, text=question, font=('Chilanka', 12, 'bold'), fill='black')


# Right Side: Answers Location

# Head: Label to explain the user what to do.
right.create_text(250, 50, text='Escolha sua resposta', font=('Chilanka', 17, 'bold'), fill='white')
right.create_line(170, 67, 330, 67,  fill='white')

#Buttons: Show the itens to the user, just one is correct.

button1 = Button(right, background='SteelBlue3', activebackground='white', foreground='white' ,relief='flat',text=opt1_text, 
font=('Chilanka', 12, 'bold'),highlightthickness = 0, width=37, height=4, command=lambda : click('button1'))
button1.place(x=50, y=135)

right.create_line(50, 222, 446, 222, fill='white')

button2 = Button(right, background='SteelBlue3', activebackground='white', foreground='white' ,relief='flat',text=opt2_text, 
font=('Chilanka', 12, 'bold'),highlightthickness = 0, width=37, height=4, command=lambda : click('button2'))
button2.place(x=50, y=225)

right.create_line(50, 312, 446, 312, fill='white')

button3 = Button(right, background='SteelBlue3', activebackground='white', foreground='white' ,relief='flat',text=opt3_text, 
font=('Chilanka', 12, 'bold'),highlightthickness = 0, width=37, height=4, command=lambda : click('button3'))
button3.place(x=50, y=315)

right.create_line(50, 401, 446, 401, fill='white')

button4 = Button(right, background='SteelBlue3', activebackground='white', foreground='white' ,relief='flat',text=opt4_text, 
font=('Chilanka', 12, 'bold'),highlightthickness=0, width=37, height=4, command=lambda : click('button4'))
button4.place(x=50, y=405)


root.mainloop()