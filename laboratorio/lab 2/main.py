from math import tan

import rbisec
import rnewton


def fun_lab2ej2a (x):
    return (2*x) - tan(x)

hx, hf = rbisec.rbisec(fun_lab2ej2a, [0.8, 1.4], 1e-5, 100)



def fun_lab2ej2b (x):
    return (x**2) - 3

hx2, hf2= rbisec.rbisec(fun_lab2ej2b, [1,4, 2], 1e-5, 100) 
# elijo ese intervalo porque sqrt(2) < sqrt(3) < sqrt(4)



    
if __name__ == '__main__':
    rbisec.printRes(hx2, hf2)
    
    