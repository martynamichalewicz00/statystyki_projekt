import webbrowser
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date
import sys
import os
from matplotlib import pyplot as plt

prawda=0
today = date.today()
d=open("data.txt","r")
data=d.readlines()
calosc=len(data)

def czy_sa_puste():
    output = ""
    with open("ile_stare.txt") as f:
        for line in f:
            if not line.isspace():
                output += line
    f = open("ile_stare.txt", "w")
    f.write(output)
    f.close()

    output = ""
    with open("data_stare.txt") as f:
        for line in f:
            if not line.isspace():
                output += line
    f = open("data_stare.txt", "w")
    f.write(output)
    f.close()

    output = ""
    with open("strony_stare.txt") as f:
        for line in f:
            if not line.isspace():
                output += line
    f = open("strony_stare.txt", "w")
    f.write(output)
    f.close()

    output = ""
    with open("strony.txt") as f:
        for line in f:
            if not line.isspace():
                output += line
    f = open("strony.txt", "w")
    f.write(output)
    f.close()

    output = ""
    with open("ile.txt") as f:
        for line in f:
            if not line.isspace():
                output += line
    f = open("ile.txt", "w")
    f.write(output)
    f.close()

    output = ""
    with open("strony.txt") as f:
        for line in f:
            if not line.isspace():
                output += line
    f = open("strony.txt", "w")
    f.write(output)
    f.close()


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def rgb_kolor(rgb):
    return "#%02x%02x%02x" % rgb

def czy_rowne(tekst):
    f = open("strony.txt", "a")
    ff = open("strony.txt", "r")
    t = ff.readlines()
    i = 0
    nowe_ile=open("ile.txt","a")
    nowe_data=open("data.txt","a")
    global prawda
    tekst2=tekst+"\n"
    for i in range(len(t)):
        if tekst2==t[i] or tekst==t[i]:
            prawda += 1
    if prawda == 0:
        f.writelines("\n" + Term.get())
        nowe_ile.writelines("\n"+"0")
        nowe_ile.close()
        nowe_data.writelines("\n"+str(today))
        nowe_data.close()
    else:
        messagebox.showerror("BŁĄD!", "Taka strona jest już zapisana!")



def zapisz_strone():
    tekst=Term.get()
    if tekst=="":
        messagebox.showerror("BŁĄD!", "Pusta linijka!")
    else:
        czy_rowne(tekst)
    restart_program()

