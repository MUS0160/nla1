import numpy as np

def f_subst(L, b):
    m, n =  np.shape(L)     # pomocí vhodné funkce numpy uložte do proměnných m, n počet řádků a sloupců L
    x =  np.zeros(n)        # vytvořte vektor samých nul délky n
    x[0] = b[0] / L[0, 0]   # první prvek řešení
    for i in range(1, m):
        # nejdříve pomocí vnořeného for cyklu určíme hodnotu sumy z kroku 2:
        suma = 0
        for j in range(0,i):    # doplňte vhodně meze smyčky
            suma += L[i,j]*x[j] # doplňte
        # odečteme sumu od prvku pravé strany a vydělíme diagonálním prvkem
        x[i] = (b[i] - suma)/L[i,i]     # doplňte
    return x

def b_subst(L, b):
    m, n =  np.shape(L)     
    x =  np.zeros(n)   
    x[m-1] = b[m-1] / L[m-1, n-1]   
    for i in range(m-2, -1, -1):
        suma = 0
        for j in range(m-1,i, -1):
            suma += L[i,j]*x[j] 
        x[i] = (b[i] - suma)/L[i,i]     
    return x

def my_lu(A):
    m,n = np.shape(A)
    U = A
    L = np.eye(m,n)
    for k in range(0, m-1):
        print(f"k cycle: {k}")
        for j in range(k+1, m):
            print(f"j cycle: {k}, {j}")
            L[j,k] = U[j,k]/U[k,k]
            U[j, k:m+1] = U[j, k:m+1] - L[j,k]*U[k, k:m+1]
    return L, U

if __name__ == "__main__":
    np.set_printoptions(precision=3)
    A = np.random.rand(4,4)
    Acopy = A.copy()
    print(A)
    print("\n------------------------------\n")
    L,U = my_lu(Acopy)
    
    #print(U)
    #print("\n------------------------------\n")

    #print(L)
    #print("\n------------------------------\n")

    A2 = L@U
    print("\n------------------------------\n")
    print(A2)
    print("\n------------------------------\n")
    print(A)
    print("\n------------------------------\n")



