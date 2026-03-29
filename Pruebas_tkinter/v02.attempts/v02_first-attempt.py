import tkinter as tk 

# FUNCIONES DE COMANDO 
"""
def op_function():
     global actual_entry_op
     entryValue_op = actual_entry_op.get()
     print("op: ", entryValue_op)
     entry_op.delete(0, tk.END)

def num1_function():
     global actual_entry_num1
     num1_value = actual_entry_num1.get()
     print("num1: ", num1_value)
     # entry_num1.delete(0, tk.END)


def num2_function():
     global actual_entry_num2
     num2_value = actual_entry_num2.get()
     print("num2: ", num2_value)
     #  entry_num2.delete(0, tk.END)
"""

def result_function():
     global actual_entry_op, actual_entry_num1, actual_entry_num2, result_label
     if result_label is not None:
        result_label.destroy()

     x = int(actual_entry_op.get())
     num1 = int(actual_entry_num1.get())
     num2 = int(actual_entry_num2.get())

     if x == 1:
      result_display = num1 + num2
     elif x == 2:
      result_display = num1 - num2
     elif x == 3:
      result_display = num1 * num2
     elif x == 4:
       if num2 == 0:
        result_display = "error"
       else:
        result_display = num1 / num2
     elif x == 5:
       result_display = num1 ** num2

     result_label = tk.Label(ventana, text=result_display)
     result_label.pack()



# PRE_SET
ventana = tk.Tk()
ventana.title("CALCULADORA")


# MENU
menu_op = tk.Label(ventana, text="Tipo de operación:\n"
                   "1 = suma,\n" 
                   "2 = resta\n"
                   "3 = multiplicación\n" 
                   "4 = división\n "
                   "5 = potencia\n")
menu_op.pack()

actual_entry_op = tk.StringVar()
entry_op = tk.Entry(ventana, textvariable= actual_entry_op)
entry_op.pack()

# button_op = tk.Button(ventana, text= "ENTER", command= op_function)
# button_op.pack()

# NUMERO 1
num1_label = tk.Label(ventana, text= "Numero 1")
num1_label.pack()

actual_entry_num1 = tk.StringVar()
entry_num1 = tk.Entry(ventana, textvariable= actual_entry_num1)
entry_num1.pack()

#button_num1 = tk.Button(ventana, text= "ENTER", command= num1_function)
#button_num1.pack()

# NUMERO 2
num2_label = tk.Label(ventana, text= "Numero 2")
num2_label.pack()

actual_entry_num2 = tk.StringVar()
entry_num2 = tk.Entry(ventana, textvariable= actual_entry_num2)
entry_num2.pack()

#button_num2 = tk.Button(ventana, text= "ENTER", command= num2_function)
#button_num2.pack()


# Resultado  
result_label = None
button_result = tk.Button(ventana, text= "Result", command= result_function)
button_result.pack()

ventana.mainloop()