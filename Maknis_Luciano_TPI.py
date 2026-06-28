# Utilizadas en varias opciones 
def validar_texto(n):   # Funcion para validar texto, no sea espacio en blanco y no contenga numeros.   
    if n =="":
        print("\nNombre vacio,comience de nuevo\n")
        return False
    if not n.replace(" ", "").isalpha():
        print("\nNombre invalido,ningun país tiene numeros\n")
        return False
    return True 
def validar_numero(n): # Funcion para validar numeros, no sea espacio en blanco y no contenga letras.  
    if n =="":
        print("\nEspacio vacio,comience de nuevo\n")
        return False
    if not n.isdigit():
        print("\nNumero invalido,intente de nuevo\n")
        return False
    return True
def copiar_lista(): # La funcion copia el archivo CSV a una lista para el uso que se nesesite
    with open("c:/Users/Usuario/Desktop/csv.txt","r",newline="",encoding="UTF-8") as archivo:
            lector= csv.reader(archivo)
            return list(lector)
def mostrar_tabla_paises(n): # Funcion para mostrar en la consola ,alineados, los elementos de la lista requeridos
    print(f"{"país":<20} {"poblacion":<12} {"superficie":<12} {"continente":<15}\n")
    for i in n:
        print(f"{i[0]:<20} {i[1]:<12} {i[2]:<12} {i[3]:<15}") 
def texto_a_lower(n):# Utilizada en opcion 4-1 .Esta funcion normaliza el texto como la categoria continente o pais de la lista                                   
     return n.strip().replace(" ","").replace("í","i").lower()
         
# Utilizadas en opcion 1 
def pais_repetido(n,opcion_uno): #Utilizada en opcion 1 y 2
    repetido= False            # La funcion toma lo introducido por el usuario y luego                               
    for i in lista:            # Recorre la lista, informa si el pais ya se encuentra en los datos                                   
        if texto_a_lower(n) == texto_a_lower(i[0]) :# en la opcion 1 no es lo deseado en la opcion 2 si lo es                                        
            repetido= True 
    
    if opcion_uno:
        if repetido: # Informa si el pais ya se encuentra en los datos
            print("\nEl pais ya se encuentra en la lista\n")
            return True
        else:
            return False  
    else:
        if not repetido: # A la inversa de lo anterior, informa si el pais no encuentra en los datos 
            print("\nEl pais no se encuentra en la lista\n")
            return False
        return True  
def agregar_y_mostrar(n,m,o,p):
    m= int(m)  # Pasamos los valores a int si es nesesario 
    o= int(o)
    
    lista_pasaje.append(n)  # Agregamos lo elementos solicitado a una lista
    lista_pasaje.append(m)
    lista_pasaje.append(o)
    lista_pasaje.append(p)
    print(f"\nLos nuevos datos agregados son:\n ")
    print(f"{"país":<20} {"poblacion":<12} {"superficie":<12} {"continente":<15}") 
    print(f"{lista_pasaje[0]:<20} {lista_pasaje[1]:<12} {lista_pasaje[2]:<12} {lista_pasaje[3]:<15}") 
               
def guardar_en_archivo(ruta, lista): # La funcion guarda en una nueva linea del archivo CSV los nuevos datos 
    with open(ruta,"a", newline="",encoding="UTF-8") as archivo:                      
                    escritor= csv.writer(archivo)
                    escritor.writerow(lista)
                    
# Utilizada en opcion 2
def actualizar_lista(n,m,o):  # La funcion toma los valores introducidos por el usuario
    m= int(poblacion)         # el pais el cual fue verificado que este en la lista
    o= int(superficie)        # lo suma con el nuevo dato de superficie y poblacion
    for i in range (len(lista)):
        if texto_a_lower(n) == texto_a_lower(lista[i][0]):
            lista[i][1]=m
            lista[i][2]=o
            print(f"\nLos datos actualizados son:\n ")
            mostrar_tabla_paises(lista[1:])                        
            break                     
def guardar_en_archivo_sobrescribir(ruta, lista): # La funcion sobreescribe el archivo por completo                 
    with open(ruta,"w", newline="",encoding="UTF-8") as archivo: # que se usa para modificar un elemento de la lista                       
                    escritor= csv.writer(archivo) 
                    escritor.writerows(lista)
                     
# Utilizada en opcion 3
def busqueda_tres(n,m,busqueda):
    for i in n:  # toma la busqueda y verifica con "in" si esta el en primer elemento, categoria nombre del pais 
        
        if busqueda in (i[0]).strip().replace(" ","").replace("í","i").lower() :                
            m.append(i)
