from tkinter import *
import tkinter as tk
from tkinter import ttk
import math as m 



main=tk.Tk()
main.title('mohamed dwidar 20100361')
main.resizable(False,False)



 
        
choice=''
e=(2.7182818285)
pi=(22/7)
def click(num):
    now=screen.get()
    screen.delete(0,END)
    screen.insert(0,str(now)+str(num))

def evalu():
    
    y=screen.get()
    z=eval(y)
    screen.delete(0,END)
    screen.insert(0,z)
    

def remover():
    screen.delete(0,END)
def sin(n):
    if n==90:
        return 1
    elif n==0:
        return 0
    else:
        return m.sin(n*(pi)/180)
def cos(n):
    if n==90:
        return 0
    elif n==0:
        return 1
    else:
        return m.cos(n*(pi)/180)
def tan(n):
    if n==0:
        return 0
    elif n==90:
        return 'syntax error'
    else:
        return m.tan(n*(pi)/180)
def log(n):
    return m.log10(n)
def ln(n):
    return m.log(n)
def fac(n):
    return m.factorial(n)

def rt(n):
    return m.sqrt(n)

def backspace():
    be=screen.get()
    last=len(be)
    screen.delete(last-1 , END)

#_converter triggered with a button_ 
def reverser():
    main.geometry("498x470")
    eennttermodconv=Button(main,width=7, height=3, borderwidth=1 , bg='gray26',fg='white' , text='converter',command=lambda:conver())
    eennttermodconv.grid(row=8, column=4)
    main.configure(bg='white')

def conver():
    main.geometry("646x470")
    def con():
        global choice
        choice=typoo.get()
        if choice=='length':
            adder=['miles','kilometer','meter','inch','centimeter','millimeter','micrometer','nanometer','angstrom','picometer']
            fvaluoo['values']=adder
            evaluoo['values']=adder
        elif choice=='temprature':
            adder=['celsius','fahrenheit','kelvin']
            fvaluoo['values']=adder
            evaluoo['values']=adder
    def calc():
        if choice=='length':
            fo=screen.get()
            units = {"miles" : 1609.344 , 'kilometer' : 1000 , 'meter':1 , 'inch':(1/39.37) , 'centimeter':(10**(-2)) , 'millimeter':(10**(-3)),'micrometer':(10**-6),'nanometer':(10**(-9)),'angstrom':(10**(-10)),'picometer':(10**(-12))}
            first=fvaluoo.get()
            last=evaluoo.get()
            answer=(float(fo)*float(units[first]))/float(units[last])
            screen.delete(0,END)
            screen.insert(0,answer)
        
        if choice=='temprature':
            fo=float(screen.get())
            first=fvaluoo.get()
            last=evaluoo.get()
            if first=='celsius':
                if last=='celsius':
                    answer=fo
                    screen.delete(0,END)
                    screen.insert(0,answer)
                elif last=='fahrenheit':
                    answer=(fo*(9/5))+32
                    screen.delete(0,END)
                    screen.insert(0,answer)
                elif last=='kelvin':
                    answer=(fo+273.15)
                    screen.delete(0,END)
                    screen.insert(0,answer)
            if first=='fahrenheit':
                if last=='celsius':
                    answer=(fo-32)*(5/9)
                    screen.delete(0,END)
                    screen.insert(0,answer)
                elif last=='fahrenheit':
                    answer=fo
                    screen.delete(0,END)
                    screen.insert(0,answer)
                elif last=='kelvin':
                    answer=(fo-32)*(5/9)+273.15
                    screen.delete(0,END)
                    screen.insert(0,answer)
            if first=='kelvin':
                if last=='celsius':
                    answer=(fo-273.15)
                    screen.delete(0,END)
                    screen.insert(0,answer)
                elif last=='fahrenheit':
                    answer=(fo-273.15)*(9/5)+32
                    screen.delete(0,END)
                    screen.insert(0,answer)
                elif last=='kelvin':
                    answer=fo
                    screen.delete(0,END)
                    screen.insert(0,answer)
    eennttermodconv=Button(main,width=7, height=3, borderwidth=1 , bg='white',fg='black' , text='converter',command=lambda:reverser())
    eennttermodconv.grid(row=8, column=4)



    typoo=ttk.Combobox(main, values=['temprature','length'])
    typoo.grid(row=0,column=5)
    conbutton=Button(main,text='confirm',command=lambda:con())
    conbutton.grid(row=1,column=5)
    fvaluoo=ttk.Combobox(main, values=[])
    fvaluoo.grid(row=3,column=5)
    evaluoo=ttk.Combobox(main, values=[])
    evaluoo.grid(row=7,column=5)
    flab=Label(main, text='from value',bg='grey25', fg='white')
    flab.grid(row=4,column=5)
    elab=Label(main, text='to value',bg='grey25', fg='white')
    elab.grid(row=6,column=5)
    conbutton=Button(main,text='convert',command=lambda:calc())
    conbutton.grid(row=5,column=5)



    main.configure(bg='grey25')














