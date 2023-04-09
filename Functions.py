import numpy as np
import matplotlib.pyplot as plt

def Triangular(universe:list,a:int,b:int,c:int)->list:
    lista = []
    y = []

    for i in universe:
        if i == b:
            y.append(1)
        elif i <= a:
            y.append(0)
        elif i >= a and i <= b:
            y.append(1/(b-a)*(i-a))
        elif i >= b and i <= c:
            y.append(-1/(c-b)*(i-c))
        else:
            y.append(0)
    return y

def Trapezoidal(universe:list,a:int,b:int,c:int,d:int)->list:
    y = []

    for i in universe:
        if i == b:
            y.append(1)
        elif i <= a:
            y.append(0)
        elif i >= a and i <= b:
            y.append(1/(b-a)*(i-a))
        elif i >= b and i <= c:
            y.append(1)
        elif i >= c and i <= d:
            y.append(-1/(d-c)*(i-d))
        else:
            y.append(0)
    return y

def Bell(universe:list,a:int,b:int,c:int)->list:
    lista = []
    y = [(1/(1+np.abs((i-c)/a)**(2*b))) for i in universe]
    return y

def Gaussian(universe:list,c:int,sigma:int)->list:
    lista = []
    y = [(np.exp(-((i-c)**2)/(2*sigma**2))) for i in universe]
    return y

def Sigmoidal(universe,a:float,c:int)->list:
    lista = []
    y = [(1/(1+np.exp(-a*(i-c)))) for i in universe]
    return y

