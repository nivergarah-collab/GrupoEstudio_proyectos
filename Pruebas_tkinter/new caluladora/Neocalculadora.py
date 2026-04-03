from tkinter import *
# import funciones as f
Buttons = [
 {"tipo":"operacion", "valor":"**", "texto":"exp"},
 {"tipo":"operacion", "valor":"sqr", "texto":"sqr "},
 {"tipo":"trigger", "valor":"c", "texto":"c"},
 {"tipo":"trigger", "valor":"Ce", "texto":"Ce"},
 {"tipo":"operacionPrefija", "valor":"**2", "texto":"exp2"},
 {"tipo":"operacionPrefija", "valor":"sqr2", "texto":"sqr2"},
 {"tipo":"operacionPrefija", "valor":"!", "texto":"!"},
 {"tipo":"operacionPrefija", "valor":"1/x", "texto":"1/x"},
 {"tipo":"numero", "valor":2.71828, "texto":"e"},
 {"tipo":"numero", "valor":3.1415, "texto":"π"},
 {"tipo":"numero", "valor":1.61803, "texto":"phi"},
 {"tipo":"operacion", "valor":"/", "texto":"/"},
 {"tipo":"numero", "valor":7, "texto":"7"},
 {"tipo":"numero", "valor":8, "texto":"8"},
 {"tipo":"numero", "valor":9, "texto":"9"},
 {"tipo":"operacion", "valor":"*", "texto":"*"},
 {"tipo":"numero", "valor":4,"texto":"4"},
 {"tipo":"numero", "valor":5,"texto":"5"},
 {"tipo":"numero", "valor":6,"texto":"6"},
 {"tipo":"operacion", "valor":"-", "texto":"-"}, 
 {"tipo":"numero", "valor":1, "texto":"1"},
 {"tipo":"numero", "valor":2, "texto":"2"},
 {"tipo":"numero", "valor":3, "texto":"3"},
 {"tipo":"operacion", "valor":"+", "texto":"+"},
 {"tipo":"operacion", "valor":"log", "texto":"log"},
 {"tipo":"numero","valor":0, "texto":"0"},
 {"tipo":"trigger","valor":".","texto":"."},
 {"tipo":"trigger","valor":"=","texto":"="}
]
number1 = None
number2 = None
operacion_vigente = None
tipo_vigente = None
resultado = None
number_status = 0
def numero(item):
    global number_status
    print("inside numberStatus", number_status)
    if number_status == 0:
     global number1
     number1 = int(item["valor"])
     print("numero1: ", number1)
    elif number_status == 1:
     global number2
     number2 = int(item["valor"])
     print("numero2: ", number2)
    else:
       print("otro number stauts")

def operacion(item):
     global number_status
     global operacion_vigente
     global tipo_vigente
     global number1
     if number1 != None:
      number_status = 1
      operacion_vigente,tipo_vigente = item["valor"],item["tipo"]
     else:
       number_status = 1
       number1 = 0
       operacion_vigente,tipo_vigente = item["valor"],item["tipo"]

def trigger(item):
    if  item["valor"] == "=": 
     global resultado
     global operacion_vigente
     global tipo_vigente
     global number_status
     if tipo_vigente == "operacionPrefija" and number2 != None: 
       resultado = "error"
     else: 
      if operacion_vigente == "**": 
       resultado = number1 ** number2
      elif operacion_vigente == "sqr":
       resultado = number1 ** (number2 ** -1)
      elif operacion_vigente == "**2":
       resultado = number1 ** 2    
      elif operacion_vigente == "sqr2":
       resultado = number1 ** 0.5
      elif operacion_vigente == "!":
       for i in range (1, number1 + 1):
        resultado *= i
      elif operacion_vigente == "1/x":
       resultado = 1 / (number1 ** -1)
      elif operacion_vigente == "/":
       resultado = number1 / number2
      elif operacion_vigente == "*":
       resultado = number1 * number2
      elif operacion_vigente == "-":
       resultado = number1 - number2
      elif operacion_vigente == "+":
       resultado = number1 + number2
      else: 
       print('Error en la funcion igual')    
     print(resultado)
     number_status = 0 

    # if i["valor"] == "c": 
    # global number_status
    # global number1
    # global number2

ventana=Tk()
ventana.title("NEOCalculator")
e=Entry(ventana, width=25, borderwidth=5) 
e.grid(row=0,column=0,columnspan=3)


def button_click(item):
 print(item)
 if item["tipo"] == "operacion" or item["tipo"] == "operacionPrefija": 
   operacion(item)
 elif item["tipo"] == "trigger":
   trigger(item)
 elif item["tipo"] == "numero":  
   numero(item)
    




buttons_list = []
count = 0
for item in Buttons:
    button_i = Button(
        ventana,
        text=item["texto"],
        padx=25,
        pady=25,
        command=lambda valor=item: button_click(valor)
    )

    button_i.grid(row=(count // 4) + 1, column=count % 4)
    buttons_list.append(button_i)
    count += 1


















ventana.mainloop()