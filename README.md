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

**gui_core** (Gtk.Window)
Es el núcleo de la intefáz gráfica del usuario, en esta se llevan a cabo la gran mayoría de métodos relacionados con el despliegue de informacíón en la pantalla. Consta de los siguientes métodos:
  * **udpateLabelStatus** este método se encarga de detectar el cambio dentro de los entrys de cada variable con el fin de cambiar la alerta en caso de tratar de iniciar la simulación con algúna variable vacía.
  
  * **checkEsencials** Este método se activa por el botón CONFIRMAR además se complementa con el anterior, se encarga de detectar los entrys vacíos y les       agrega una alerta a los labels correspondientes, además regula el inicio de la simulación. No se ejecutará la simulación si los parametros no están         completamente entregados.
  
  * **start** Método accionado por el botón de tras pasar positivamente por checkEsencials, este se encarga de recolectar y administrar la información para     entregarla al core de la simulación, este metodo además despliega la ventana donde debe ser ingresado la cantidad de pasos a simular. Antes de             finalizar agrega los datos obtenidos en la tabla de resultados.
  
  * **resize** Se encarga de cambiar el tamaño de la ventana.
  
  * **aboutShow** Muestra el diálogo ABOUT.
  
**gui_stepsWindow** (Gtk.Dialog)
Es la ventana de diálogo encargada de confirmar toda la información de la simulación antes de ejecutarla, además de pedir la cantidad de pasos a simular.

**gui_about** (Gtk.Dialog)
Es la ventana de diálogo contenedora de información del proyecto.

**sim_runner**
Es el objeto encargado de organizar todo para la correcta ejecución de la simulación, funciona como el "main" del código encargado de la simulación, crea la comunidad, la enfermedad y las ingresa de la simulación que también es creada por este objeto (tanto la comunidad, la enfermedad y la comunidad son objetos), su único método es entregar un "log" de la comunidad.

**sim_simulation**
Este objeto se encarga de ejecutar los pasos indicados en la comunidad que se le es entregada.

**sim_comunidad**
Este es uno de los objetos más complejos, apenas es creado genera la población indicada, circulos cercanos y por último infecta inicialmente la cantidad de personas indicadas. Excluyendo los getters el único método que tiene es:

  * **take_step** Este método se encarga de realizar un paso de simulación, checkea los infectados y los hace evolucionar(curarse o morirse), infecta           círculos cercanos y añade la información a un log.

**sim_disease**
La enfermedad, este objeto es poco más que un contenedor de atributos, ya que su único método es llevar el registro de infectados.

**sim_citizen**
El ciudadano o persona, se generada con un identificador único en sim_comunidad, es el objeto más complejo del proyecto, sus métodos son:

  * **add_buddy** Método activado en el momento de la generación de la comunidad, añade "amigos" o "buddies" al círculo cercano de cada persona.
  
  * **enough_buddies** Método accedido en previamente a add_buddy para comprobar si e ciudadano tiene los amigos suficientes o no.
  
  * **infect** Infección segura de un ciudadano, tras activar esto es un ciudadano este se vuelve inmune además de pasar su estado a infectado.
  
  * **attempt_infect** Es el intento de infección que actua de manera aleatorea en función de los parámetros entregados anteriormente, en caso de salir positiva activa el infect() del ciudadano.
  
  * **infect_buddies** Es un método accedido en la comprobación de la comunidad al simular un paso, este checkea la posibilidad de infección dentro de su grupo de amigos cercanos, ejecuta el attempt_infect() en todos sus cercanos.
  
  * **evolve** Este método comprueba el estado de infección de la persona, pasada cierta cantidad de pasos se define si la persona muere o se sana.


### Desarrollado por **Angel Guerrero** y **Yostin Sepúlveda**

#### Gracias especiales a:
**[Ivo Wetzel](https://stackoverflow.com/users/170224/ivo-wetzel)** Por crear las bases para el archivo [numbify.py](https://github.com/AngelTheG/Proyecto--I-/blob/master/gui_numbify.py) y publicarlo en la página de ayuda de [stack overflow](https://stackoverflow.com/questions/2726839/creating-a-pygtk-text-field-that-only-accepts-number).
  
