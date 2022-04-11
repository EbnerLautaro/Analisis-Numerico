
import sys

def rnewton (fun, x0, err, maxIteration):
    ''' ENTRADA:
        fun: funcion que retorna (f(x), f'(x))
        x0: aproximacion inicial
        err: tolerancia de error
        maxIteration: numero de iteraciones maximas del programa 
        SALIDA:
        hx: lista con todas las aproximaciones de x
        hf: lista con la evaluaciones correspondiente a x
    '''
    hx = [] 
    hf = []
    fx1, ffx1 = fun(x0)         # fx1 = f(x1) and ff(x1) = f'(x1)
    hx.append(x0)
    hf.append(fx1)

    if abs(fx1) < sys.float_info.epsilon or abs(ffx1) < sys.float_info.epsilon:
        raise ValueError ('STOP (1)')
    
    for i in range(maxIteration):
        x1 = x0 - (fx1/ffx1)    # Implementacion de la iteracion del metodo de Newton
        fx1,ffx1 = fun(x1)      # fx1 = f(x1) and ff(x1) = f'(x1)
        hx.append(x1)
        hf.append(fx1)

        if abs(x1-x0) > err or (abs(fx1) < sys.float_info.epsilon):
            x0 = x1
        else:
            break

    return hx, hf


