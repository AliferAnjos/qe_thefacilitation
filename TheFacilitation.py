from tkinter import *
from tkinter import messagebox
from fractions import Fraction
import os
import sys
import webbrowser


base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
# foto = os.path.join(base_path, 'images', 'mickey.png')
icone = os.path.join(base_path, 'images', 'equa.ico')

screen = Tk()
screen.title("Quadratic Equation - The Facilitation")
screen.geometry("600x600")
screen.config(padx=25, pady=25, bg="#000000")
screen.resizable(False, False)
screen.iconbitmap(icone)



def site():
    webbrowser.open("lastdreamer.com")


#Last Dreamer - Label
ld = Button(text="LASTDREAMER.COM", bg="#000000", fg="#ffffff", font="Consolas", highlightthickness=0, command=site)
ld.place(x=207, y=550)

#Frame
tela_intro = Frame(screen, bg="#1b1b53")
tela_intro.pack(fill="both", expand=True)

f1 =  Label(text="-b ± √(b² -4ac)", fg="#ffffff", bg="#1b1b53", width=15, font=("Consolas", 20), anchor="center")
f1.place(x=160, y=37)
f2 =  Label(text="x = ---------------", fg="#ffffff", bg="#1b1b53", width=20, font=("Consolas", 20), anchor="center")
f2.place(x=91, y=65)
f3 =  Label(text="2a", fg="#ffffff", bg="#1b1b53", width=20, font=("Consolas", 20), anchor="center")
f3.place(x=115, y=93)


#Entries
a_entry = Entry(justify="center", width=10)
a_entry.place(x=80, y=210)
b_entry = Entry(justify="center", width=10)
b_entry.place(x=240, y=210)
c_entry = Entry(justify="center", width=10)
c_entry.place(x=400, y=210)

a_label = Label(text="a", justify="center", fg="#ffffff", bg="#1b1b53", font=("Consolas", 20))
a_label.place(x=100, y=170)
b_label = Label(text="b", justify="center", fg="#ffffff", bg="#1b1b53", font=("Consolas", 20))
b_label.place(x=260, y=170)
c_label = Label(text="c", justify="center", fg="#ffffff", bg="#1b1b53", font=("Consolas", 20))
c_label.place(x=420, y=170)

tip = Label(text="Negative Numbers:  Input Them With the Negative Sign\nex: -3", justify="center", fg="#ffffff", bg="#1b1b53", font=("Consolas", 10))
tip.place(x=83, y=240)


def delta():
    try:
        a = int(a_entry.get())
        b = int(b_entry.get())
        c = int(c_entry.get())
    except  ValueError:
        messagebox.showerror("ERROR", "Only Natural and Negative Numbers are Accepted!\nTry Again!")
        return
    
    delta_calculo = (b)**2 - (4*a*c)
    delta_resultado = Label(text=delta_calculo, justify="center", width=10, fg="#000000")
    delta_resultado.place(x=240, y=350)

    raiz_d = (delta_calculo**(1/2))
    x1 = (-(b) - raiz_d) / (2*a)
    x1  = Fraction(x1).limit_denominator()
    x2 = (-(b) + raiz_d) / (2*a)
    x2  = Fraction(x2).limit_denominator()


    if x1 < x2:
       s1_result = Label(text=x1, justify="center", fg="#000000", width=5)
       s1_result.place(x=200, y=450)

       s2_result = Label(text=x2, justify="center", fg="#000000", width=5)
       s2_result.place(x=335, y=450)
    else:
       s1_result = Label(text=x2, justify="center", fg="#000000", width=5)
       s1_result.place(x=200, y=450)

       s2_result = Label(text=x1, justify="center", fg="#000000", width=5)
       s2_result.place(x=335, y=450)


facilitate = Button(text="FACILITATE", bg="#000000", fg="#ffffff", justify="center", font="Consolas", command=delta)
facilitate.place(x=223, y=280)

delta_icone = Label(text="Δ - Delta", fg="#ffffff", bg="#1b1b53", font=("Consolas", 15))
delta_icone.place(x=70, y=350)

delta_resultado = Label(text="", justify="center", width=10, fg="#000000")
delta_resultado.place(x=240, y=350)

s = Label(text="S = ", fg="#ffffff", bg="#1b1b53", font=("Consolas", 30))
s.place(x=90, y=430)

chave_esq = Label(text="{", fg="#ffffff", bg="#1b1b53", font=("Consolas", 30))
chave_esq.place(x=150, y=430)
chave_dir = Label(text="}", fg="#ffffff", bg="#1b1b53", font=("Consolas", 30))
chave_dir.place(x=400, y=430)
virgula = Label(text=",", fg="#ffffff" , bg="#1b1b53", font=("Consolas", 30))
virgula.place(x=270, y=430)


s1_result = Label(text="", justify="center", fg="#000000", width=5)
s1_result.place(x=200, y=450)

s2_result = Label(text="", justify="center", fg="#000000", width=5,)
s2_result.place(x=335, y=450)




screen.mainloop()


#Formula
#      -b ± √(b² -4ac)
#X =   ---------------
#           2a


# Δ (Delta)