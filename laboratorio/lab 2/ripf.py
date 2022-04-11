from json import tool
import sys

import toml

def ripf(fun, x0, err, maxIteration):
    ''' ENTRADA:
        fun: funcion que retorna f(x)
        x0: aproximacion inicial para el metodo de Newton
        err: tolerancia de error
        maxIteration: numero de iteraciones maximas del programa 
        SALIDA
    '''
    hx = []
    hx.append(x0)
    for i in range(maxIteration):
        x = fun(x0)
        hx.append(x)
        if abs(x-x0) < err:
            break

        else:
            x0=x
    return hx


def printRes_ripf(hx):
    for i in range(len(hx)):
        print(f"[{i:2d}] x: {hx[i]}")


def f (x):
    return x**3 + 4*x**2 - 10

ax = ripf(f, -3, 10e-5,10)
printRes_ripf(ax)