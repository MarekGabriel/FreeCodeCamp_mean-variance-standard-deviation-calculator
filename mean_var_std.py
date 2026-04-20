import numpy as np

def calculate(lista):

    if len(lista) != 9:
        raise ValueError('List must contain nine numbers.')
    
    tablica = np.array(lista)
    tablica = tablica.reshape(3,3)
    
    srednia_kolumny = [float(i) for i in tablica.mean(axis = 0)]
    srednia_wiersze = [float(i) for i in tablica.mean(axis = 1)]
    srednia_global = float(tablica.mean())
    
    wariancja_kolumny = [float(i) for i in tablica.var(axis = 0)]
    wariancja_wiersze = [float(i) for i in tablica.var(axis = 1)]
    wariancja_global = float(tablica.var())

    std_kolumny = [float(i) for i in tablica.std(axis = 0)]
    std_wiersze = [float(i) for i in tablica.std(axis = 1)]
    std_global = float(tablica.std())

    max_kolumny = [float(i) for i in tablica.max(axis = 0)]
    max_wiersze = [float(i) for i in tablica.max(axis = 1)]
    max_global = float(tablica.max())

    min_kolumny = [float(i) for i in tablica.min(axis = 0)]
    min_wiersze = [float(i) for i in tablica.min(axis = 1)]
    min_global = float(tablica.min())

    suma_kolumny = [float(i) for i in tablica.sum(axis = 0)]
    suma_wiersze = [float(i) for i in tablica.sum(axis = 1)]
    suma_global = float(tablica.sum())
    
    wynik = {'mean': [srednia_kolumny, srednia_wiersze, srednia_global], 
             'variance': [wariancja_kolumny, wariancja_wiersze, wariancja_global], 
             'standard deviation': [std_kolumny, std_wiersze, std_global], 
             'max': [max_kolumny, max_wiersze, max_global], 
             'min': [min_kolumny, min_wiersze, min_global], 
             'sum': [suma_kolumny, suma_wiersze, suma_global]
            }

    return wynik