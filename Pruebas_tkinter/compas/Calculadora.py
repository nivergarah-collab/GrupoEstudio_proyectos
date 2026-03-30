from tkinter import * # El "*" es para importar todo del tkinter.

Ventana=Tk() #crea la ventana.
Ventana.title("Calculadora") #da nombre a la ventana.
e=Entry(Ventana,width=40,borderwidth=5) #crea la pantalla donde el usuario ingresara los numeros y el"e" es solo el nombre ponganle como quieran.
e.grid(row=0,column=0,columnspan=4) #asigna donde va la pantalla y lo que ira debajo de ella, El ".grid" es una red como su nombre lo indica,
# en donde le tengo que asignar en que posicion de la red ira, row=fila, column= columna y el "columspan" le dice que debajo de la pantalla iran 4 columnas.

#defino la funcion de los botones: 
def boton_click(numero):
    boton_actual= e.get() #El .get() lee lo que se ingresa en la pantalla y lo guarda.
    e.delete(0,END) #borra lo antes guardado para que no se repita al momento de ingresar otra cosa.
    e.insert(0,str(boton_actual)+str(numero))#esta linea diferencia el numero que entra primero con el que entra despues,
    return                                     #sin esa linea seria como escribir" satse omoc aloh" en vez de "hola como estas."

def boton_suma():
    primer_numero=e.get()
    global p_numero # el "global" permite que todas las funciones puendan acceder a la variable.
    global operacion
    operacion= "suma"
    p_numero=int(primer_numero)# El int es para numeros enteros y float es para los decimales 
    e.delete(0,END)
    
def boton_resta():
    primer_numero=e.get()
    global p_numero
    global operacion
    operacion= "resta"
    p_numero=int(primer_numero)
    e.delete(0,END)
        
def boton_mult():
    primer_numero=e.get()
    global p_numero
    global operacion
    operacion= "multiplicacion"
    p_numero=int(primer_numero)
    e.delete(0,END)    
    
def boton_div():
    primer_numero=e.get()
    global p_numero
    global operacion
    operacion= "division"
    p_numero=int(primer_numero)
    e.delete(0,END)    
    
def boton_clear():
    e.delete(0,END)
    
def boton_igual():
    primer_numero=e.get()
    e.delete(0,END)
    if operacion=="suma": # El "if" es el Si de Pseint  y el "SiNo" seria elif  
        resultado=p_numero+int(primer_numero)
    if operacion=="resta":
        resultado=p_numero-int(primer_numero)
    if operacion=="multiplicacion":
        resultado=p_numero*int(primer_numero)
    if operacion=="division":
        resultado=p_numero/int(primer_numero)  
               
    e.insert(0,resultado)    
    
# defino como seran los botones:           
boton_1=Button(Ventana, text="1", padx=40, pady=20,command=lambda: boton_click(1))
#creo el boton,se mostrara en la ventana, dira 1, el largo es 40 y el ancho es 20 y al final le doy la funcio que hara cuando lo presione.
boton_2=Button(Ventana, text="2", padx=40, pady=20,command=lambda: boton_click(2))# El "commmand" llama a la funcion asignda
boton_3=Button(Ventana, text="3", padx=40, pady=20,command=lambda: boton_click(3))
boton_4=Button(Ventana, text="4", padx=40, pady=20,command=lambda: boton_click(4))#El "lambda" me da paja explicarlo :D busquenlo ustedes
boton_5=Button(Ventana, text="5", padx=40, pady=20,command=lambda: boton_click(5))
boton_6=Button(Ventana, text="6", padx=40, pady=20,command=lambda: boton_click(6))
boton_7=Button(Ventana, text="7", padx=40, pady=20,command=lambda: boton_click(7))
boton_8=Button(Ventana, text="8", padx=40, pady=20,command=lambda: boton_click(8))
boton_9=Button(Ventana, text="9", padx=40, pady=20,command=lambda: boton_click(9))
boton_0=Button(Ventana, text="0", padx=40, pady=20,command=lambda: boton_click(0))
boton_S=Button(Ventana, text="+", padx=40, pady=20,command=boton_suma)
boton_R=Button(Ventana, text="-", padx=40, pady=20,command=boton_resta)
boton_M=Button(Ventana, text="*", padx=40, pady=20,command=boton_mult)
boton_D=Button(Ventana, text="/", padx=40, pady=20,command=boton_div)  
boton_L=Button(Ventana, text="C", padx=40, pady=20,command=boton_clear)  
boton_I=Button(Ventana, text="=", padx=40, pady=20,command=boton_igual)  

# le doy una posicion en la ventana a cada boton, El "boton.Pack()" es una forma desordenada de decir donde ira el boton, siempre se mostrara en el centro de la pantalla.
# recordar que el uno siempre sera 0, es decir 0 = 1 y 1= 2.
boton_1.grid(row=3, column=0)
boton_2.grid(row=3, column=1)
boton_3.grid(row=3, column=2)
boton_4.grid(row=2, column=0)
boton_5.grid(row=2, column=1)
boton_6.grid(row=2, column=2)
boton_7.grid(row=1, column=0)
boton_8.grid(row=1, column=1)
boton_9.grid(row=1, column=2)
boton_0.grid(row=4, column=1)
boton_S.grid(row=3, column=3)
boton_R.grid(row=2, column=3)
boton_M.grid(row=1, column=3)
boton_D.grid(row=4, column=3)
boton_L.grid(row=4, column=0)
boton_I.grid(row=4, column=2)

Ventana.mainloop() #esta linea mantiene la ventana abierta 
#Y pensar que todo esto se puede hacer en 46 lineas de codigo, pero no se como :C 