screen=Entry(main, width=61 , borderwidth=4 , bg='lavender' , fg='cadetblue4' , justify=LEFT , font=("Calibri",12) )
screen.grid(row=0 , column=0 , columnspan=5 , pady=3 , padx=0  )

eenntter1=Button(main,width=16 , height=3, borderwidth=1 , bg='grey' , text='1',command=lambda:click('1'))
eenntter1.grid(row=1, column=0)


eenntter2=Button(main,width=16, height=3, borderwidth=1 , bg='grey' , text='2',command=lambda:click('2'))
eenntter2.grid(row=1, column=1)

eenntter3=Button(main,width=16, height=3, borderwidth=1 , bg='grey' , text='3',command=lambda:click('3'))
eenntter3.grid(row=1, column=2)

eenntterc=Button(main,width=7, height=3, borderwidth=1 , bg='red', fg='white' , text='C',command=lambda:remover())
eenntterc.grid(row=1, column=3)

eenntterdot=Button(main,width=7, height=3, borderwidth=1 , bg='light coral' , text='bksp' , command=backspace)
eenntterdot.grid(row=1, column=4)

#-----------------------------------------------------------------------------------------
eenntter4=Button(main,width=16 , height=3, borderwidth=1 , bg='grey' , text='4',command=lambda:click('4'))
eenntter4.grid(row=2, column=0)

eenntter5=Button(main,width=16, height=3, borderwidth=1 , bg='grey' , text='5',command=lambda:click('5'))
eenntter5.grid(row=2, column=1)

eenntter6=Button(main,width=16, height=3, borderwidth=1 , bg='grey' , text='6',command=lambda:click('6'))
eenntter6.grid(row=2, column=2)

eenntterx=Button(main,width=16, height=3, borderwidth=1 , bg='yellow' , text='x',command=lambda:click('*'))
eenntterx.grid(row=2, column=3, columnspan=2)

#-----------------------------------------------------------------------------------------
eenntter7=Button(main,width=16 , height=3, borderwidth=1 , bg='grey' , text='7',command=lambda:click('7'))
eenntter7.grid(row=3, column=0)

eenntter8=Button(main,width=16, height=3, borderwidth=1 , bg='grey' , text='8',command=lambda:click('8'))
eenntter8.grid(row=3, column=1)

eenntter9=Button(main,width=16, height=3, borderwidth=1 , bg='grey' , text='9',command=lambda:click('9'))
eenntter9.grid(row=3, column=2)

eenntterdiv=Button(main,width=16, height=3, borderwidth=1 , bg='yellow' , text='/',command=lambda:click("/"))
eenntterdiv.grid(row=3, column=3, columnspan=2)


#-----------------------------------------------------------------------------------------
eenntteradd=Button(main,width=16 , height=3, borderwidth=1 , bg='yellow' , text='+',command=lambda:click('+'))
eenntteradd.grid(row=4, column=2)

eenntter0=Button(main,width=16, height=3, borderwidth=1 , bg='grey' , text='0',command=lambda:click('0'))
eenntter0.grid(row=4, column=1)

