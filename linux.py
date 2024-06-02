# from fractions import Fraction
from tkinter import *
import webbrowser

# print("Rembember to input the negative numbers with the negative sign.\nExample: -1\n") 
# a = int(input("Input the A of the equation:\n"))
# b = int(input("Input the B of the equation:\n"))
# c = int(input("Input the C of equation:\n"))


# def delta(): 
#     delta_calculo = (b)**2 - (4*a*c)
#     print(delta_calculo)
#     return delta_calculo


# raiz_d = (delta()**(1/2))

# def eq_x1():
#     x1 = (-(b) - raiz_d) / (2*a)
#     print(x1)
#     return x1


# def eq_x2():
#     x2 = (-(b) + raiz_d) / (2*a)
#     print(x2)
#     return x2


# delta()
# eq_x1()
# eq_x2()


screen = Tk()
screen.title("Quadratic Equation - The Facilitation")
screen.geometry("600x600")
screen.config(padx=25, pady=25, bg="#000000")
screen.resizable(False, False)


def site():
    webbrowser.open_new("lastdreamer.com")


#Last Dreamer - Label
ld = Button(text="LASTDREAMER.COM", bg="#000000", fg="#ffffff", font="Consolas", command=site, highlightthickness=0)
ld.place(x=190, y=550)

#Frame
tela_intro = Frame(screen, bg="#800000")
tela_intro.pack(fill="both", expand=True)

f1 =  Label(text="-b ± √(b² -4ac)", fg="#ffffff", bg="#800000", width=15, font=("Consolas", 20), anchor="center")
f1.place(x=160, y=37)
f2 =  Label(text="x = ---------------", fg="#ffffff", bg="#800000", width=20, font=("Consolas", 20), anchor="center")
f2.place(x=91, y=65)
f3 =  Label(text="2a", fg="#ffffff", bg="#800000", width=20, font=("Consolas", 20), anchor="center")
f3.place(x=115, y=93)


#Entries
a_entry = Entry(justify="center", width=10)
a_entry.place(x=70, y=210)
b_entry = Entry(justify="center", width=10)
b_entry.place(x=230, y=210)
c_entry = Entry(justify="center", width=10)
c_entry.place(x=390, y=210)

a_label = Label(text="a", justify="center", fg="#ffffff", bg="#800000", font=("Consolas", 20))
a_label.place(x=103, y=170)
b_label = Label(text="b", justify="center", fg="#ffffff", bg="#800000", font=("Consolas", 20))
b_label.place(x=263, y=170)
c_label = Label(text="c", justify="center", fg="#ffffff", bg="#800000", font=("Consolas", 20))
c_label.place(x=423, y=170)

tip = Label(text="Negative Numbers:  Input Them With the Negative Sign\nex: -3", justify="center", fg="#ffffff", bg="#800000", font=("Consolas", 10))
tip.place(x=65, y=240)



def delta():
    a = a_entry.get()
    if a[0] == "-" and a[1:].isdigit():
        return True
    elif a.isdigit():
        return True
    
    b = b_entry.get()
    if b[0] == "-" and b[1:].isdigit():
        return True
    elif b.isdigit():
        return True
    
    c = c_entry.get()
    if c[0] == "-" and c[1:].isdigit():
        return True
    elif c.isdigit():
        return True
    
    global delta_calculo
    delta_calculo = (b)**2 - (4*a*c)
    return delta_calculo




facilitate = Button(text="FACILITATE", bg="#000000", fg="#cd2d2d", justify="center", font="Consolas", command=delta)
facilitate.place(x=208, y=280)





screen.mainloop()


# #Formula
# #      -b ± √(b² -4ac)
# #X =   ---------------
# #           2a


# # Δ - Delta