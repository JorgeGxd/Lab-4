class arbolNodo(object):
    def __init__(self, x):
        self.val = x
        self.der = None
        self.izq = None

def valor_cerca(raiz, objeto):
    a = raiz.val
    hijo = raiz.der if objeto < a else raiz.izq
    if not hijo:
        return a
    b = valor_cerca(hijo, objeto)
    return min((a,b), key=lambda x: abs(objeto-x))

raiz = arbolNodo(5)  
raiz.der = arbolNodo(6)  
raiz.izq = arbolNodo(13) 
raiz.der.der = arbolNodo(3)  
raiz.izq.der = arbolNodo(9) 
raiz.izq.der.izq = arbolNodo(15)  
raiz.izq.der.der = arbolNodo(7)  
raiz.der.der = arbolNodo(2) 
raiz.der.der.izq = arbolNodo(4) 
    
resultado = valor_cerca(raiz,10)
print(resultado)