# Utilizadas en opcion 4
def busqueda_tres(n,m,busqueda): # Toma la busqueda y verifica con "==" los elemenos de categoria
    for i in n[1:]:              # continente que coinciden            

        if busqueda == texto_a_lower(i[3]):                        
            m.append(i) 
def opcion_cuatro_dos_y_tres(n,m,cuatro_dos):  # Utilizada en opcion 4 - 2 y 3
    if cuatro_dos:
        for i in lista[1:]: # Comparamos los limites con la categoria correspondiente  
            if n <= int(i[1]) and m >= int(i[1]) :                        
                lista_busqueda.append(i)
    elif not cuatro_dos:
        for i in lista[1:]:                  
            if n <= int(i[2]) and m >= int(i[2]) :                        
                lista_busqueda.append(i)           
# Utilizadas en opcion 5 
def ordenar_por_nombre(n,m,cinco_uno): # Utilizada en opcion 5 - 1  
    if cinco_uno:                      # La funcion utiliza el metodo sorted en la columna pais
        n = sorted(m[1:])              # devolviendo ordenado alfabeticamente 
        print("\nLos paises de la A a la Z son\n")                   
        mostrar_tabla_paises(n) 
    elif not cinco_uno:
        n=sorted(m[1:],reverse=True)
        print("\nLos paises de la Z a la A son\n")
        mostrar_tabla_paises(n) 
def burbuja1(n,opcion_cinco_dos): #Utilizada en opcion 5 - 2
    if opcion_cinco_dos:
        for i in range (len(n)-1):  # Utilizamos el algoritmo burbuja
            hizo_intercambio= False                 # para ordenar la lista que copia el archivo CSV
                                                    # quedando el menor arriba y el mayor abajo
            for x in range(len(n)-1 -i):
                if int(n[x][1]) > int(n[x+1][1]):
                    n[x] , n[x+1] = n[x+1] , n[x]
                    hizo_intercambio= True
                    
            if not hizo_intercambio:
                break
        
        print(f"\nLos paises por población ascendente son:\n ")
        mostrar_tabla_paises(n)
    if not opcion_cinco_dos:
        for i in range (len(n)-1):  # Utilizamos lo anterior 
            hizo_intercambio= False                  # Cambiando ">" a "<" para obtener
                                                    # el mayor arriba y el menor abajo
            for x in range(len(n)-1 -i): 
                if int(n[x][1]) < int(n[x+1][1]):
                    n[x] , n[x+1] = n[x+1] , n[x]
                    hizo_intercambio= True
                    
            if not hizo_intercambio:
                break
            
        print(f"\nLos paises por población descendente son:\n ")                        
        mostrar_tabla_paises(n)
def burbuja(n,opcion_cinco_3):    #Utilizada en opcion 5 - 3
    if opcion_cinco_3:           # Es la funcion anterior adaptada a otra opcion
        for i in range (len(n)-1):  
            hizo_intercambio= False                  
                                                    
            for x in range(len(n)-1 -i): 
                if int(n[x][2]) < int(n[x+1][2]):
                    n[x] , n[x+1] = n[x+1] , n[x]
                    hizo_intercambio= True
                    
            if not hizo_intercambio:
                break
            
        print(f"\nLos paises por superficie descendente son:\n ")
        mostrar_tabla_paises(n)
    if not opcion_cinco_3:
        for i in range (len(n)-1):  
            hizo_intercambio= False                 
                                                    
            for x in range(len(n)-1 -i):
                if int(n[x][2]) > int(n[x+1][2]):
                    n[x] , n[x+1] = n[x+1] , n[x]
                    hizo_intercambio= True
                    
            if not hizo_intercambio:
                break
        
        print(f"\nLos paises por superficie ascendente son:\n ")
        mostrar_tabla_paises(n)
        
# Utilizadas en opcion 6 
def maximo_y_minimo(n):  # Utilizada en opcion 6 - 1
    menos_inf= -math.inf  # Saltando las categorias con 1:, toma el primer elemento 
    inf= math.inf       # y lo compara con menos infinito, de ahi en adelante la
    maximo= "texto"     # variable se queda con "el mayor visto hasta ahora" hasta finalizar el bucle
    minimo= "texto"          
    for i in lista[1:]:         
        poblacion= int(i[1]) 
        if poblacion> menos_inf:
            menos_inf =poblacion
            maximo =i[0]
            
        if poblacion< inf:  # De la misma forma pero partiendo de infinito positivo se encuentra el minimo
            inf =poblacion
            minimo =i[0]    
    print(f"\nEl país con mayor poblacion es {maximo} y país con menor poblacion es {minimo}\n") 
   
