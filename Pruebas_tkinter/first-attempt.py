import tkinter as tk

EntradaOpciones = None
EntradaNum1 = None
EntradaNum2 = None

valorGlobal = None

EntradaOpciones = tk.StringVar()
"""
def variableCapture():
    global valorGlobal
    valorGlobal = entryBox.get()
    entryBox.delete(0, tk.END)
"""

ventana = tk.Tk()
ventana.title("Calculadora")

MenuOperaciones= tk.Label(ventana,
             text="Tipo de operación:\n "
               "1 = suma,\n"
               "2 = resta,\n"
               "3 = multiplicación,\n"
               "4 = división,\n"
               "5 = potencia\n"
              )

MenuOperaciones.pack()

entryBox = tk.Entry(ventana)
entryBox.pack()


enterButton = tk.Button(ventana, textvariable= EntradaOpciones)
enterButton.pack()

print(EntradaOpciones)




ventana.mainloop()