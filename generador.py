"""
Un generador de senal es el responsable de generar una senal portadora.

"""

class Generador(object):

    import numpy as np

    def __init__(self, amplitud, fase, frecuencia):
        self.amplitud = amplitud
        self.fase = fase
        self.frecuencia = frecuencia

        #  muestras por segundo
        self.frecuencia_muestreo = frecuencia*3

    def generar(self, tiempo_inicial, tiempo_final):

        import math

        cantidad_muestras = (tiempo_final - tiempo_inicial).seconds/\
        self.frecuencia_muestreo

        muestras = range(cantidad_muestras)
        #TODO agregar un ruido blanco a la senal
        noise=np.random.normal(0,1,muestras)    
        ret = [self.amplitud*math.sin(2*(1/self.frecuencia)*i+self.fase) \
        for i in muestras]

        retwithnoise=ret+noise

        return retwithnoise
