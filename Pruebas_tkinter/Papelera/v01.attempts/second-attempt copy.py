import tkinter as tk

def contador():
    global count

    valor = entryBox.get()

    if count == 0:
        EntradaOpciones.set(valor)
    elif count == 1:
        EntradaNum1.set(valor)
    elif count == 2:
        EntradaNum2.set(valor)

    count += 1
    entryBox.delete(0, tk.END)

    print("Opciones:", EntradaOpciones.get())
    print("Num1:", EntradaNum1.get())
    print("Num2:", EntradaNum2.get())


ventana = tk.Tk()
ventana.title("Calculadora")

count = 0

EntradaOpciones = tk.StringVar()
EntradaNum1 = tk.StringVar()
EntradaNum2 = tk.StringVar()

tk.Label(
    ventana,
    text="Tipo de operación:\n"
         "1 = suma\n"
         "2 = resta\n"
         "3 = multiplicación\n"
         "4 = división\n"
         "5 = potencia"
).pack()

entryBox = tk.Entry(ventana)
entryBox.pack()

enterButton = tk.Button(ventana, text="ENTER", command=contador)
enterButton.pack()

ventana.mainloop()