def promedio(n,opcion_seis_dos,suma = 0): # opcion 6 - 2 y 3 
    if opcion_seis_dos:
        for i in n[1:]:           # Se recogen las superficies saltando las categorias con [1:]
            superficie= int(i[2])    # se las suma y divide por las longitud de la lista
            suma += superficie       # obtenido con la logitud de la lista len()
        print(f"\nEl promedio de superficie es {suma/len(lista):.0f} Km²\n")
    elif not opcion_seis_dos:
        for i in n[1:]:           # Se utiliza el mismo modus operandi de lo anterior para la poblacion        
            poblacion= int(i[1])     
            suma += poblacion        
        print(f"\nEl promedio de poblacion es {suma/len(lista):.0f} personas\n")

def validar_filtro(n): # opcion 6 - 4
    if n == "si" or n == "no": # Valida si la entrada que recibe la opcion es "si" o "no"
        return True
    else:
        print("""\nSolo es valido "si" o "no" en este campo, de vuelta al menu\n""")        
        return False
def paises_por_continente(m):
    for i in lista: # Funcion para contar los paises por continente
        if i[3] in m:
            m[i[3]] +=1
                                                        
        if i[3]== "Europa/Asia":
            m["Asia"] +=1 
            m["Europa"] +=1
            
def nro_por_continentes(n): # Funcion para mostrar en pantalla los paises por continente
        print(f"\n{"Continente":<15} {"Cantidad de Países":<10}")
        print(f"""
{"Asia":<15} {n["Asia"]:<10} 
{"Europa":<15} {n["Europa"]:<10}
{"America":<15} {n["America"]:<10}
{"Africa":<15} {n["africa"]:<10}
{"Oceanía":<15} {n["Oceanía"]:<10}
                          \n""")

import math
import csv
lista=[]
opcion= 0

