import tkinter as tk

root = tk.Tk()
root.title("Grid de Botones Compacto")

# Lista de textos para los botones
textos = ['Botón 1', 'Botón 2', 'Botón 3', 'Botón 4', 'Botón 5', 'Botón 6']
botones = []
contador = 0

for texto in textos:
    btn = tk.Button(root, text=texto)
    btn.grid(row=contador // 3, column=contador % 3)
    botones.append(btn)  # Guarda el botón en la lista
    contador += 1   


botones[0].config(text="boton 1")  # Modifica el primer botón   
root.mainloop()



