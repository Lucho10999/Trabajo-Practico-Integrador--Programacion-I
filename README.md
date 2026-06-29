# Trabajo Práctico Integrador (TPI) - Gestión de Datos de Países

&emsp; Programa procesamiento, ordenamiento y análisis estadístico de un dataset demográfico de países. \
El sistema lee y procesa la información en un archivo de texto estructurado en formato CSV. 

**Marco Teórico y Arquitectura**

&emsp; Conforme a lo descripto en el informe adjunto, el programa se diseñó en una estructura general \
desplegada mediante un bucle principal `while` que administra la navegación del usuario, derivando las acciones \
a través de estructuras condicionales `if` anidadas que invocan funciones modulares, ya sea, de uso repetitivo o \
de única responsabilidad.  

**Estructuras de Datos** 

&emsp; Lista: Implementada como la estructura dominante debido a su similitud de forma con las filas de un archivo CSV, \
agilizando la manipulación y la sobrescritura.    
&emsp; Listas de listas: A partir de la implementación de la lista como estructura dominante, surge por consiguiente la \
implementación de la lista de listas para almacenar el archivo CSV en la memoria del programa. \
&emsp; Diccionarios: Utilizados de forma específica en los módulos estadísticos por su accesibilidad clave-valor de \
     continentes, mejorando la legibilidad estética y evitando el uso de variables sueltas. 
     
**Menú de Opciones del programa**
1.  **Agregar país:** Introduciendo Nombre, Población, Superficie y Continente.
2.  **Actualizar los datos de población y superficie:** Modifica los valores numéricos de un país existente y actualiza sus datos.
3.  **Buscar un país:** Consulta rápida en el dataset mediante coincidencias parciales.
4.  **Filtrar países:** Submenú que incluye filtrado por Continente, Rango de población, Rango de superficie y combinación de Múltiples filtros.
5.  **Ordenar países:** Clasificación por Nombre, Población o Superficie en orden ascendente o descendente.
6.  **Visualizar estadísticas:** Reportes automatizados del país con mayor/menor población, promedios demográficos y cantidad total de países por continente mapeados.
7.  **Salir:** Cierre del programa e interrupción del ciclo de ejecución.

**Requisitos , Instalación y despliegue**

**Ruta del Archivo**

&emsp; El programa está preconfigurado para leer y escribir el dataset en la ruta absoluta: \
`c:/Users/Usuario/Desktop/csv.txt`.
Para desplegarlo se debe contar con el archivo en dicha ruta o alterar la ruta dentro del programa

**Ejecución**

&emsp; Contando con un editor de codigo instalado, luego clonando el repositorio a la propia computadora
puede ser iniciado y desplegado.
  

**Archivos y links adjuntos**

Video explicativo: https://drive.google.com/file/d/17JEvlKe0OFDeIWafot31pxZjYZKDgh9U/view?usp=sharing   

Informe adjunto (PDF): https://drive.google.com/file/d/1vRIc3mOPuPTD8ckvchZd8UhAAmxvCg3z/view?usp=sharing
