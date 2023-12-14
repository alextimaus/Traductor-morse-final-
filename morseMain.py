# Este programa convierte una entrada de texto en código Morse y emite el sonido correspondiente.

from ObtenedorDeEntrada import ObtenedorDeEntrada
from ProcesadorDeEntrada import ProcesadorDeEntrada
from interfaz import  interfaz

if __name__ == "__main__":
    entrada = ObtenedorDeEntrada()
    procesador = ProcesadorDeEntrada()
    procesador.procesarEntrada(entrada.getEntrada())                                                   