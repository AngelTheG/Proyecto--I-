# Simulador de modelo ISR

Este proyecto es un simulador de una infección codificado entorno al modelo ISR para análisis de probabilidades infecciosas.


#### Requisitos:
   **Librería [Gtk](https://www.gtk.org/docs/installations/linux/)**
  
### Ejecución
Para ejecutar el proyecto se debe abrir el archivo [gui_core.py](https://github.com/AngelTheG/Proyecto--I-/blob/master/gui_core.py) desde la terminal.


## Primer Lanzamiento
Apenas se ejecute el "core" de la interfaz gráfica, se desplegará la ventana núcleo del proyecto.
Los elementos que se logran ver son:
  
  **Botón ABOUT**:
  
  * Este botón despliega una ventana que muestra la información del proyecto además de incluir un botón que te redirige a este repositorio.
   
  **Botón Cambiar Tamaño de la Ventana**:
  
  * Es un botón completamente experimental que está conectado al cambio del tamaño de la ventana (como indica su nombre).
  
  **Entradas COMUNIDAD**:
  
  * En esta sucesión de entradas se ingresan los parámetros con los que se desea trabajar en la simulación
  
  **Entradas ENFERMEDAD**:
  
  * Al igual que en la anterior sucesión de entradas, estas dos entradas pertencen a los valores que se le asignarán a la enfermedad.
  
  **Botón CONFIRMAR**:
  
  * Este botón actua como primer bypass ya que al ser clickeado este desplegará la ventana en la cual los pasos deben ser ingresados además muestra la información previamente ingresada para la simulación.
  
  **Botón CONFIRMAR(pasos)**:
  
  * Una vez que se confirmen los pasos la ejecución de la simulación comenzará a ejecutarse.
  
  **Tabla de resultados**:
  
  * Aquí se desplegará el registro paso por paso de la simulación, mostrando datos como el número del paso, la cantidad de casos activos, casos totales, muertos y curados

## Metodología
El proyecto consta de 7 archivos de ejecución.
Principalmente está el **gui_core.py** el cual como indica su nombre es el núcleo del proyecto, este hereda las clases Numbify, NoGenerated y About. Por útimo consta de los siguientes métodos:

* **openFile**: Accionado por el botón Abrir, el método crea un dialogo de selección de archivo limitado a archivos .csv, una vez abierto procesará la información del archivo si es compatible y la cargará en la tabla (TreeView) en la parte inferior derecha. Es importante destacar que esto solo sucederá si se generó una tabla previamente ya que esto gatilla el proceso de evaluación automática, si se da el caso de accionar el botón sin antes haber generado una escala, se desplegará un dialogo en el que se indica la necesidad de crear una tabla previamente. Puede ocurrir que la tabla no cubra la totalidad de puntos del archivo, por lo que la calificación asignada en ese caso será "Los puntos exceden la escala generada".

* **aboutShow**: Despliega una ventana About llamando a la clase antes importada.

* **generate**: Calcula y muestra una tabla generada según los datos indicados.

* **saveFile**: Guarda los datos desplegados en la tabla, tras cargar un archivo, dentro de un archivo pdf.

### Desarrollado por **Angel Guerrero** y **Yostin Sepúlveda**

#### Gracias especiales a:
**[Ivo Wetzel](https://stackoverflow.com/users/170224/ivo-wetzel)** Por crear el archivo [numbify.py](https://github.com/AngelTheG/Proyecto-3/blob/master/numbify.py) y publicarlo en la página de ayuda de [stack overflow](https://stackoverflow.com/questions/2726839/creating-a-pygtk-text-field-that-only-accepts-number).
  
