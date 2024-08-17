
# 1)

def lista_rep (lista):

    for i in lista:

        rep=lista.count(i)
        if rep > 1 :
            con = True
            break
        else:
            con = False


    if con == True:

        return print("en la lista hay repeticiones de numeros")
    
    else:  

        return print("no hay repeticiones en la lista")
    

lista= [1,2,3,4,5,6,7,8,9,0]
lis = [1,4,8,9,0,5,6,5,3]

lista_rep(lista)
lista_rep(lis)

# 2)

def vocales (frase):

    palabras = frase.split()

    for i in range(0,len(palabras)):

        p = palabras[i]
        
        if p.count("a") > 1 or p.count("e") > 1 or p.count("i") > 1 or p.count("o") > 1 or p.count("u") > 1 :

            print(p)
            break

    if i == len(palabras):
        print("no existe")
            

palabra ="los estudiantes de programacion"
pal = "un pez es un pez"

vocales(palabra)
vocales(pal)

# 3)

def comparacion (lis1,lis2):
    res = []
    for i in range(0,len(lis1)) :
        m = lis1[i]

        for j in range(0,len(lis2)) :

            if m == lis2[j]:
                break
            
        if j == len(lis2)-1:
            res.append(m)

    print(res)

lis1 = [1,2,3,4,7]
lis2 = [1,2,6,5]

comparacion(lis1,lis2)

# 4)

def promedio (arrglo):

    prom = 0

    for i in range (0,len(arreglo)):

        prom += arreglo[i]

    print(prom/len(arreglo))

arreglo = [1,2,3,4,5,5]

promedio(arreglo)

# 5)

def medio (arreglo):

    arreglo.sort()
    posicion = (len(arreglo)-1)/2
    print(arreglo[int(posicion)])

arreglo2 = [4,6,5,3,7,2,1]

medio(arreglo2)