def kolejne_okno(klik,strona):
    a = open("data_stare.txt", "r")
    b = open("ile_stare.txt", "r")
    c = open("strony_stare.txt", "r")
    d = open("data.txt","r")
    e = open("ile.txt","r")
    f = open("strony.txt","r")
    aa=a.readlines()
    bb=b.readlines()
    cc=c.readlines()
    dd=d.readlines()
    ee=e.readlines()
    ff=f.readlines()

    tablica=[]
    tablica_dla_starych=[]
    tablica_x=[]
    tablica_y=[]

    kolejneokno=Toplevel()
    kolejneokno.title(strona)
    kolejneokno.geometry("400x300+660+200")
    kolejneokno.resizable(False, False)
    style = ttk.Style()
    style.configure("Treeview", background=rgb_kolor((43, 43, 43)), foreground=rgb_kolor((230, 230, 230)),
                    rowheight="30", fieldbackground=rgb_kolor((43, 43, 43)), font=(("Couture", 13)))
    style.configure("Treeview.Heading", font=('Couture', 18, 'bold'))
    style.layout("Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])

    scroll = ttk.Scrollbar(kolejneokno)
    scroll.pack(side=RIGHT, fill=Y)
    tabela = Frame(kolejneokno)
    tabela.pack()
    ij=0


    for i in range(len(cc)):
        if strona==str(cc[i]) or strona==str(cc[i])+"\n":
            tablica_dla_starych.append(i)
    for i in range(len(ff)):
        if strona==str(ff[i]) or strona==str(ff[i])+"\n":
            tablica.append(i)

    utworz = ttk.Treeview(tabela)
    utworz['columns'] = ('ILOSC WEJSC', 'DATA')
    utworz.column("#0", width=0, stretch=NO)
    utworz.column('ILOSC WEJSC', anchor=CENTER)
    utworz.column('DATA', anchor=CENTER)
    utworz.heading('ILOSC WEJSC', text="ILOSC WEJSC", anchor=CENTER)
    utworz.heading('DATA', text="DATA", anchor=CENTER)
    for i in range(len(aa)):
        if i in tablica_dla_starych:
            utworz.insert(parent='', index=ij, iid=ij, text='', values=(str(bb[i]), str(aa[i])))
            tablica_y.append(bb[i])
            tablica_x.append(aa[i])
            utworz.pack()
            ij+=1
    for j in range(len(dd)):
        if j in tablica:
            utworz.insert(parent='', index=ij, iid=ij, text='', values=(str(ee[j]), str(dd[j])))
            tablica_y.append(ee[j])
            tablica_x.append(dd[j])
            utworz.pack()
            ij += 1
    converted_list = []
    for element in tablica_y:
        converted_list.append(element.strip())
    converted_list = list(map(int, converted_list))
    fig = plt.figure()
    fig.suptitle(strona, fontsize=20)
    plt.plot(tablica_x, converted_list,color="black")
    plt.scatter(tablica_x, converted_list,color="black")
    plt.show()


def nowe_okno():
    klik=[]
    s = open("ile.txt", "r")
    a=open("data_stare.txt","r")
    b = open("ile_stare.txt", "r")
    c = open("strony_stare.txt", "r")
    a2=a.readlines()
    b2=b.readlines()
    c2=c.readlines()
    t2 = s.readlines()
    noweokno=Toplevel()
    noweokno.title("STATYSTYKI")
    noweokno.geometry("600x500+50+170")
    noweokno.resizable(False, False)
    style=ttk.Style()
    style.configure("Treeview",background=rgb_kolor((43,43,43)),foreground=rgb_kolor((230,230,230)),rowheight="25",fieldbackground=rgb_kolor((43,43,43)),font=(("Couture",13)))
    style.configure("Treeview.Heading", font=('Couture', 18, 'bold'))
    style.layout("Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])
    scroll = ttk.Scrollbar(noweokno)
    scroll.pack(side=RIGHT, fill=Y)
    tabela=Frame(noweokno)
    tabela.pack()
    utworz=ttk.Treeview(tabela)
    utworz['columns'] = ('STRONA', 'ILOSC WEJSC','DATA')
    utworz.column("#0", width=0, stretch=NO)
    utworz.column('STRONA', anchor=CENTER)
    utworz.column('ILOSC WEJSC',anchor=CENTER)
    utworz.column('DATA',anchor=CENTER)
    utworz.heading('STRONA', text="STRONA", anchor=CENTER)
    utworz.heading('ILOSC WEJSC',text="ILOSC WEJSC", anchor=CENTER)
    utworz.heading('DATA', text="DATA", anchor=CENTER)
    for i in range(len(a2)):
        if i==(len(a2)-1):
            if b2[i] != '0':
                utworz.insert(parent='', index=i, iid=i, text='', values=(str(c2[i]), str(b2[i]), a2[i]))
                utworz.pack()
        else:
            if b2[i] != '0\n':
                utworz.insert(parent='', index=i, iid=i, text='', values=(str(c2[i]), str(b2[i]), a2[i]))
                utworz.pack()

    d = open("data.txt", "r")
    e = open("ile.txt", "r")
    f = open("strony.txt", "r")
    d2 = d.readlines()
    e2 = e.readlines()
    f2 = f.readlines()
    tabela2 = Frame(noweokno)
    tabela2.pack()
    utworz2 = ttk.Treeview(tabela2)
    utworz2['columns'] = ('STRONA', 'ILOSC WEJSC', 'DATA')
    utworz2.column("#0", width=1, stretch=NO)
    utworz2.column('STRONA', anchor=CENTER)
    utworz2.column('ILOSC WEJSC', anchor=CENTER)
    utworz2.column('DATA', anchor=CENTER)
    utworz2.heading('STRONA', text="STRONA", anchor=CENTER)
    utworz2.heading('ILOSC WEJSC', text="ILOSC WEJSC", anchor=CENTER)
    utworz2.heading('DATA', text="DATA", anchor=CENTER)
    for i in range(len(d2)):
      utworz2.insert(parent='', index=i, iid=i, text='', values=(str(f2[i]), str(e2[i]), d2[i]))
      utworz2.pack()
    def select_item(event):
        rowid = utworz2.identify_row(event.y)
        klik=rowid
        klik=int(klik)
        strona=f2[klik]
        kolejne_okno(klik,strona)
    utworz2.bind('<ButtonRelease>', select_item)


def search_term():
    f = open("strony.txt", "a")
    ff = open("strony.txt", "r")
    t = ff.readlines()
    i = 0
    s = open("ile.txt", "r")
    t2 = s.readlines()
    tekst=Term.get()
    tekst2=tekst+"\n"
    for i in range(len(t)):
        if tekst2==t[i] or tekst==t[i]:
            linijka=t2[i]
            linijka=int(linijka)
            linijka+=1
            linijka=str(linijka)
            if i==len(t):
                t2[i] = linijka
            else:
                t2[i]=linijka+"\n"
    s=open("ile.txt","w")
    s.writelines(t2)
    s.close()

    webbrowser.open("https://" + Term.get(), new=1)
    restart_program()

root = Tk()
root.title("BROWSEARCH")




root.geometry("630x40+400+80")
root.resizable(False, False)
root.config(bg=rgb_kolor((43, 43, 43)))

Term = StringVar(root, value="")
Term_entry = ttk.Entry(root, textvariable=Term, width=50)
Term_entry.grid(row=0, column=1, padx=10, pady=10)
Term_entry.focus()

statystyki=Button(root,text="STATYSTYKI",font=('Radwave Demo',10),command=nowe_okno)
statystyki.grid(row=0,column=2,padx=2)

zapisz=Button(root,text="ZAPISZ STRONE",font=('Radwave Demo',10),command=zapisz_strone)
zapisz.grid(row=0,column=3,padx=3)

if str(today)!=str(data[calosc-1]):

    ile = open("ile.txt", "r")
    ile_linijki=ile.readlines()
    nowe_ile=open("ile_stare.txt","a")
    nowe_ile.write("\n")
    nowe_ile.writelines(ile_linijki)
    nowe_ile.close()

    strony=open("strony.txt","r")
    ile_stron=strony.readlines()
    nowe_strony=open("strony_stare.txt","a")
    nowe_strony.write("\n")
    nowe_strony.writelines(ile_stron)
    nowe_strony.close()

    daty=open("data.txt","r")
    ile_dat=daty.readlines()
    nowe_daty=open("data_stare.txt","a")
    nowe_daty.write("\n")
    nowe_daty.writelines(ile_dat)
    nowe_daty.close()

    for i in range(len(ile_linijki)):
        if i==(len(ile_linijki)-1):
            ile_linijki[i] = '0'
        else:
            ile_linijki[i] = '0\n'
    ile2=open("ile.txt","w")
    ile2.writelines(ile_linijki)
    ile2.close()
    ile.close()
    for i in range(len(data)):
        if i==(len(data)-1):
            data[i]=str(today)
        else:
            data[i]=str(today)+"\n"
    dd = open("data.txt", "w")
    dd.writelines(data)
    dd.close()


Term_entry.bind("<Return>", (lambda event: search_term()))
czy_sa_puste()
root.mainloop()