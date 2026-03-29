import tkinter as tk


valor_ingresado = None

def asignacionDeVariable():
    global valor_ingresado
    valor_ingresado = casillaInput.get()
    print("Variable actualizada a:", valor_ingresado)
    casillaInput.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("CALCULADORA")

menuOperaciones = tk.Label(
    ventana,
    text="Tipo de operación:\n"
         "1 = suma\n"
         "2 = resta\n"
         "3 = multiplicación\n"
         "4 = división\n"
         "5 = potencia"
)
menuOperaciones.pack()

casillaInput = tk.Entry(ventana)
casillaInput.pack()

botonInput = tk.Button(
    ventana,
    text='ENTER',
    command=asignacionDeVariable
)
botonInput.pack()

ventana.mainloop()