while opcion != 7:  # \n    
    print(f"""\n --------- === Menu === ---------   
1 Agregar país               
2 Actualizar los datos de población y superficie 
3 Buscar un país
4 Filtrar países
5 Ordenar países
6 Visualizar estadísticas
7 Salir          
            """)
    
    seleccion= input("\nSeleccione un opcion, utilizando los numeros ")
    
    if seleccion == "1": 
            pais= input("\nIntroduzca el nombre del país a agregar ").strip().capitalize()
            # Se reciben y validan los elementos de la lista de paises. Nombre,poblacion,superficie,continente.          
            
            if not validar_texto(pais):
                continue 
            
            lista=copiar_lista() # Copia el archivo CSV para evaluar sus nombres
            
            opcion_uno= True      
  
            if pais_repetido(pais,opcion_uno):
                continue
            
            poblacion= input("\nIntroduzca la poblacion del país a agregar ").strip()           
            if not validar_numero(poblacion):
                continue
            superficie= input("\nIntroduzca la superficie del país a agregar ").strip()
            if not validar_numero(superficie):
                continue
            continente= input("\nIntroduzca el continente del país a agregar ").strip().capitalize()
            if not validar_texto(continente):
                continue
            
            lista_pasaje=[]             
                
            agregar_y_mostrar(pais,poblacion,superficie,continente)    
                       
            # Sumamos la lista como un ultima linea al archivo CSV
            guardar_en_archivo("c:/Users/Usuario/Desktop/csv.txt", lista_pasaje)
                                            
    if seleccion == "2": # Repitiendo lo anterior se toman los datos
        
            pais= input("\nIntroduzca el nombre del país a actualizar ").strip().capitalize()
            # Se reciben y validan los elementos de la lista de paises. Nombre,poblacion,superficie,continente.          
            if not validar_texto(pais):
                continue
            
            lista=copiar_lista() # Copia el archivo CSV para evaluar sus nombres
           
            opcion_uno= False
   
            if not pais_repetido(pais,opcion_uno):
                continue
            
            poblacion= input("\nIntroduzca la nueva poblacion del país ").strip()           
            if not validar_numero(poblacion): 
                continue
            superficie= input("\nIntroduzca la nueva superficie del país ").strip()
            if not validar_numero(superficie):
                continue
        
            actualizar_lista(pais,poblacion,superficie) # Luego de actualizar el pais en la lista
                                                        # se reescribe el archivo por completo                    
                                                        # con el pais actualizado                 
            guardar_en_archivo_sobrescribir("c:/Users/Usuario/Desktop/csv.txt", lista)   #queda en archivo prueba                     
    if seleccion == "3":
        lista=copiar_lista() # aplicando mismos metodo a la busqueda del usuario y la busqueda en el bucle for de la funcion                           
        
        busqueda=input("Buscar país ").strip().replace(" ","").replace("í","i").lower()
        if not validar_texto(busqueda): 
            continue
        lista_busqueda=[]  #se reinicia la lista

        busqueda_tres(lista,lista_busqueda,busqueda)
        print(f"""\nLas coincidencias encontradas con "{busqueda}" son:\n """)
        mostrar_tabla_paises(lista_busqueda)
                                             
    if seleccion == "4":           
            print(f"""\n --- === Filtrar países por === ---   
1 Continente   
2 Rango de población
3 Rango de superficie
4 Multiples filtros
 
5 Volver al menu           
            """)
            selec =input("\nSeleccione un opcion, utilizando los numeros ")
            if selec == "1":       # Reciclando lo anterior de la opcion 3 se busca el continente
                busqueda=input("Introduzca el Continente ").strip().replace(" ","").replace("í","i").lower() 
                if not validar_texto(busqueda):
                    continue         # Se utiliza la funcion para normalizar lo que introduce el usuario 
                                    # con los nombres de la lista
                lista_busqueda=[]                                         
                lista=copiar_lista() # Se busca utilizando la funcion y muestra en pantalla
            
                busqueda_tres(lista,lista_busqueda,busqueda)                      
                print(f"""\nLos paises en "{busqueda}" son:\n """)
                mostrar_tabla_paises(lista_busqueda)
                
            if selec == "2":                
                inferior=input("Introduzca la cota inferior ").strip()                               
                if not validar_numero(inferior):   #Se pide al usuario los limites 
                    continue                       # luego se lo valida
                superior=input("Introduzca la cota superior ").strip()
                if not validar_numero(superior):
                    continue
                
                lista=copiar_lista()              
                lista_busqueda=[]
                inferior=int(inferior)  # utilizando la funcion se buscan elementos e
                superior=int(superior)  # entre los limites
                
                cuatro_dos=True
                opcion_cuatro_dos_y_tres(inferior,superior,cuatro_dos)
                                        
                print(f"""\nLos paises con población en rango "{inferior}-{superior}" son:\n """)
                mostrar_tabla_paises(lista_busqueda) 
                           
            if selec == "3":                
                inferior=input("Introduzca la cota inferior ").strip()                               
                if not validar_numero(inferior): # se repite el accionar de la opcion anterior
                    continue                    
                superior=input("Introduzca la cota superior ").strip()
                if not validar_numero(superior):
                    continue
                
                lista=copiar_lista()                
                lista_busqueda=[]
                inferior=int(inferior)
                superior=int(superior)                
                
                cuatro_dos=False
                opcion_cuatro_dos_y_tres(inferior,superior,cuatro_dos)                
                        
                print(f"""\nLos paises con superficie en rango "{inferior}-{superior}" son:\n """)
                mostrar_tabla_paises(lista_busqueda)     
               
            if selec == "4":
                print(f"""\n=== ¿Que filtro desea aplicar? ===
Seleccione con "si" o "no"\n""")  # Se consulta al usuario por "si" o por "no"
                
                filtro =input("\nDesea aplicar el filtro continente ").strip().lower()
                if not validar_filtro(filtro):
                    continue
                
                filtro1 =input("\nDesea aplicar el filtro rango de población ").strip().lower()
                if not validar_filtro(filtro1):
                    continue
                 
                filtro2 =input("\nDesea aplicar el filtro rango de superficie ").strip().lower()
                if not validar_filtro(filtro2):
                    continue
                
                filtros=copiar_lista()  # Se copia el archivo CSV a una nueva variable
                               
                if filtro == "si":    
                    busqueda=input("\nIntroduzca el Continente ").strip().lower() 
                    if not validar_texto(busqueda):
                        continue
                    lista=copiar_lista()                
                    lista_busqueda=[]   # Se filtran de la lista lo elemento que no cumplen con la condicion
                    
                    filtros = [i for i in filtros[1:] if busqueda== (i[3]).strip().replace("í","i").lower()]
                     
                if filtro1 == "si":
                    inferior=input("\nIntroduzca la cota inferior para la poblacion ").strip()                               
                    if not validar_numero(inferior):
                        continue 
                    superior=input("Introduzca la cota superior para la poblacion ").strip()
                    if not validar_numero(superior):
                        continue
                    
                    lista=copiar_lista()              
                    inferior=int(inferior)
                    superior=int(superior) #En caso de haber pasado un filtro recibe la lista ya reducida
                    
                    filtros = [i for i in filtros[1:] if inferior <= int(i[1]) and superior >= int(i[1]) ]
                                     
                    
                if filtro2 == "si":
                    inferior=input("\nIntroduzca la cota inferior para la superficie ").strip()                               
                    if not validar_numero(inferior):
                        continue 
                    superior=input("Introduzca la cota superior para la superficie ").strip()
                    if not validar_numero(superior):
                        continue
                    
                    lista=copiar_lista()                
                    
                    inferior=int(inferior)
                    superior=int(superior)
                    
                    filtros = [i for i in filtros[1:] if inferior <= int(i[2]) and superior >= int(i[2]) ]
                    
                print(f"\nLos paises en filtrados son:\n ")
                mostrar_tabla_paises(filtros)          
            if selec == "5":
                continue                        
            
    if seleccion == "5":
            print(f"""\n --- === Ordenar países por === ---   
1 Nombre   
2 Población
3 Superficie 
   
4 Volver al menu           
                """)
            selec =input("\nSeleccione un opcion, utilizando los numeros ")
            if selec== "1":
                print(f"""\n --- === Ordenar nombres por === ---   
1 Nombres de A a Z   
2 Nombres de Z a A
                           
                                """) 
                selec =input("\nSeleccione un opcion, utilizando los numeros ")
                lista=copiar_lista() ; lista_por_nombre=[] ; cinco_uno= True                
  
                if selec== "1":                    
                    ordenar_por_nombre(lista_por_nombre,lista,cinco_uno)              
                if selec== "2":
                    cinco_uno= False
                    ordenar_por_nombre(lista_por_nombre,lista,cinco_uno)
               
            if selec== "2":
                print(f"""\n --- === Ordenar población por === ---   
1 Población ascendente  
2 Población descendente
                            
                                """)
                selec =input("\nSeleccione un opcion, utilizando los numeros ")
                
                lista=copiar_lista()
                lista_para_burbuja= lista[1:]     # Se tuvo que hacer una lista sin categorias para que funcione
                
                
                if selec== "1":
                        opcion_cinco_dos= True
                        burbuja1(lista_para_burbuja,opcion_cinco_dos) 
                        
                if selec== "2":
                        opcion_cinco_dos= False
                        burbuja1(lista_para_burbuja,opcion_cinco_dos) 
                        
            if selec == "3":
                print(f"""\n --- === Ordenar superficie por === ---   
1 Superficie ascendente  
2 Superficie descendente
                            
                                """)
                selec =input("\nSeleccione un opcion, utilizando los numeros ")
                
                lista=copiar_lista()
                lista_para_burbuja= lista[1:]     # Repitiendo lo anterior aplicado a la superfie en lugar de poblacion
                                
                if selec== "1":
                        opcion_cinco_3= False       
                        burbuja(lista_para_burbuja,opcion_cinco_3)  
                                                    
                if selec== "2":
                        opcion_cinco_3= True       
                        burbuja(lista_para_burbuja,opcion_cinco_3)
                                   
                if selec == "4":
                    continue                     
    if seleccion == "6":
                print(f"""\n --- === estadísticas === ---   
1 País con mayor y menor población 
2 Promedio de poblacion
3 Promedio de superficie
4 Cantidad de países por continente

5 Volver al menu          
                """)
                selec =input("\nSeleccione un opcion, utilizando los numeros ")
                if selec== "1":
                    lista=copiar_lista()
                                   
                    maximo_y_minimo(lista)                           
                if selec== "2":
                    lista=copiar_lista()
                    opcion_seis_dos= False # Para que la funcion "promedio(n) devuelta poblacion o superficie "
                    promedio(lista,opcion_seis_dos) # se altera la variable "punto_3"

                if selec== "3":
                    lista=copiar_lista()    
                    opcion_seis_dos= True
                    promedio(lista,opcion_seis_dos)
                             
                if selec== "4":
                    lista=copiar_lista() # A cada continente en el diccionario se le suma +=1 por cada vez que aparece
                                         # al recorrer la lista. Un pais aparece en dos Europa/Asia
                    diccionarios_continentes={ "Asia":0 , "Europa": 0 ,"America": 0 , "Oceanía": 0,  "africa": 0}  

                    paises_por_continente(diccionarios_continentes)
                                               
                    nro_por_continentes(diccionarios_continentes)        
                if selec == "5":
                    continue                      
    if seleccion == "7":
        break        