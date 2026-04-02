import tkinter as tk


def contador():
    global count, entradaActual

    valor = entradaActual.get()

    if count == 0:
        EntradaOpciones.set(valor)
        entradaActual = EntradaNum1
    elif count == 1:
        EntradaNum1.set(valor)
        entradaActual = EntradaNum2
    elif count == 2:
        EntradaNum2.set(valor)

    entryBox.delete(0, tk.END)
    count += 1

    print("Opciones:", EntradaOpciones.get())
    print("Num1:", EntradaNum1.get())
    print("Num2:", EntradaNum2.get())



ventana = tk.Tk()
ventana.title("Calculadora")

count = 0

EntradaOpciones = tk.StringVar()
EntradaNum1 = tk.StringVar()
EntradaNum2 = tk.StringVar()

entradaActual = EntradaOpciones


MenuOperaciones= tk.Label(ventana,
             text="Tipo de operación:\n "
               "1 = suma,\n"
               "2 = resta,\n"
               "3 = multiplicación,\n"
               "4 = división,\n"
               "5 = potencia\n"
              )
MenuOperaciones.pack()

entryBox = tk.Entry(ventana, textvariable=entradaActual)
entryBox.pack()


enterButton = tk.Button(ventana, text="ENTER", command= contador())
enterButton.pack()


ventana.mainloop()


"""
num1 = int(input("Ingrese el primer numero\n"))
num2 = int(input("Ingrese el segundo numero\n"))

if x == 1:
 r = num1 + num2
 print(f"El resultado es {num1} + {num2} = {r}")
elif x == 2:
 r = num1 - num2
 print(f"El resultado es {num1} - {num2} = {r}")
elif x == 3:
 r = num1 * num2
 print(f"El resultado es {num1} * {num2} = {r}")
elif x == 4:
 if num2 == 0:
  print(f"El resultado es {num1} / {num2} = error")
 else:
  r = num1 / num2
  print(f"El resultado es {num1} / {num2} = {r}")
elif x == 5:
 r = num1 ** num2
 print(f"El resultado es {num1} ^ {num2} = {r}")  
 """