from tkinter import *

ventana=Tk()
ventana.title("NEOCalculator")
e=Entry(ventana, width=10, borderwidth=5) 
e.grid(row=0,column=0,columnspan=3)


# lista=[0,1,2,3,4,5,6,7,8,9,"+"], 
# count= 0
# for i in lista: 
#  botton_i = Button(ventana, text=i)
#  botton_i.grid(row= count // 3 + 3 , column=  count % 3  )
#  count += 1


def button_send():
    global variablePrueba



variablePrueba= StringVar
for i in range(10): 
    botton_i=Button(ventana, text=i), command= lambda: button_send(i)
    botton_i.grid(row= (i // 3)+1 , column= i % 3 )
 



















ventana.mainloop()