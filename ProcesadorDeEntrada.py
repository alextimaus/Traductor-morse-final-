from EmitidorDeSonido import EmitidorDeSonido
from Diccionario import Diccionario
import time


class ProcesadorDeEntrada:
    def procesarEntrada(self, entrada):
        miDiccionario = Diccionario()
        sonido = EmitidorDeSonido()

        for i in entrada.upper():
            if i == " ":
                time.sleep(1)
                continue
            claveMorse = miDiccionario.getMorse(i)
            print(i, " " + claveMorse)

            for j in claveMorse:
                if j == ".":
                    sonido.emitirSonidoCorto()
                else:
                    sonido.emitirSonidoLargo()
                time.sleep(0.5)
