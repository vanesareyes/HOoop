class Detector(object):
    import numpy as np
    def __init__(self,umbral):
        #TODO: completar con la inicializacion de los parametros del objeto
        pass

    def detectar(self, senal, umbral):
        
      #  signal_det=np.array(10)
      # for i in range(len(senal)):

      if max(senal)>umbral:
        return 1
      else:
        return 0

  #    return signal_det
        #TODO: Completar
   #     pass