eenntterdot=Button(main,width=16, height=3, borderwidth=1 , bg='grey' , text='.',command=lambda:click('.'))
eenntterdot.grid(row=4, column=0)

eennttersub=Button(main,width=16, height=3, borderwidth=1 , bg='yellow' , text='-',command=lambda:click('-'))
eennttersub.grid(row=4, column=3, columnspan=2)

#-----------------------------------------------------------------------------------------
eennttertan=Button(main,width=16 , height=3, borderwidth=1 , bg='steel blue' , text='tan',command=lambda:click('tan('))
eennttertan.grid(row=6, column=0)

eennttercos=Button(main,width=16, height=3, borderwidth=1 , bg='steel blue' , text='cos',command=lambda:click('cos('))
eennttercos.grid(row=5, column=1)



eennttereval=Button(main,width=16, height=3, borderwidth=1 , bg='green1' , text='=',command=lambda:evalu())
eennttereval.grid(row=5, column=3, columnspan=2)

#______________________________________________________________________________
eennttersiner=Button(main,width=16, height=3, borderwidth=1 , bg='steel blue' , text='sin',command=lambda:click('sin('))
eennttersiner.grid(row=5, column=0)

eenntterkt2=Button(main,width=7, height=3, borderwidth=1 , bg='yellow' , text=')',command=lambda:click(')'))
eenntterkt2.grid(row=6, column=4)

eenntterkt1=Button(main,width=7, height=3, borderwidth=1 , bg='yellow' , text='(',command=lambda:click('('))
eenntterkt1.grid(row=6, column=3)

eenntterloger=Button(main,width=16, height=3, borderwidth=1 , bg='steel blue' , text='log',command=lambda:click('log('))
eenntterloger.grid(row=6, column=1)

eenntterlner=Button(main,width=16, height=3, borderwidth=1 , bg='steel blue' , text='ln',command=lambda:click('ln('))
eenntterlner.grid(row=6, column=2)

#----------------_________________________________-------------------------------------------------
eenntterrooter=Button(main,width=16, height=3, borderwidth=1 , bg='steel blue' , text='root',command=lambda:click('rt('))
eenntterrooter.grid(row=7, column=0)

eenntterpw=Button(main,width=16, height=3, borderwidth=1 , bg='steel blue' , text='Y^x',command=lambda:click('**'))
eenntterpw.grid(row=7, column=1)

eenntterpw2=Button(main,width=16, height=3, borderwidth=1 , bg='steel blue' , text='X^2',command=lambda:click('**2'))
eenntterpw2.grid(row=7, column=2)

eenntterepw=Button(main,width=16, height=3, borderwidth=1 , bg='steel blue' , text='e^x',command=lambda:click('e**'))
eenntterepw.grid(row=5, column=2)

#------------------------------------------------------------------------------------------
eenntterabs=Button(main,width=16, height=3, borderwidth=1 , bg='steel blue' , text='|x|',command=lambda:click('abs('))
eenntterabs.grid(row=8, column=0)

eenntterfac=Button(main,width=16, height=3, borderwidth=1 , bg='steel blue' , text='x!',command=lambda:click('fac('))
eenntterfac.grid(row=8, column=1)

eenntterenvy=Button(main,width=16, height=3, borderwidth=1 , bg='steel blue' , text='1/x',command=lambda:click('1/'))
eenntterenvy.grid(row=8, column=2)

eennttermoder=Button(main,width=7, height=3, borderwidth=1 , bg='steel blue' , text='%',command=lambda:click('%'))
eennttermoder.grid(row=8, column=3)

eenntterpier=Button(main,width=7, height=3, borderwidth=1 , bg='steel blue' , text='π',command=lambda:click('pi'))
eenntterpier.grid(row=7, column=3)

eennttereer=Button(main,width=7, height=3, borderwidth=1 , bg='steel blue' , text='e',command=lambda:click('e'))
eennttereer.grid(row=7, column=4)

eennttermodconv=Button(main,width=7, height=3, borderwidth=1 , bg='gray26',fg='white' , text='converter',command=lambda:conver())
eennttermodconv.grid(row=8, column=4)









main.mainloop()