class arbolNodo(object):
    def __init__(self, x):
        self.val = x
        self.der = None
        self.izq = None

def ordenar(numero):
    
    if not numero:
        return None
    valor = len(numero)//2
    nodo = arbolNodo(numero[valor])
    nodo.izq = ordenar(numero[:valor])
    nodo.der = ordenar(numero[valor+1:])
    return nodo

def preOrden(nodo): 
    if not nodo: 
        return      
    print(nodo.val)
    preOrden(nodo.izq) 
    preOrden(nodo.der) 
    
resultado = ordenar([1,2,3,4,5,6,7,])
preOrden(resultado)