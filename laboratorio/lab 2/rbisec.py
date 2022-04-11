from math import tan
import sys

def rbisec(fun, inter, err, maxIteration):
    ''' ENTRADA:
        fun: funcion
        inter: lista de dos elementos de la forma [a,b], representan los extremos
        err: tolerancia de error
        maxIteration: numero de iteraciones maximas del programa 

        SALIDA:
        hx: lista con todas las aproximaciones de x
        hf: lista con la evaluaciones correspondiente a x
    '''

    hx = []
    hf = []
    a = inter[0]
    b = inter[1]
    fa = fun(a)
    fb = fun(b)
    distancia = b-a

    if fa * fb > 0:
        raise ValueError ('STOP (1) - La funcion no tiene una raiz en ese intervalo')

    for _ in range(maxIteration):

        distancia = distancia / 2
        c = a + distancia
        hx.append(c)
        fc = fun(c)
        hf.append(fc)
        if abs(distancia) < err or abs(fc) < sys.float_info.epsilon:
            print('\nSTOP (2) - Aproximacion lo suficientemente correcta\n'            )
            break

        if fa * fc < 0:
            b = c
            fb = fc

        else:
            a = c
            fa = fc

    return hx, hf


def printRes (hx, hf):
    for i in range(len(hx)):
        print(f"[{i:2d}]: x: {hx[i]}\t\t f(x): {hf[i]}")