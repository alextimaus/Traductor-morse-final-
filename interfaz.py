from tkinter import *
from ProcesadorDeEntrada import ProcesadorDeEntrada
from ObtenedorDeEntrada import ObtenedorDeEntrada
from Diccionario import Diccionario
from EmitidorDeSonido import EmitidorDeSonido
import time

ventana = Tk()
ventana.geometry('600x400')
ventana.configure(background='#7c1324')
ventana.title('Principal')
ventana.resizable(width=FALSE, height=FALSE)

etiqueta_titulo = Label(ventana, text='Traductor a código Morse', fg='white', font=('Times New Roman', 20, 'bold'))
etiqueta_titulo.configure(background='#7c1324')
etiqueta_titulo.pack(pady=10)

etiqueta_palabra = Label(ventana, text='Escriba su palabra:', fg='white', font=('Times New Roman', 15))
etiqueta_palabra.configure(background='#7c1324')
etiqueta_palabra.pack(pady=10)

caja_palabra = Entry(ventana, width=25, fg='white', font=('Times New Roman', 15))
caja_palabra.configure(background='#7c1324')
caja_palabra.pack(pady=5)

boton_traducir = Button(ventana, text='Traducir', width=25, fg='white', font=('Times New Roman', 15), command=lambda: procesarEntrada(caja_palabra.get()))
boton_traducir.configure(background='#7c1324')
boton_traducir.pack(pady=10)

etiqueta_resultado = Label(ventana, text='', fg='white', font=('Times New Roman', 15))
etiqueta_resultado.configure(background='#7c1324')
etiqueta_resultado.pack(pady=10)

ventana.bind('<Return>', lambda event: procesarEntrada(caja_palabra.get()))
def procesarEntrada(entrada):
    miDiccionario = Diccionario()
    sonido = EmitidorDeSonido()
    resultado_morse = ""

    for i in entrada.upper():
        if i == " ":
            time.sleep(1)
            continue
        claveMorse = miDiccionario.getMorse(i)
        resultado_morse += f"{i} {claveMorse}\n"

        for j in claveMorse:
            if j == '.':
                sonido.emitirSonidoCorto()
                time.sleep(0.1)
            else:
                sonido.emitirSonidoLargo()
            time.sleep(0.5)
    
    etiqueta_resultado.config(text=resultado_morse)

ventana.mainloop()
